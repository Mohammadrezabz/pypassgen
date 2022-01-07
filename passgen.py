import string
import random
MIN_RANGE = 16
MAX_RANGE = 26
PATH = 'C://Users//Mohammadreza//Documents//Passgen.txt'
def generate(acc_name):
	words = [word for word in string.ascii_letters]
	punctuations = [punc for punc in string.punctuation] 
	digits = [dig for dig in string.digits]
	all_keyboard = words + punctuations + digits
	password = ""
	for i in range(random.randrange(MIN_RANGE , MAX_RANGE)):
		password += "".join(random.choice(all_keyboard)) 
		

	print(password)

	with open(PATH , 'a+') as file :
		file.write(acc_name +':'+ password + '\n')


if __name__ == '__main__':
	acc_name = str(input("Account Name?? : "))
	generate(acc_name)