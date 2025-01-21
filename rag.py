def get_rag_recommendations(feedback_data, advisor):
    """
    Generate recommendations using RAG on feedback data.

    :param feedback_data: DataFrame containing feedback.
    :param advisor: Instance of CoachingAdvisorLLM.
    :return: AI recommendations.
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

        # Pass combined feedback to the advisor for recommendations
        recommendations = advisor.generate_advice(combined_feedback)
        return recommendations

    except Exception as e:
        return f"Error while generating RAG recommendations: {str(e)}"