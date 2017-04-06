# Given a string array words, find the maximum value of length(word[i]) * length(word[j]) 
# where the two words do not share common letters. 
# You may assume that each word will contain only lower case letters. 
# If no such two words exist, return 0.



# thinking process
# 1. cannot think of a way which do not iterate through the words.

# 2. so go with the intuitive way: 2 for loops

# 3. think of a better way to check if 2 words has same character or not

# 	3.1 use set, two many space
# 	3.2 use bit map, since there are only 26 characters


# conclusion:
# use bit map to improve both space and speed
def solve(words):
	def toBitMap(words):
		result = 0
		for c in words:
			result = result | (1 << ( ord(c) - ord('a') ) )
		return result
	nums = map(toBitMap, words)
	result = 0
	for i in xrange(0, len(nums)-1):
		for j in xrange(i+1, len(nums)):
			if nums[i] & nums[j] == 0:
				result = max(result, len(words[i]) * len(words[j]))
	return result


words = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
print solve(words)


