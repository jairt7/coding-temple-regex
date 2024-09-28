import re
def method_1():
    text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
    emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)
    for email in emails:
        if "@exclude.com" in email:
            emails.remove(email)
    print(emails)

def method_2():
    text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
    emails = re.findall(r"\b[A-Za-z0-9._%+-]+@domain\.[A-Z|a-z]{2,}\b", text)
    print(emails)

method_1()
method_2()