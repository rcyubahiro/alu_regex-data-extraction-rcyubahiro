from extractors import *

sample_text = """
My email is user@example.com and my backup is firstname.lastname@company.co.uk.
Visit https://www.example.com or https://subdomain.example.org/page.
Call me at (123) 456-7890 or 123.456.7890.
My card number is 1234-5678-9012-3456.
The meeting is at 14:30 or 2:30 PM.
"""

print("Emails:", extract_emails(sample_text))
print("URLs:", extract_urls(sample_text))
print("Phone Numbers:", extract_phone_numbers(sample_text))
print("Credit Cards:", extract_credit_cards(sample_text))
print("Time Formats:", extract_time_formats(sample_text))
