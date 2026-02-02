import re
import json

# Read the text input from a file
with open("input.txt", "r") as f:
    text = f.read()
    
# Define regex patterns for extraction
email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.([A-Za-z]{2,})+"

url_pattern = r"https?://[^\s]+"

phone_pattern = (r"(?:\+250\s?\d{9}"
                r"|0\d{9}"
                r"|\(?\d{3}\)?[-.\s]\d{3}[-.\s]\d{4})")

currency_pattern = (r"(\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?"
                   r"|(?:RWF|FRW)\s?\d{1,3}(?:,\d{3})*"
                   r"|\d{1,3}(?:,\d{3})*\s?(RWF|FRW))")
                   

html_tags_pattern = r"<[^>]+>"

hashtags_pattern = r"#\w+"

# Use regex to find all matches in the text
emails = re.findall(email_pattern, text)
urls = re.findall(url_pattern, text)
phones = re.findall(phone_pattern, text)
currency = re.findall(currency_pattern, text)
html_tags = re.findall(html_tags_pattern, text)
hashtags = re.findall(hashtags_pattern, text)

# Organize extracted data into a dictionary
output = {
    "emails": emails,
    "urls": urls,
    "phones": phones,
    "currency": currency,
    "html_tags": html_tags,
    "hashtags": hashtags 
}

# Save results into a JSON file
with open("output.json", "w") as f:
    json.dump(output, f, indent=4)

print("Praise God, extraction completed successfully! See output.json")

