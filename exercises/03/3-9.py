# 3-9. Email Domain Extraction

email_1 = 'mclovin@gmail.com'
email_2 = 'ilovepython@yahoo.com'

print(email_1[8:])
print(email_2[12:])

# challenge answer

print(email_1[email_1.index("@") + 1:])
print(email_2[email_2.index("@") + 1:])
# add 1 because the starting index is inclusive!
# yay no counting!