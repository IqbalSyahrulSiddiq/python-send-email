import csv, smtplib, ssl

message = """Subject: Your grade

Hi {name}, your grade is {grade}"""
from_address = "8f6a6d71fd6056"
password = "e966a6bc141df8"

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 2525, context=context) as server:
    server.login(from_address, password)
    with open("listContact.csv") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for name, email, grade in reader:
            server.sendmail(
                from_address,
                email,
                message.format(name=name,grade=grade),
            )