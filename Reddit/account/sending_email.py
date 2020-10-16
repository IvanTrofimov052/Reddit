import smtplib

class:
	def __init__(self):
		smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
		smtpObj.starttls()

