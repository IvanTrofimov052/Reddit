import random

def random_non_repeating_nums(max, need_nums):
	population = range(1,max+1)

	return random.sample(population, need_nums)