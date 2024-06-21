# Dylan Hartman
# 06 / 21 / 2024
# BubbleSort.py

from random import randint

def getRandomList(size: int, minimum: int = 1, maximum: int = 100):
	return [randint(minimum, maximum) for i in range(size)]

def iteration(numbered_list: list, index: int):
	for idx in range(index-1):
		if numbered_list[idx] > numbered_list[idx + 1]:
			numbered_list[idx], numbered_list[idx + 1] = numbered_list[idx + 1], numbered_list[idx]
	return numbered_list

def bubbleSort(numbered_list: list):
	for idx in range(len(numbered_list), 1, -1):
		numbered_list = iteration(numbered_list, idx)

	return numbered_list


if __name__ == "__main__":
	numbered_list: list = getRandomList(10)
	print(f"Unsorted List: {numbered_list}")

	sorted_list: list = bubbleSort(numbered_list)
	print(f"Sorted List: {sorted_list}")

# EOF
