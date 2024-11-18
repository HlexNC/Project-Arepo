import streamlit as st
import requests
import os
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Chatbot:
    def __init__(self, rasa_url=None, session_id=None):
        """
        Initializes the Chatbot instance.

        Parameters:
        - rasa_url (str): The base URL for the Rasa server.
        - session_id (str): A unique identifier for the user session.
        """
        self.rasa_url = rasa_url or os.getenv("RASA_SERVER", "http://rasa:5005")
        self.webhook_url = f"{self.rasa_url}/webhooks/rest/webhook"
        self.status_url = f"{self.rasa_url}/status"
        self.session_id = session_id or "user"

    def send_message(self, message):
        """
        Sends a message to the Rasa chatbot and retrieves the response.

        Parameters:
        - message (str): The user's input message.

        Returns:
        - list: A list of responses from the chatbot.
        """
        payload = {
            "sender": self.session_id,
            "message": message,
        }
        try:
            response = requests.post(self.webhook_url, json=payload, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            st.error(f"Error communicating with the chatbot: {e}")
            logger.error(f"Error communicating with the chatbot: {e}")
            return [{"text": "I'm sorry, but I'm unable to process your request at this time."}]

    def get_status(self):
        """
        Retrieves the current status of the Rasa server.

        Returns:
        - dict: The status information of the Rasa server.
        """
        try:
            response = requests.get(self.status_url, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            if response.status_code == 409:
                logger.warning("Received 409 Conflict when accessing /status endpoint.")
                return {"status": "conflict"}
            else:
                st.error(f"HTTP error occurred while fetching status: {http_err}")
                logger.error(f"HTTP error occurred while fetching status: {http_err}")
                return {}
        except requests.exceptions.RequestException as e:
            st.error(f"Error fetching chatbot status: {e}")
            logger.error(f"Error fetching chatbot status: {e}")
            return {}

    def is_model_ready(self, max_retries=5, backoff_factor=2):
        """
        Checks if the Rasa model is loaded and ready.

        Parameters:
        - max_retries (int): Maximum number of retries.
        - backoff_factor (int): Factor by which to increase wait time between retries.

        Returns:
        - bool: True if the model is ready, False otherwise.
        """
        for attempt in range(1, max_retries + 1):
            status = self.get_status()
            model_file = status.get("model_file")
            num_active_training_jobs = status.get("num_active_training_jobs", 0)
            logger.info(f"Attempt {attempt}: Rasa model file - {model_file}, active training jobs - {num_active_training_jobs}")

            if model_file and num_active_training_jobs == 0:
                logger.info("Rasa model is ready.")
                return True
            elif num_active_training_jobs > 0:
                wait_time = backoff_factor ** attempt
                st.info(f"Rasa model is still loading (active training jobs: {num_active_training_jobs}). Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
            else:
                logger.warning("Rasa model status is unknown or not ready.")
                st.warning("Chatbot status is unknown. Please ensure the Rasa server is running correctly.")
                return False

        st.error("Chatbot is not ready after multiple attempts. Please ensure a model is trained and loaded correctly.")
        return False

    def run(self):
        """
        Runs the chatbot interface within the Streamlit app.
        """
        if "messages" not in st.session_state:
            st.session_state["messages"] = []

        st.markdown("### Chatbot")

        # Display message suggestions
        with st.sidebar:
            st.write("#### Message Suggestions")
            suggestions = [
                "Hello!",
                "Can you provide a data analysis summary?",
                "I need a health recommendation.",
                "Tell me a joke.",
                "What's your favorite color?"
            ]
            for suggestion in suggestions:
                if st.button(suggestion, key=f"suggestion_{suggestion}"):
                    st.session_state["input"] = suggestion

        # Display previous messages
        for message in st.session_state["messages"]:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Message input
        prompt = st.chat_input("Enter your message:")

        # Handle input from suggestions
        if "input" in st.session_state:
            prompt = st.session_state.pop("input")

        if prompt:
            # Check if the model is ready before sending the message
            if not self.is_model_ready():
                st.warning("Chatbot is currently unavailable. Please train and load a model as per the README instructions.")
                return  # Exit the function without sending the message

            # Proceed to send the message
            st.session_state["messages"].append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            responses = self.send_message(prompt)
            for resp in responses:
                st.session_state["messages"].append({"role": "assistant", "content": resp.get("text", "No response from chatbot.")})
                with st.chat_message("assistant"):
                    st.markdown(resp.get("text", "No response from chatbot."))
