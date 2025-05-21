import re

# Load sample text from file
with open("test_input.txt", "r") as file:
    sample_text = file.read()

patterns = {
    "Emails": r'\b[\w\.-]+@[\w\.-]+\.\w{2,}\b',
    "URLs": r'https?://[^\s,<>"]+',
    "Phone Numbers": r'\(?\d{3}\)?[-.\s]\d{3}[-.\s]\d{4}',
    "Credit Cards": r'\b\d{4}[-\s]\d{4}[-\s]\d{4}[-\s]\d{4}\b',
    "Time (24h)": r'\b([01]?[0-9]|2[0-3]):[0-5][0-9]\b',
    "Time (12h)": r'\b(1[0-2]|0?[1-9]):[0-5][0-9]\s?(AM|PM|am|pm)\b',
    "HTML Tags": r'<[^>]+>',
    "Hashtags": r'#\w+',
    "Currency Amounts": r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?'
}

for key, pattern in patterns.items():
    matches = re.findall(pattern, sample_text)
    flat_matches = [' '.join(m) if isinstance(m, tuple) else m for m in matches]
    print(f"{key}: {flat_matches}")
