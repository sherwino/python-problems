from collections import Counter

s = "abcdabcdabcdabcabcvmvmbvjbvassdasdererytyruuititiyiuyicabcdaabcdaabcd"

s = s.lower()
divisible_nums = [x for x in range(1, len(s)) if len(s) % x == 0]

print divisible_nums

for x in range(len(divisible_nums)):
	curNum = divisible_nums[x]
	splitList = [s[i:i+curNum] for i in range(0, len(s), curNum)]
	most_common_strings = (comstr for comstr in splitList if comstr[:1])
	c = Counter(most_common_strings)
	print c.most_common()
	

	# for idx in range(len(splitList)):

# 		print filter(lambda x: x == "Python", languages)
		
# 		squares = [x**2 for x in range(1, 11)]

# print filter(lambda x: x >= 30 and x <= 70, squares)

# garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"

# message = garbled[::-1]
#

# print message

# threes_and_fives = [x for x in range(1,16) if x%3==0 or x%5==0]

# from collections import Counter
# words_to_count = (word for word in word_list if word[:1].isupper())
# c = Counter(words_to_count)
# print c.most_common(3)