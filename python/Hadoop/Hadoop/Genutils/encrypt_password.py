'''
Module Name : encryt_password.py
Created On : 10th Nov 2019
Created By : amir riaz
Purpose : This module encrypts the password 
'''

#Importing Python Libraries
import Crypto
from Crypto.Cipher import ARC4
import base64


def main():
	#Asking for the user inputs
	password = raw_input("Enter the password : ")
	key = 'hkjhkhkl'

	#Getting the encrypted password
	val = encryptpassword(password, key)
	encoded_val = base64.b64encode(val)
	print('The encrypted password value is : ' + str(encoded_val))

	#decryptpassword(encoded_val,key)

#encryption function 
def encryptpassword(pwd, key):
	obj = ARC4.new(key)
	encryptedpassword = obj.encrypt(pwd)
	return encryptedpassword

#decryption function 
def decryptpassword(encoded_val, key):
	decoded_val = base64.b64decode(encoded_val)
	obj = ARC4.new(key)
	decryptedpassword = obj.decrypt(decoded_val)
	print('The decrypted password value is : ' + str(decryptedpassword))

#calling main function
main()






