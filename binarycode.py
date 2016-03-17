high, low = 1000, 0

print('Please think of a number between {0} and {1}!'.format(low, high))

guessing = True 
while guessing:
	
	guess = +(low + high) // 2
	print('Is your number {0}?'.format(guess))
	pointer = raw_input("Enter 'h' to indicate the guess is to high. "
						"Enter 'l' to indicate the guess is to low. "
						"Enter 'c' to indicate I guessed correct.").lower()
	if pointer == 'h' :
		high = guess
	elif pointer == 'l' :
		low = guess
	elif pointer == 'c' :
		guessing = False
	else:
		print('sorry, I did not understand your input.')
		
print('Game over. Your number was {0}.'.format(guess))