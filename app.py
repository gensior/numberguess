import random

def main():
	loops = 0
	score = []
	print("Welcome to the guessing game!");
	print("Guess a number.")
	secret = random.randint(1,64)
	# print(secret)
	while(loops < 8):
		try:
			guess = input(":")
			guess = int(guess)
			score.append(compare(guess, secret))
			if (score[-1] == 0):
				break
			loops += 1
		except ValueError:
			continue
	if (loops >= 8):
		print("You lose!")


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