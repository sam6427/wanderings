import sys
from random import randint

def run_guess(start, end, guess, jackpot):
	try:
		if start <= guess <= end :
			if guess == jackpot:
				print('Well done !! You won the game !') 
				return True
			else:
				print('Bad luck ! Try again.')
				return False
		else:
			print(f'Please enter a number netween {start} and {end}')
			return False
	except TypeError:
		print('arguments mudt all be numbers')
		return False

# useful only for other version

# def play_game(start, end, jackpot):
# 	while True:
# 		user_input = input(f'Try to guess a number between {start} and {end}: \n')
# 		try:
# 			user_guess = int(user_input)
# 			if user_guess == jackpot :
# 				print('Well done !! You won the game !') 
# 				break
# 			else :
# 				print('Bad luck ! Try again.')
# 		except ValueError:
# 			print('Please enter a number.')
# 			continue

if __name__ == '__main__':
	try:
		start = int(sys.argv[1])
		end = int(sys.argv[2])
		jackpot = randint(start, end)
		while True:
			try:
				user_input = input(f'Try to guess a number between {start} and {end}: \n')
				user_guess = int(user_input)
				if run_guess(start, end, user_guess, jackpot):
					break
			except ValueError:
				print('Please enter a number.')
				continue

	except IndexError as err:
		print('Enter two numbers to play the game.')



# other version using play_game()

# try:
# 	start = int(sys.argv[1])
# 	end = int(sys.argv[2])
# 	jackpot = randint(start, end)
# 	play_game(start, end, jackpot)

# except IndexError as err:
# 	print('Enter two numbers to play the game.')



		