# Email Spam Detection Application

## Overview
This is a simple Streamlit web application that detects whether an email is spam or legitimate using machine learning. The application uses a pre-trained model to classify emails based on their content.

## Features
- User-friendly interface for pasting email content
- Quick classification of emails as spam or legitimate
- Visual indicators for classification results

## Prerequisites
- Python 3.7+
- Streamlit
- scikit-learn
- pickle

## Installation
1. Clone this repository or download the source code
2. Install the required dependencies:
   ```
   pip install streamlit scikit-learn
   ```
3. Ensure you have the following files in your project directory:
   - `app.py` (the main application code)
   - `spam_detection.pickle` (pre-trained classification model)
   - `tfidf_vectorizer.pickle` (pre-trained TF-IDF vectorizer)

## Usage
1. Run the application:
   ```
   streamlit run app.py
   ```
2. Open the provided URL in your web browser
3. Paste the email content in the text area
4. Click the "Predict" button to classify the email

## How It Works
1. The application loads a pre-trained machine learning model and TF-IDF vectorizer
2. When a user submits email content, the text is transformed using the TF-IDF vectorizer
3. The transformed text is passed to the model for prediction
4. The application displays whether the email is spam or legitimate based on the model's prediction

## Model Details
- The model was pre-trained using scikit-learn
- TF-IDF (Term Frequency-Inverse Document Frequency) is used for feature extraction from the text
- The model classifies emails as class 1 (spam) or class 0 (legitimate)

## Files
- `app.py`: Main Streamlit application code
- `spam_detection.pickle`: Pre-trained classification model
- `tfidf_vectorizer.pickle`: Pre-trained TF-IDF vectorizer

## Future Improvements
- Add confidence scores for predictions
- Include a sample dataset for testing
- Allow users to upload email files directly
- Add model retraining capabilities with user feedback
- Implement additional preprocessing steps for better accuracy
