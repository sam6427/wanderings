import sys
from random import randint

def play_game(start, end, jackpot):
	while True:
		user_input = input(f'Try to guess a number between {start} and {end}: \n')
		try:
			user_guess = int(user_input)
			if user_guess == jackpot :
				print('Well done !! You won the game !') 
				break
			else :
				print('Bad luck ! Try again.')
		except ValueError:
			print('Please enter a number.')
			continue


try:
	start = int(sys.argv[1])
	end = int(sys.argv[2])
	jackpot = randint(start, end)
	play_game(start, end, jackpot)

except IndexError as err:
	print('Enter two numbers to play the game.')

		