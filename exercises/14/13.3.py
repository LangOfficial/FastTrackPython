# 13-3. No Invalid Emails

def validate_emails(emails):
  return [email for email in emails if '@' in email]

emails = ["jimmyjohnson@gmail.com", "alyssaG@gmail.com", "ethaniscoolAtgmail.com"]

valid_emails = validate_emails(emails)
print(valid_emails)