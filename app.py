import streamlit as st
from llm import CoachingAdvisorLLM
from utils import save_feedback, load_feedback
import os

# Load API key
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("API key is not set. Please set the OPENAI_API_KEY environment variable.")
    st.stop()

# Initialize the advisor
advisor = CoachingAdvisorLLM(api_key)

# Streamlit App
def main():
    profile = st.sidebar.selectbox("Select Profile", ["User", "Admin"])

    if profile == "User":
        st.title("User Feedback Form")
        st.write("Please fill out this quick questionnaire.")

        # Feedback form
        name = st.text_input("Name:")
        feedback = st.text_area("Provide your coaching feedback:")
        satisfaction = st.slider("Rate your satisfaction (1-10):", 1, 10, 5)
        submit_button = st.button("Submit Feedback")

        if submit_button:
            if name and feedback:
                save_feedback(name, feedback, satisfaction)
                st.success("Thank you for your feedback!")
            else:
                st.warning("Please complete all fields before submitting.")

    elif profile == "Admin":
        st.title("Admin Dashboard")
        st.write("View feedback and get AI recommendations.")

        # Load Feedback
        feedback_data = load_feedback()
        st.dataframe(feedback_data)

        # Generate Recommendations
        if not feedback_data.empty:
            st.header("Generate AI Recommendations")
            if st.button("Get Recommendations"):
                recommendations = advisor.get_recommendations(feedback_data)
                st.success("AI Recommendations:")
                st.write(recommendations)
        else:
            st.warning("No feedback available yet.")
if __name__ == "__main__":
    main()