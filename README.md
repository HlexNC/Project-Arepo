[![Project Apero Banner](./docs/img/ASP_Banner.png)](https://github.com/HlexNC/Project-Arepo)

# Project Apero - Stroke Prediction Web App

## Project Description

Project Apero is a comprehensive web application designed to help individuals assess their risk of stroke and receive personalized recommendations. The system integrates data analysis, machine learning, and a conversational chatbot interface to provide actionable health insights.

## Overview

- **Purpose:** Provide users with personalized health risk assessments and actionable recommendations to reduce stroke risk.
- **Key Features:**
  - Personalized Stroke Risk Assessment using machine learning.
  - Interactive Data Analysis and Visualization.
  - Chatbot Assistance for real-time health advice.
- **Technologies:** Python, Streamlit, Rasa, Scikit-Learn, Docker.

## Installation

### Prerequisites

- Docker
- Git
- Python 3.9+

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/HlexNC/Project-Arepo.git
   cd Project-Apero
   ```
2. **Build and run Docker services:**
   ```bash
   docker-compose up --build
   ```
3. **Access the application:**
   Open your web browser and navigate to [http://localhost:8501](http://localhost:8501).

## Data

The application uses a publicly available stroke prediction dataset.

- **Dataset Source:** [Kaggle - Stroke Prediction Dataset](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset)
- **Data Handling:** The dataset is preprocessed using outlier detection and synthetic data augmentation to improve model robustness.

## Usage

- **Personalized Recommendations:** Input your personal health data to receive an estimated stroke probability and risk level.
- **Data Analysis:** Explore interactive visualizations and key insights from the data.
- **Chatbot Assistance:** Engage with our Rasa-powered chatbot for quick, real-time health advice.

## Documentation

For detailed documentation, please refer to the project Wiki.

## License

This project is licensed under the GNU General Public License v3. See the [LICENSE](LICENSE) file for details.

## Contact

For inquiries or support, please open an issue in the repository.
