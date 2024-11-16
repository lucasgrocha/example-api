import requests
import inquirer

# FastAPI server URL
BASE_URL = 'http://127.0.0.1:8000'

# Fetch all emails from the FastAPI endpoint
def fetch_emails():
    try:
        response = requests.get(f"{BASE_URL}/emails")
        response.raise_for_status()
        return response.json()['emails']
    except requests.exceptions.RequestException as e:
        print(f"Error fetching emails: {e}")
        return []

# Interactively select an email using inquirer
def select_email(emails):
    if emails:
        questions = [
            inquirer.List('email',
                          message="Select an email:",
                          choices=emails,
            ),
        ]
        answers = inquirer.prompt(questions)
        return answers.get('email')
    else:
        print("No emails available to select.")
        return None

# Fetch person's data by email
def fetch_person_by_email(email):
    try:
        response = requests.get(f"{BASE_URL}/people", json={"email": email})
        response.raise_for_status()
        return response.json()  # Person's full data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching person data: {e}")
        return None

# Main logic
if __name__ == "__main__":
    emails = fetch_emails()  # Get the list of emails
    selected_email = select_email(emails)  # Select an email interactively

    if selected_email:
        person_data = fetch_person_by_email(selected_email)  # Get person's data by email

        if person_data:
            print("\nPerson's Details:")
            for key, value in person_data.items():
                print(f"{key.capitalize()}: {value}")
        else:
            print("No data found for this email.")
