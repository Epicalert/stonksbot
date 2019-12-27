import json
from os import path
import getpass

def create_credentials_file():
	"""Asks user for all credentials and writes it to credentials.json"""
	credentials = {}
	
	descriptions = json.loads(open("credential_descriptions.json").read())

	print("Please enter your credentials below. (All input will be hidden for security.)")
	for key in descriptions:
		credentials[key] = getpass.getpass(descriptions[key] + ": ")

	open("credentials.json", "w+").write(json.dumps(credentials))


create_credentials_file()
