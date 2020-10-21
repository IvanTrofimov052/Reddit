import hashlib

def hashing_passwords(password):
	sha = hashlib.sha1(password.encode('utf-8'))
	return sha.hexdigest()
