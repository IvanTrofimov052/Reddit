import smtplib


def sending_email(email, text):
	try:
		smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
		smtpObj.ehlo()
		smtpObj.starttls()
		smtpObj.login('wristoservice@gmail.com', 'alcodance')
		smtpObj.sendmail("wristoservice@gmail.com", email, text)
		smtpObj.quit()
	except:
		pass
