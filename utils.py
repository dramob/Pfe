import pandas as pd
import os

FEEDBACK_FILE = "feedback_data.csv"

def save_feedback(name, feedback, satisfaction):
    """
    Save user feedback to a CSV file.

    :param name: User's name
    :param feedback: Feedback provided by the user
    :param satisfaction: Satisfaction rating (1-10)
    """
    # Check if the file exists; if not, create it with headers
    if not os.path.exists(FEEDBACK_FILE):
        df = pd.DataFrame(columns=["Name", "Feedback", "Satisfaction"])
        df.to_csv(FEEDBACK_FILE, index=False)

    # Load existing data
    df = pd.read_csv(FEEDBACK_FILE)

    # Create a new DataFrame with the new entry
    new_entry = pd.DataFrame([{"Name": name, "Feedback": feedback, "Satisfaction": satisfaction}])

    # Concatenate the new entry with the existing data
    df = pd.concat([df, new_entry], ignore_index=True)

    # Save the updated DataFrame back to the CSV
    df.to_csv(FEEDBACK_FILE, index=False)

def load_feedback():
    """
    Load feedback from the CSV file.

    :return: DataFrame containing feedback
    """
    if os.path.exists(FEEDBACK_FILE) and os.stat(FEEDBACK_FILE).st_size > 0:
        return pd.read_csv(FEEDBACK_FILE)
    else:
        # Return an empty DataFrame with headers if the file is empty
        return pd.DataFrame(columns=["Name", "Feedback", "Satisfaction"])