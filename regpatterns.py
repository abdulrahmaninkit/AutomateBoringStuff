import re, pyperclip # to install the modules use pip install pyperclip and pip install regex

# Create a regex for phone numbers
phoneRegex = re.compile(r'''
(
     # Example phone numbers: 415-555-0000, (415) 555-0000, 555-0000, ext 12345, ext. 12345, x 12345
    (\d{3}|\(\d{3}\))?          # Area code (optional, with or without parentheses)
    (\s|-)                      # Separator (optional space or hyphen)
    \d{3}                       # First 3 digits
    -                           # Separator
    \d{4}                       # Last 4 digits
    (((ext(\.)?\s)|x) #extra part word part
        (\d{2,5}))? #extra number part
)
''', re.VERBOSE)

# Create a regex for email addresses
emailRegex = re.compile(r'''
    [a-zA-Z0-9_.+]+              # Name part
    @                            # '@' symbol
    [a-zA-Z0-9_.+]+              # Domain name part
''', re.VERBOSE)

# Get the text (use the example text directly for simplicity)

text = pyperclip.paste()

# Extract the email/phone from text

extractedPhone = phoneRegex.findall(text) #if groups are present findall returns tuple hence for loop is required
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []

for phoneNumbers in extractedPhone:
    allPhoneNumbers.append(phoneNumbers[0])


#copy the extracted result into the clipboard
result = '\n'.join(allPhoneNumbers)+'\n'+'\n'.join(extractedEmail)

pyperclip.copy(result)
print(result)




# Sample text to use.


# Hello everyone,

# Please reach out to us at the following contact points for further information:

# John Doe - Technical Support
# Phone: 800-555-1234
# Email: john.doe@example.com

# Jane Smith - Customer Service
# Phone: (415) 555-5678 ext. 123
# Email: jane.smith@customer.com

# Robert Brown - Sales Department
# Phone: 555-2345
# Email: robert.brown@sales.example.com

# General Inquiries
# Phone: 415-555-6789
# Email: info@example.com

# Marketing Team
# Phone: 212-555-0000 x4567
# Email: marketing@ourcompany.org

# Event Coordination Team
# Phone: (312) 555-9876
# Email: events@ourcompany.org

# Please feel free to contact us at any of the above numbers or emails. We look forward to assisting you.

# Best regards,
# Your Company