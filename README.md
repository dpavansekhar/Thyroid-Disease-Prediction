# Thyroid Disease Prediction

## Overview

The Thyroid Disease Prediction project is designed to predict the presence of thyroid diseases using machine learning models. The project leverages various classification algorithms to analyze and classify patient data based on features such as age, gender, smoking history, and thyroid function tests.

## Table of Contents

1. [Project Description](#project-description)
2. [Data Description](#data-description)
3. [Modeling](#modeling)
4. [Results](#results)
5. [Web Interface](#Web-Interface) 
6. [Usage](#usage)

## Project Description

This project involves the development and evaluation of machine learning models to predict thyroid disease status. The dataset contains various features related to patient health and lifestyle, which are used to train and test different classification algorithms.

## Data Description

The dataset includes the following columns:

- **Age**: Patient's age.
- **Gender**: Patient's gender (e.g., Male, Female).
- **Smoking**: Smoking status (e.g., Yes, No).
- **Hx Smoking**: History of smoking.
- **Hx Radiotherapy**: History of radiotherapy.
- **Thyroid Function**: Thyroid function test results.
- **Physical Examination**: Results from physical examination.
- **Adenopathy**: Presence of adenopathy.
- **Pathology**: Pathology results.
- **Focality**: Tumor focality.
- **Risk**: Risk assessment.
- **T, N, M**: Tumor stages (T - Tumor size, N - Lymph nodes, M - Metastasis).
- **Stage**: Overall cancer stage.
- **Response**: Treatment response.
- **Recurred**: Recurrence of disease (target variable).

## Modeling

The following machine learning models were developed and evaluated:

- **Logistic Regression**
- **Random Forest Classifier**
- **Support Vector Machine (SVM)**
- **Gradient Boosting**

Each model was trained on the dataset, and its performance was assessed using metrics such as accuracy, precision, recall, and F1-score.

## Results

The performance metrics for each model are summarized as follows:

- **Logistic Regression**
  - Accuracy: 95.65%
  - Precision: 96.00%
  - Recall: 94.12%
  - F1-Score: 95.06%

- **Random Forest Classifier**
  - Accuracy: 98.26%
  - Precision: 99.00%
  - Recall: 96.88%
  - F1-Score: 97.91%

- **Support Vector Machine (SVM)**
  - Accuracy: 96.52%
  - Precision: 96.23%
  - Recall: 93.75%
  - F1-Score: 94.97%

- **Gradient Boosting**
  - Accuracy: 95.65%
  - Precision: 98.00%
  - Recall: 89.58%
  - F1-Score: 93.25%

## Web Interface

I have developed an simple web interface using the python streamlit library for all the 4 models which I  have trained.

### Explanation about Streamlit library

## Streamlit Integration

Streamlit is an open-source framework designed for creating and sharing interactive web applications for machine learning and data science. It allows you to build user interfaces for your machine learning models with minimal effort, making it easier to visualize and interact with your data and models.

### Key Features

- **Ease of Use**: Streamlit is designed to be simple and intuitive. It allows you to create web applications with just a few lines of code, making it accessible even for those with minimal web development experience.
  
- **Real-Time Updates**: Changes made to the code are immediately reflected in the web application, providing real-time feedback and interactions.

- **Interactive Widgets**: Streamlit provides a range of interactive widgets, such as sliders, text inputs, and buttons, that can be easily integrated into your applications to gather user input and display results.

- **Integration with Python**: Streamlit works seamlessly with Python, allowing you to leverage your existing Python code and libraries for data processing, machine learning, and visualization.


## Usage

To use the provided models, follow these steps:

1. Use the trained models to make predictions on new data.

2. In this project, Streamlit is used to create a simple web interface for predicting thyroid disease based on user input. The web app allows users to input various features related to thyroid disease and view the prediction results from the trained machine learning models.

To run the Streamlit app, follow these steps:

1. **Ensure Streamlit is Installed**:
   If you haven't already installed Streamlit, you can do so using pip:

   ```bash
   pip install streamlit

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/dpavansekhar/thyroid-disease-prediction.git


## Sample Snapshot of Web Interface
![image](https://github.com/user-attachments/assets/ade76b72-3d40-4c46-865b-c9779d261590)

