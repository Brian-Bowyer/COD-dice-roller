import random

def compute_successes(pool, again=10, raw=True):
	"""Computes the number of successes on a given pool.

	pool - an int representing the number of dice to roll.
	again - an int representing on what value dice explode (i.e. where extra dice are added)
	raw - a bool representing whether the raw result is requested or the number of successes
	"""
	to_roll = pool
	rolls = []
	while to_roll > len(rolls):
		next_roll = random.randint(1,10)
		if next_roll >= again:
			to_roll += 1
		rolls.append(next_roll)

	return sorted(rolls, reverse=True) if raw else count_successes(rolls)

def count_successes(roll_list):
	return roll_list.count(10) + roll_list.count(9)+roll_list.count(8)