import string
import random
import argparse
import os 
MIN_RANGE = 16
MAX_RANGE = 26
if os.name == "nt":
	PATH = os.environ['USERPROFILE'] + '\\Documents\\Passgen.txt'
else:
	PATH = os.path.expanduser('~') + '/Documents/passgen.txt'
def generate(acc_name , pathto):
	words = [word for word in string.ascii_letters]
	punctuations = [punc for punc in string.punctuation] 
	digits = [dig for dig in string.digits]
	all_keyboard = words + punctuations + digits
	password = ""
	for i in range(random.randrange(MIN_RANGE , MAX_RANGE)):
		password += "".join(random.choice(all_keyboard)) 
		

	print(password)

	with open(pathto , 'a+') as file :
		file.write(acc_name +':'+ password + '\n')


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Password Generator")
	parser.add_argument('-p' , '--path' , default = PATH ,  type=str , help="Path For Saving Passwords")
	parser.add_argument('-A' , '--account' , type=str , help="Account Name For Generated Password" , required=True)
	args = parser.parse_args()
	generate(acc_name=args.account , pathto = args.path)
