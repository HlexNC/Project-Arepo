Lastname1, Firstname1, 123456

Lastname2, Firstname2, 123456

Project Apero

https://github.com/THD-AI-2023/AIN-B-3-Assistant-Systems

https://github.com/THD-AI-2023/AIN-B-3-Assistant-Systems/-/wikis/home

![Project Apero Banner](./docs/.ASP_Banner.png)

## Project description

**Project Apero** is an advanced recommendation system designed to enhance user experience by providing personalized suggestions based on user behavior and preferences. Leveraging modern technologies such as Streamlit for the frontend and Rasa for chatbot integration, this project aims to deliver an intuitive and efficient system for diverse applications.

## Installation

### Prerequisites

- **Docker:** Ensure Docker is installed on your system.
- **Git:** For cloning the repository and managing submodules.

### Steps

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/THD-AI-2023/AIN-B-3-Assistant-Systems.git
    cd Assistant-Systems-Project
    ```

<!--
2. **Set Up Virtual Environments (Optional):**
    If you prefer to run the application without Docker, you can set up virtual environments for each component.

    **Create and Activate Virtual Environment for Streamlit App:**
    ```bash
    python3 -m venv venv_streamlit
    source venv_streamlit/bin/activate  # On Windows: venv_streamlit\Scripts\activate
    ```

    **Install Dependencies for Streamlit App:**
    ```bash
    pip install --upgrade pip
    pip install -r requirements.txt
    ```

    **Create and Activate Virtual Environment for Rasa Server:**
    Open a new terminal window for the Rasa server.
    ```bash
    python3 -m venv venv_rasa
    source venv_rasa/bin/activate  # On Windows: venv_rasa\Scripts\activate
    ```

    **Install Dependencies for Rasa Server:**
    ```bash
    pip install rasa==3.6.2
    ```

    **Create and Activate Virtual Environment for Rasa Action Server:**
    Open another terminal window for the Rasa action server.
    ```bash
    python3 -m venv venv_rasa_actions
    source venv_rasa_actions/bin/activate  # On Windows: venv_rasa_actions\Scripts\activate
    ```

    **Install Dependencies for Rasa Action Server:**
    ```bash
    pip install rasa-sdk==3.6.2
    pip install -r actions/requirements-actions.txt
    ```
-->

2. **Build and Start Services:**
    ```bash
    docker-compose up --build
    ```

3. **Access the Streamlit Application:**
    Open your browser and navigate to [http://localhost:8501](http://localhost:8501) to access the interactive web interface.

> ### **IMPORTANT NOTE** :information_source:
>
> If you are using the chatbot feature for the first time, **please ensure that the Rasa model has been properly trained**. Training the model is crucial for the chatbot to function correctly. To train the Rasa model, please follow the instructions in the [Training the Rasa Chatbot](#training-the-rasa-chatbot) section below. Failing to train the Rasa model may result in unexpected behavior or errors when interacting with the chatbot.

## Data

### Dataset

We utilize the [Stroke Prediction Dataset](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset) from Kaggle for training and evaluation.

### Data Handling

- **Outlier Detection:** Implemented using the Z-score method to identify and handle anomalies.
- **Data Augmentation:** Added 30% realistic synthetic data to enhance dataset robustness.
- **Data Transformation:** Normalized numerical features following best practices outlined in [Google's Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course/numerical-data).

## Basic Usage

### Running the Application with Docker

1. **Ensure Docker Engine is Installed:**
    Make sure Docker is installed and running on your system.

2. **Build and Start Services:**
    Navigate to the project root directory and execute:
    ```bash
    docker-compose up --build
    ```
    This command builds the Docker images, trains the Rasa model, and starts all services as defined in `docker-compose.yml`.

3. **Access the Streamlit Application:**
    Open your browser and navigate to [http://localhost:8501](http://localhost:8501) to access the interactive web interface.

### Training the Rasa Chatbot

If a Rasa model has not been trained in the `models/chatbot/` directory, follow these steps:


1. **Access the Rasa Server Container:**
    ```bash
    docker exec -it rasa_server bash
    ```

2. **Train the Rasa Model:**
    Inside the container, execute:
    ```bash
    rasa train
    ```

3. **Restart Services:**
    Exit the container and restart the Docker services:
    ```bash
    exit
    docker-compose up --build
    ```

4. **Monitor Rasa Server Logs:**
    Ensure the Rasa server is running by checking the logs for messages like:
    ```
    2024-11-09 01:15:42 INFO     root  - Rasa server is up and running.
    ```

5. **Finalize Setup:**
    - Navigate to the Data Analysis page in the Streamlit app and wait for the evaluation models to finish training.
    - Once evaluations are complete, models will be available for use within the Chatbot.
    - Ensure that data filters are applied as needed and that session management maintains these filters when switching between Data Analysis and Chatbot sections.

## Demonstration Video

A screencast demonstrating the key functionalities of the **Project Apero**. The demo includes:

- **Application Workflow Without Rasa Model:**
  - Showcases the application's basic functionalities when the Rasa model is not trained, highlighting data analysis and recommendation features.
  
- **Training the Rasa Model:**
  - Demonstrates the steps to train the Rasa model, ensuring the chatbot is operational.
  
- **Data Analysis Workflow:**
  - Walks through the data analysis process, including loading data, preprocessing, outlier detection, and visualization.
  
- **Generating Recommendations:**
  - Illustrates how personalized health recommendations are generated based on user input and model predictions.
  
- **Chatbot Functionalities:**
  - Exhibits interactions with the Rasa chatbot, including handling user queries, providing recommendations, and managing conversations.

[Watch the Demo Video](./docs/.ASP_Demo.mp4)

## Implementation of the Requests

The **Project Apero** encompasses a multi-faceted approach to developing a data-driven web application integrated with a chatbot for personalized health recommendations. Below is an overview of how each project request has been implemented:

1. **Multi-page Web App with Streamlit**:
    - **Home Page**:
        - **File**: `src/app.py`
        - **Function**: `main()`
        - **Description**: Implements the user interface for collecting personal health information through interactive forms using Streamlit's form functionalities.
    - **Data Analysis Page**:
        - **File**: `src/data/data_analysis.py`
        - **Function**: `DataAnalysis.run()`
        - **Description**: Handles data analysis operations, including loading, preprocessing, filtering, visualization, and model training.
    - **Recommendations Page**:
        - **File**: `src/app.py`
        - **Function**: Placeholder within `main()` function (implementation to be completed as needed)
        - **Description**: Intended to display personalized health recommendations based on user input and predictive modeling.
    - **Chatbot Page**:
        - **File**: `src/chatbot/rasa_chatbot.py`
        - **Function**: `Chatbot.run()`
        - **Description**: Integrates the Rasa-based chatbot within the Streamlit application, enabling real-time user interactions and assistance.

2. **Data Handling and Augmentation**:
    - **Data Import**:
        - **File**: `src/data/data_loader.py`
        - **Function**: `load_data(filepath=None)`
        - **Description**: Loads the dataset from a predefined CSV file, ensuring seamless data ingestion into the application.
    - **Outlier Handling**:
        - **File**: `src/data/data_analysis.py`
        - **Function**: `preprocess_data(data)`
        - **Description**: Implements statistical methods to identify and manage outliers, enhancing data integrity and reliability.
    - **Fake Data Generation**:
        - **File**: `src/data/data_augmentation.py`
        - **Function**: `augment_data(X, y, augmentation_factor=0.3)`
        - **Description**: Utilizes the Faker library to generate synthetic data, augmenting the original dataset by 25-50% to improve model robustness.

3. **Machine Learning Integration with Scikit-Learn**:
    - **Model Training**:
        - **File**: `src/data/data_analysis.py`
        - **Function**: `DataAnalysis.train_models(status_text, progress_bar)`
        - **Description**: Trains multiple machine learning models, including Logistic Regression, Support Vector Machines, and Random Forest classifiers, on both real and augmented datasets.
    - **Model Evaluation**:
        - **File**: `src/data/data_analysis.py`
        - **Function**: `DataAnalysis.evaluate_model(model, model_name, X_test, y_test, data_type="")`
        - **Description**: Assesses model performance using metrics such as Accuracy, Precision, Recall, F1 Score, and ROC AUC, with results visualized within the application.
    - **Recommendation System**:
        - **File**: `actions/actions.py`
        - **Function**: `ActionGenerateRecommendation.run(dispatcher, tracker, domain)`
        - **Description**: Generates personalized health recommendations based on user-provided data and predictive modeling outputs.

4. **Chatbot Development with Rasa**:
    - **Intent Recognition and Entity Extraction**:
        - **Files**: `domain.yml`, `nlu.yml`
        - **Function**: Defined intents and entities within Rasa's configuration files to enable accurate understanding of user inputs.
    - **Custom Actions**:
        - **File**: `actions/actions.py`
        - **Functions**: `ActionShowDataAnalysis.run()`, `ActionGenerateRecommendation.run()`, `ActionProvideStrokeRiskReductionAdvice.run()`, `ActionFallback.run()`
        - **Description**: Implements custom actions to handle data analysis summaries, generate recommendations, provide stroke risk reduction advice, and manage fallback responses.
    - **Integration with Streamlit**:
        - **File**: `src/chatbot/rasa_chatbot.py`
        - **Function**: `Chatbot.run()`
        - **Description**: Ensures seamless communication between the Streamlit application and the Rasa chatbot through REST APIs.

5. **Documentation and Version Control**:
    - **MyGit Repository and Wiki**:
        - **Files**: All project files are maintained within the Git repository, with detailed documentation in the Wiki.
        - **Description**: Organizes source code, documentation, and model files in a structured manner, facilitating collaboration and version control.
    - **README Structure**:
        - **File**: `README.md`
        - **Description**: Adheres to the specified structure, providing clear instructions, project details, and comprehensive information on setup and usage.

Each component has been meticulously developed to ensure a cohesive and user-friendly application that leverages data analysis and machine learning to deliver meaningful health recommendations.

## Right-fit Question for Chatbot

Integrating a chatbot within the **Project Apero** is a strategic decision grounded in enhancing user engagement and providing real-time assistance. To determine whether conversation design is the right fit for this feature, we conducted a self-assessment based on Google's guidelines.

### Is conversation the right fit?

Review the following statements to determine whether conversation design is the right strategy for your feature. If you're checking off most of them, it's likely that dialog is a good fit.

| Check to see whether each statement is true about your feature | Benefits of Conversation |
| --- | --- |
| - [x] Users already have human-to-human conversations about this task or topic.<br><br> - [x] The interaction is brief, with minimal back-and-forth dialog. | **Conversation is intuitive.** It lets users say what they want to get what they want. |
| - [x] Users would have to tap multiple times to complete the task with a screen.<br><br> - [x] Users might have to navigate multiple apps or widgets to complete the task with a screen.<br><br> - [ ] The feature is difficult or cumbersome to find. | **Conversation saves the user more time and effort than a screen-based UI.** Conversation can be the ultimate shortcut. It reduces friction by quickly getting the user what they want. |
| - [x] Users can do this task while multitasking.<br><br> - [x] Users can do this task when their hands or eyes are busy. | **Conversation lets users multitask.** It helps them when they're busy, especially in situations when their hands or eyes are occupied, or when they're on the move. |
| - [x] Users feel comfortable talking or typing about this topic. | **Conversation lets users speak freely.** Spoken conversations are best in private spaces or familiar shared spaces. Written conversations are best for personal devices. |

---

### Explanation of Checked Statements:

1. **Users already have human-to-human conversations about this task or topic.**
    - Health-related advice and discussions are common in everyday conversations, making conversation a natural fit for delivering personalized recommendations.

2. **The interaction is brief, with minimal back-and-forth dialog.**
    - Users typically seek quick and concise health recommendations, allowing for brief interactions without the need for extensive dialog.

3. **Users would have to tap multiple times to complete the task with a screen.**
    - Without a chatbot, users might navigate through multiple pages or forms to receive recommendations, which can be time-consuming.

4. **Users might have to navigate multiple apps or widgets to complete the task with a screen.**
    - A chatbot centralizes the interaction, reducing the need to switch between different applications or tools.

5. **Users can do this task while multitasking.**
    - Users can interact with the chatbot while performing other tasks, enhancing convenience and accessibility.

6. **Users can do this task when their hands or eyes are busy.**
    - The chatbot supports voice interactions, allowing users to receive recommendations even when their hands or eyes are occupied.

7. **Users feel comfortable talking or typing about this topic.**
    - Users are generally comfortable discussing health-related topics, especially in a private and secure conversational interface.

### Conclusion

Based on the above assessment, incorporating a chatbot aligns perfectly with the project's objectives. It offers an intuitive, efficient, and user-friendly interface for delivering personalized health recommendations, enhancing overall user experience and engagement.


## Work Done

The **Project Apero** was developed collaboratively by two team members, each contributing distinct components to ensure a comprehensive and robust application.

### **Student 1: [Firstname Lastname, Mat-No: 123456]**

1. **Graphical User Interface (GUI) / Visualization**:
    - Developed the Streamlit-based multi-page web application interface.
    - Implemented interactive forms for data collection and dynamic visualizations using Altair.
    - Designed the layout and navigation structure to enhance user experience.

2. **General Data Analysis**:
    - Conducted exploratory data analysis using Pandas to uncover key insights and correlations.
    - Implemented statistical methods for outlier detection and data cleaning.
    - Integrated data visualization tools to present analysis results within the application.

3. **Sample Dialogs**:
    - Created and documented sample interaction scenarios for the Rasa chatbot.
    - Ensured that dialogues effectively cover use cases such as data analysis requests and health recommendations.
    - Collaborated on refining chatbot responses to align with user intents.

### **Student 2: [Firstname Lastname, Mat-No: 654321]**

4. **Strategies for Outliers and Fake Data**:
    - Developed algorithms for identifying and managing outliers within the dataset.
    - Utilized the Faker library to generate realistic synthetic data, augmenting the original dataset by 30%.
    - Documented the approaches and their impact on model training and performance.

5. **Scikit-Learn Integration**:
    - Trained multiple machine learning models including Logistic Regression, Support Vector Machines, and Random Forest classifiers.
    - Performed model evaluation using metrics such as Accuracy, Precision, Recall, F1 Score, and ROC AUC.
    - Selected the best-performing model based on evaluation results and integrated it into the recommendation system.

6. **Dialog Flow**:
    - Designed and implemented the dialog flow within the Rasa framework to handle various user intents.
    - Configured intents, entities, and actions to support seamless interactions and accurate intent recognition.
    - Ensured that the chatbot effectively manages conversation states and provides relevant responses.

### **Both Members: Documentation and Programming**

- **Documentation**:
    - Maintained comprehensive project documentation within the MyGit Wiki, covering project setup, data handling, model training, and usage instructions.
    - Structured the README.md file according to the specified guidelines, ensuring clarity and completeness.

- **Programming**:
    - Collaborated on integrating different components of the application, including the web interface, data analysis modules, machine learning models, and chatbot functionalities.
    - Ensured code quality through consistent coding standards, thorough testing, and effective version control using Git.

This collaborative effort resulted in a well-rounded and functional application that meets the project’s objectives and provides valuable health recommendations through an intuitive user interface and intelligent chatbot assistance.

## Features

- **Interactive Web Interface:** Built with Streamlit, offering a seamless and responsive user experience.
- **Personalized Recommendations:** Utilizes Scikit-Learn algorithms to provide tailored suggestions.
- **Data Analysis & Visualization:** Employs Pandas and Matplotlib for insightful data analysis and visualization.
- **Chatbot Support:** Integrates a Rasa-powered chatbot to assist users and enhance interaction.
- **Robust Data Handling:** Implements strategies for outlier detection and augmentation with realistic fake data.

## Chatbot Integration

### Overview

The chatbot is built using the Rasa framework and is designed to interact contextually with the data analysis results presented on the Streamlit app. It can assist users in navigating the application, provide recommendations, and answer queries related to the data insights.

### Features

- **Context-Aware Conversations:** Understands the context from user interactions and provides relevant responses.
- **Data-Driven Responses:** Fetches and presents data analysis results upon user requests.
- **Seamless Integration:** Embedded within the Streamlit app for a unified user experience.

### Configuration

- **Rasa Server:** Runs on port `5005`.
- **Rasa Action Server:** Runs on port `5055`.
- **Streamlit App:** Communicates with the Rasa server via the Docker network.

### Custom Actions

Custom actions are implemented in `actions/actions.py` to enable the chatbot to fetch and present data analysis results. These actions interact with the Streamlit app's data processing modules to retrieve relevant insights based on user queries.

## Modeling

### Algorithms

- **Random Forest Classifier:** Chosen for its robustness and ability to handle feature interactions.
- **Support Vector Machine (SVM):** Utilized for its effectiveness in high-dimensional spaces.

### Model Training

Models are trained using Scikit-Learn, with performance evaluated based on accuracy, precision, recall, and F1-score. The best-performing model is integrated into the Streamlit app for generating personalized recommendations.

## Docker Setup

The project is containerized using Docker and orchestrated with Docker Compose to ensure consistent environments across development and production.

### Services

- **Rasa Server (`rasa_server`):** Handles natural language understanding (NLU) and dialogue management.
- **Rasa Action Server (`rasa_action_server`):** Executes custom actions defined in the project.
- **Streamlit App (`streamlit_app`):** Provides the interactive frontend for users.
- **Duckling (`duckling`):** (Optional) Extracts entities like dates, times, and numbers from user inputs.

### Running the Services

Ensure Docker and Docker Compose are installed, then execute:

```bash
docker-compose up --build
```

### Accessing Services

- **Streamlit App:** [http://localhost:8501](http://localhost:8501)
- **Rasa Server:** [http://localhost:5005](http://localhost:5005)
- **Rasa Action Server:** [http://localhost:5055](http://localhost:5055)
- **Duckling (Optional):** [http://localhost:8000](http://localhost:8000)

## Project Structure

```
assistance-systems-project/
├── actions/
│   ├── actions.py
│   ├── Dockerfile
│   ├── requirements-actions.txt
│   └── __init__.py
├── data/
│   ├── data_analysis.py
│   ├── data_augmentation.py
│   ├── data_loader.py
│   ├── data_preprocessor.py
│   ├── data_visualization.py
│   ├── nlu.yml
│   ├── processed/
│   ├── raw/
│   └── stories.yml
├── models/
│   ├── chatbot/
│   └── data_analysis/
│       └── evaluations/
├── src/
│   ├── app.py
│   ├── chatbot/
│   │   ├── rasa_chatbot.py
│   │   └── __init__.py
│   └── __init__.py
├── .dockerignore
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
└── docs/
    └── Project_Outline.md
```

## License

This project is licensed under the [GNU GENERAL PUBLIC LICENSE](./LICENSE).

## Contact

For any inquiries or support, please open an issue in the [MyGit Repository](https://github.com/THD-AI-2023/AIN-B-3-Assistant-Systems).
