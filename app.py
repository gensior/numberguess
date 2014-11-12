import random

def main():
	quit = False
	score = []
	print("Welcome to the guessing game!");
	print("Guess a number.")
	secret = random.randint(1,100)
	# print(secret)
	while(not quit):
		try:
			guess = input(":")
			guess = int(guess)
			score.append(compare(guess, secret))
			if (score[-1] == 0):
				print("Your score is:", calc_score(score))
				break
		except ValueError:
			if(guess.upper() == 'Q'):
				print("Thanks for playing!")
				quit = True

def calc_score(scores):
	total = 0
	count = 1
	for score in scores:
		total += abs(score) * count
		count += 1
	return total

def compare(guess, secret):
	difference = guess - secret
	if (difference > 0):
		print("You are too high.")
	if (difference < 0):
		print("You are too low.")
	if (difference == 0):
		print("You win")
	return difference


# print("Hello program")
"""
	Multi line comments
	use triple quotes
"""

if __name__ == "__main__":
	main()