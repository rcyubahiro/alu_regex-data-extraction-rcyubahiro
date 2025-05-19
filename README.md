🧪 alu_regex-data-extraction-rcyubahiro
🔍 Overview
This project is a data extraction tool built using Python and Regular Expressions (regex). It scans through large text inputs and extracts specific types of data such as:

Email addresses

URLs

Phone numbers

Credit card numbers

Time (12-hour and 24-hour formats)

The goal is to simulate a real-world data parsing task as part of a Junior Full Stack Developer internship project.

  Tech Stack
Language: Python 3

Libraries: Built-in re module (for regex)

  File Structure
bash
Copy
Edit
alu regex-data-extraction-rcyubahiro/
├── extractors.py          # Contains all regex functions
├── test extractors.py     # Script to test and demonstrate the extractors
├── README.md              # Project documentation (this file)
  Features
Data Type	Supported Examples
Emails	user@example.com, firstname.lastname@company.co.uk
URLs	https://www.example.com, https://sub.example.org
Phone Numbers	(123) 456-7890, 123-456-7890, 123.456.7890
Credit Cards	1234 5678 9012 3456, 1234-5678-9012-3456
Time Formats	14:30, 2:30 PM

   How to Run
Make sure you have Python 3 installed.

Clone the repository:

bash
Copy
Edit
git clone https://github.com/rcyubahiro/alu regex-data-extraction-rcyubahiro.git
cd alu regex-data-extraction-rcyubahiro
Run the test script:

bash
Copy
Edit
python3 test extractors.py
This will output the extracted data from a sample string.

  Sample Output
text
Copy
Edit
Emails: ['user@example.com', 'firstname.lastname@company.co.uk']
URLs: ['https://www.example.com', 'https://subdomain.example.org/page']
Phone Numbers: ['(123) 456-7890', '123.456.7890']
Credit Cards: ['1234-5678-9012-3456']
Time Formats: ['14:30', '2:30 PM']
   Edge Case Handling
The script handles variations in format, such as:

Email with dots and subdomains

Phone numbers with dashes, dots, or parentheses

Mixed-format times (AM/PM and 24-hour)

License
This project is for educational use under the ALU regex extraction assignment. Feel free to reuse with attribution.

 Author
Robert CYUBAHIRO
GitHub Profile:rcyubahiro


