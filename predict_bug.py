import re
import pickle

# Load saved model
model = pickle.load(open("bug_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

def clean_text(text):
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    text = text.lower()
    return text

def predict_severity(text):
    cleaned = clean_text(text)
    vector = vectorizer.transform([cleaned])
    prediction = model.predict(vector)
    probability = model.predict_proba(vector)
    confidence = max(probability[0]) * 100
    return prediction[0], round(confidence, 2)

print("🤖 AI Bug Severity Predictor Ready!")
print("-------------------------------------")

while True:
    user_input = input("Enter Bug Description (type 'exit' to quit): ")

    if user_input.lower() == "exit":
        print("Program Closed.")
        break

    severity, confidence = predict_severity(user_input)

    print(f"🔎 Predicted Severity: {severity}")
    print(f"📊 Confidence: {confidence}%")
    print("-------------------------------------")
