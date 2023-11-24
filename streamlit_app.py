import streamlit as st
from model import predict_sentiment

# Streamlit interface
def main():
    st.title("Sentiment Analysis")
    user_input = st.text_area("Enter Text", "Type here...")
    
    # Design the UI
    if st.button("Predict"):
        with st.spinner('Analyzing...'):
            # Predict the output
            result = predict_sentiment(user_input)
            st.success("Done!")
            st.write("Sentiment:", result["model_output"])
            st.write("Confidence:", result["confidence_score"])

if __name__ == "__main__":
    main()
