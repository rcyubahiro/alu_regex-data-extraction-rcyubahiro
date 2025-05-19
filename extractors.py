import re
import string

def clean_results(results):
    return [r.rstrip(string.punctuation) for r in results]

def extract_emails(text):
    return clean_results(re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', text))

def extract_urls(text):
    return clean_results(re.findall(r'https?://(?:www\.)?[\w.-]+\.\w+(?:/\S*)?', text))

def extract_phone_numbers(text):
    return re.findall(r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}', text)

def extract_credit_cards(text):
    return re.findall(r'\b(?:\d{4}[- ]?){3}\d{4}\b', text)

def extract_time_formats(text):
    return re.findall(r'\b(?:1[0-2]|0?[1-9]):[0-5][0-9] ?[AaPp][Mm]|\b(?:[01]?[0-9]|2[0-3]):[0-5][0-9]\b', text)
