import streamlit as st
from llm import CoachingAdvisorLLM
from utils import  validate_feedback
import os 
# Load API key

api_key = os.getenv("OPENAI_API_KEY")

advisor = CoachingAdvisorLLM(api_key)

# Streamlit App
def main():
    # Title and Description
    st.title("Coaching Feedback Assistant")
    st.write("""
        Provide detailed feedback from your coaching sessions, and this app will generate actionable advice 
        using GPT-4 to improve your coaching skills.
    """)

    # Input Section
    st.header("Enter Coaching Feedback")
    feedback = st.text_area("Provide detailed coaching feedback here:")
    submit_button = st.button("Generate Advice")

    # Action on Submit
    if submit_button:
        if validate_feedback(feedback):
            with st.spinner("Analyzing feedback and generating advice..."):
                advice = advisor.generate_advice(feedback)
                if "Error:" not in advice:
                    st.success("Generated Advice:")
                    st.write(advice)
                else:
                    st.error(advice)
        else:
            st.warning("Please enter valid feedback before submitting.")

# Run the Streamlit App
if __name__ == "__main__":
    main()
