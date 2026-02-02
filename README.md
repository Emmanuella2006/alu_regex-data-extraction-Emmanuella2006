Regex Data Extraction Project
Overview 
This project shows an application of regular expressions (regex) in Python to get structured information out of unstructured text. The program will take the input of a text file and find the occurrence of certain kinds of data by using a regular expression and return them in a clean Json format.

The idea is to demonstrate real world usages of regular expressions, defensive input processing and safe data mining.

Features
The program is able to extract the following types of data:

Emails – standard formats with multi-part domains.

URLs – HTTP and HTTPS.

Phone numbers – Rwanda (local formats +250, local formats), and US formats.

Currency values – USD ($) and Rwandan Francs (RWF/FRW) in prefix and suffix.

HTML elements – such as attribute-containing tags.

Hashtags – words or phrases that begin with a hash (#).

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
Regex patterns are designed to reject bad input.

The data extracted is stored safely in JSON and is not executed.

Sensitive data (e.g., emails) is handled minimally to avoid unnecessary exposure.

The program is aware of adversarial input but does not deploy a comprehensive backend security system.

Conclusion
This project brings to light the fact that regex is able to process unstructured data (text) and convert it into structured data. It gives a real world demonstration of pattern recognition, safe processing of input, and concise presentation of output.
