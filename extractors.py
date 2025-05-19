import re

def extract_emails(text):
    return re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', text)

def extract_urls(text):
    return re.findall(r'(https?://(?:www\.)?[\w\.-]+\.\w{2,}(?:/[\w\.-]*)*)', text)

def extract_phone_numbers(text):
    # Handles +250788123456 or 0788123456
    return re.findall(r'(\+?\d{3,4}[-\s]?\d{2,3}[-\s]?\d{6})', text)

def extract_credit_cards(text):
    return re.findall(r'\b(?:\d[ -]*?){13,16}\b', text)

def extract_time(text):
    # Matches 14:35, 14:35:29
    return re.findall(r'\b([01]?\d|2[0-3]):[0-5]\d(:[0-5]\d)?\b', text)
