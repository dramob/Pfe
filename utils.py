

def validate_feedback(feedback: str) -> bool:
    """
    Validate the feedback input.

    :param feedback: Feedback text to validate.
    :return: Boolean indicating if the feedback is valid.
    """
    return bool(feedback.strip())