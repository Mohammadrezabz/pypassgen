import string
import random
MIN_RANGE = 16
MAX_RANGE = 26

def generate():
	words = [word for word in string.ascii_letters]
	punctuations = [punc for punc in string.punctuation] 
	digits = [dig for dig in string.digits]
	all_keyboard = words + punctuations + digits
	password = ""
	for i in range(random.randrange(MIN_RANGE , MAX_RANGE)):
		password += "".join(random.choice(all_keyboard)) 
		

	print(password)

	


if __name__ == '__main__':
	generate()
