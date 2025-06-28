# Novel Query Classifier

A web-based application that classifies text queries into different classic novel categories using machine learning.

## Project description and features

This application allows users to input text queries related to classic novels and predicts which novel the query is most likely about. Key features include:

- Web-based interface built with Streamlit
- Real-time text classification using SVM model
- Support for multiple classic novels
- Enter key detection for seamless user experience
- Error handling for missing model files
- User-friendly interface with clear feedback

The current model classifies queries or document segments into the following books:

Alice’s Adventures in Wonderland
Little Women
Sherlock Holmes
The Adventures of Tom Sawyer
Pride and Prejudice
Anne of Green Gables
Oliver Twist
Frankenstein
The Importance of Being Earnest
Great Expectations
The Great Gatsby

## Setup instructions

1. Install required dependencies:
```bash
pip install streamlit scikit-learn joblib
```

## Running instructions

1. Start the Streamlit application:
```bash
streamlit run streamlit_app.py
```

2. Open your web browser and navigate to the URL shown in the terminal (typically http://localhost:8501)

## Usage guide

1. Enter your question about classic novels in the text area
2. Either click the "Classify" button or press Enter to get the prediction
3. The application will display which classic novel your query is most likely related to
4. If any errors occur, they will be clearly displayed in the interface

## Project structure

- `streamlit_app.py` - Main application file containing the Streamlit interface
- `models/svm_model.pkl` - Trained SVM model for classification
- `data.pkl` - Contains TF-IDF vectorizer and class names mapping

## Error handling information

The application includes comprehensive error handling for:
- Missing model files
- Missing vectorizer
- Invalid class predictions
- Data loading errors
