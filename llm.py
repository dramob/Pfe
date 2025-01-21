from langchain_openai.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import HumanMessage, SystemMessage
import pandas as pd

class CoachingAdvisorLLM:
    def __init__(self, api_key: str, model_name: str = "gpt-4", temperature: float = 0.7):
        """
        Initialize the LLM instance with OpenAI API credentials.

        :param api_key: OpenAI API key for authentication.
        :param model_name: The model name to use (default is "gpt-4").
        :param temperature: Controls randomness in output.
        """
        if not api_key:
            raise ValueError("API key is not set. Please set the OPENAI_API_KEY environment variable.")

        self.chat = ChatOpenAI(
            openai_api_key=api_key, 
            model=model_name, 
            temperature=temperature
        )

    def generate_advice(self, feedback: str) -> str:
        """
        Generate actionable coaching advice from feedback using GPT-4.

        :param feedback: Feedback text input by the coach.
        :return: Advice generated by GPT-4.
        """
        # Define a context-specific system message
        prompt_template = ChatPromptTemplate.from_messages([
            SystemMessage(content=(
                "You are a professional coaching advisor specializing in boxing training. "
                "Analyze the following feedback provided by students about their boxing coach. "
                "The feedback is structured as a list. For each point of feedback, identify specific "
                "areas for improvement and provide actionable recommendations tailored to the concerns."
            )),
            HumanMessage(content="Here is the feedback:\n{feedback}")
        ])

        try:
            # Format the messages using the provided feedback
            formatted_messages = prompt_template.format_messages(feedback=feedback)

            # Get the response from the model
            response = self.chat(formatted_messages)
            return response.content.strip()  # Return clean output
        except Exception as e:
            return f"Error while generating advice: {str(e)}"

    def get_recommendations(self, feedback_data: pd.DataFrame) -> str:
        """
        Generate recommendations from the provided feedback DataFrame.

        :param feedback_data: DataFrame containing student feedback.
        :return: AI-generated recommendations.
        """
        try:
            # Combine feedback into a structured format
            combined_feedback = "\n".join(
                f"- {row['Name']}: {row['Feedback']} (Satisfaction: {row['Satisfaction']})"
                for _, row in feedback_data.iterrows()
            )

            # If no feedback is available, return a warning
            if not combined_feedback.strip():
                return "No feedback available to generate recommendations."

            # Debug: Print the combined feedback to ensure it's passed correctly
            print("Combined Feedback Sent to AI:")
            print(combined_feedback)

            # Generate advice using combined feedback
            return self.generate_advice(combined_feedback)
        except Exception as e:
            return f"Error while generating RAG recommendations: {str(e)}"