Regex Data Extraction Project

Overview
This project demonstrates the use of regular expressions (regex) in Python to extract structured information from unstructured text. The program reads input from a text file, identifies specific data types using regex patterns, and outputs the results in a clean JSON format.

The goal is to showcase practical regex usage, defensive input handling, and secure data extraction.

Features
The program can identify and extract the following data types:

Emails – standard formats including multi‑part domains.

URLs – both HTTP and HTTPS links.

Phone numbers – Rwanda (+250, local formats) and US formats.

Currency values – USD ($) and Rwandan Francs (RWF/FRW), both prefix and suffix styles.

HTML tags – including tags with attributes.

Hashtags – words or phrases prefixed with #.

How It Works:
Input: Place text into input.txt.
Example:

Contact me at emmanuellagacuti@gmail.com
Visit https://www.agriculture-burundi.org
Call +250 788123456 or (123) 456-7890
Budget: $1,234.56 and RWF 2,500,000
<div>Welcome!</div>
#UbuntuLeadership

Execution: Run the program:

bash
python main.py
Output: Extracted data is saved into output.json.
Example:

json
{
    "emails": ["emmanuellagacuti@gmail.com"],
    "urls": ["https://www.agriculture-burundi.org"],
    "phones": ["+250 788123456", "(123) 456-7890"],
    "currency": ["$1,234.56", "RWF 2,500,000"],
    "html_tags": ["<div>", "</div>"],
    "hashtags": ["#UbuntuLeadership"]
}

Security Considerations
Regex patterns are designed to reject malformed input.

Extracted data is stored safely in JSON and not executed.

Sensitive data (e.g., emails) is handled minimally to avoid unnecessary exposure.

The program demonstrates awareness of adversarial input without implementing a full backend security system.

Conclusion
This project highlights how regex can transform unstructured text into structured data. It provides a practical example of pattern recognition, secure handling of input, and clear output formatting.
