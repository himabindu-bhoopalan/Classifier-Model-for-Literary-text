import streamlit as st
import joblib

# Load model and vectorizer
@st.cache_resource
def load_model():
    with open('models/svm_model.pkl', 'rb') as f:
        model = joblib.load(f)
    with open('data.pkl', 'rb') as f:
        data = joblib.load(f)
    return model, data

model, data = load_model()
vectorizer = data.get('vectorizer', None)  # Assuming TF-IDF vectorizer is stored here

# Hardcoded novel names mapped to class indices 0–10
class_names = data.get('class_names')

if class_names is None or vectorizer is None:
    st.error("❌ 'class_names' or 'vectoriser' not found in data.pkl.")
else:
    st.title("📚 Novel Query Classifier")
    st.write("Ask your question pertaining to any these novels: {} and the model will predict which classic novel it belongs to.".format(' ,'.join(class_names)))

    # Text input with Enter detection
    user_input = st.text_area("Enter Question here", height=200, on_change=None)
    
    if user_input and (st.button("Classify") or st.session_state.get('last_input') != user_input):
        st.session_state.last_input = user_input
        if not vectorizer:
            st.error("❌ Vectorizer not found in data.pickle.")
        else:
            # Preprocess and predict
            input_vector = vectorizer.transform([user_input])
            prediction = model.predict(input_vector)
            
            try:
                predicted_class = class_names[prediction[0]]
            except IndexError:
                predicted_class = f"Unknown class index: {prediction[0]}"
            
            st.success(f"✅ Predicted Novel: **{predicted_class}**")
