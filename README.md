# AI Bug Severity Predictor

An AI-based machine learning project that predicts the severity of software bugs from bug descriptions.  
The system analyzes textual bug reports and classifies them into severity levels such as Low, Medium, High, and Critical.

## Features

- Predicts bug severity from bug descriptions
- Uses NLP techniques for text preprocessing
- Machine learning model using Logistic Regression
- Provides prediction confidence score
- Simple command line interface

## Technologies Used

- Python
- Pandas
- Scikit-learn
- Regular Expressions (re)
- Pickle

## Project Structure

ai-bug-severity-predictor
│
├── train_model.py
├── predict_bug.py
├── bug_model.pkl
├── vectorizer.pkl
├── requirements.txt
└── README.md

## Installation

Clone the repository

git clone https://github.com/your-username/ai-bug-severity-predictor.git

Go to project directory

cd ai-bug-severity-predictor

Install dependencies

pip install -r requirements.txt

## Run the Project

Train the model

python train_model.py

Run the prediction script

python predict_bug.py

## Example Input

Enter Bug Description: Login button not working

## Example Output

Predicted Severity: High  
Confidence: 85%

## How It Works

1. Bug descriptions are cleaned using text preprocessing.
2. TF-IDF converts text into numerical vectors.
3. Logistic Regression model is trained on the dataset.
4. The trained model predicts severity for new bug descriptions.

## Author

Tania Wazir  
BSCS Student | AI & Software Development Enthusiast
