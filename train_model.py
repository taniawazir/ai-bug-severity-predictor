import pandas as pd
import re
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Sample training dataset
data = {
    "Bug Description": [
        "Login button not working",
        "Typo in homepage",
        "Application crashes on payment",
        "Dashboard loads slowly",
        "App freezes after login",
        "Broken link in help page",
        "Payment gateway timeout error",
        "Data not saving",
        "System crash while exporting",
        "UI alignment issue"
    ],
    "Severity": [
        "High",
        "Low",
        "Critical",
        "Medium",
        "Critical",
        "Low",
        "Critical",
        "High",
        "Critical",
        "Low"
    ]
}

df = pd.DataFrame(data)

def clean_text(text):
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    text = text.lower()
    return text

df['cleaned'] = df['Bug Description'].apply(clean_text)

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['cleaned'])
y = df['Severity']

model = LogisticRegression()
model.fit(X, y)

# Save model and vectorizer
pickle.dump(model, open("bug_model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("✅ Model Trained and Saved Successfully!")
