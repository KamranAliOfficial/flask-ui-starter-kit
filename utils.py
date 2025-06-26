# utils.py
import datetime

def get_welcome_message():
    now = datetime.datetime.now()
    if 5 <= now.hour < 12:
        return "Good morning! Welcome to our site."
    elif 12 <= now.hour < 17:
        return "Good afternoon! Great to see you here."
    elif 17 <= now.hour < 21:
        return "Good evening! Hope you’re having a nice day."
    else:
        return "Hello! Welcome to our platform."

def process_contact_form(name, email, message):
    # Simulate saving or emailing (data is saved to SQLite in the main app)
    print(f"Contact Form Submitted:\nName: {name}\nEmail: {email}\nMessage: {message}")
    return True