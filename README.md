README.md
markdown
Copy
Edit
# Regex Data Extraction

This project extracts specific patterns from text using **regular expressions (regex)** in Python. It handles email addresses, phone numbers, URLs, credit card numbers, and time formats.

## Project Structure

├── extractors.py # Core regex extraction functions
├── test extractors.py # Unit tests using unittest module
├── README.md # This file
└── pycache/ # Compiled Python cache

bash
Copy
Edit

##  Supported Patterns

| Pattern Type     | Description                                 |
|------------------|---------------------------------------------|
| Emails           | Extracts standard and some obfuscated emails |
| Phone Numbers    | Local + international formats (e.g. +250...) |
| URLs             | Extracts http/https and www links            |
| Credit Cards     | Basic pattern for 16-digit credit card numbers |
| Time Formats     | Recognizes HH:MM and HH:MM:SS formats        |

##  How to Run

1. **Clone the repo**
   ```bash
   git clone https://github.com/rcyubahiro/alu_regex-data-extraction-rcyubahiro.git
   cd alu_regex-data-extraction-rcyubahiro
Run the test cases

bash
Copy
Edit
python3 test_extractors.py
  Sample Usage
python
Copy
Edit
from extractors import extract_emails, extract_urls

text = "Contact me at test.email+01@gmail.com or visit https://example.com"
print(extract_emails(text))  # Output: ['test.email+01@gmail.com']
print(extract_urls(text))    # Output: ['https://example.com']
  Output Preview
bash
Copy
Edit
.
----------------------------------------------------------------------
Ran 5 tests in 0.002s

OK
   Requirements
Python 3.8+

No external dependencies (uses only Python's built-in re and unittest)

Author
Robert CYUBAHIRO
Mastercard Foundation Scholar at ALU
Project for Regex Challenge at ALU
