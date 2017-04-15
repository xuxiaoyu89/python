'''
Given a digit string, 
return all possible letter combinations that the number could represent.

0 - 9 : ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
'''

'''
combination, append current c to each one of previous result.

result = []
for n in num:
	temp = []
	for c in phone(n):
		for l in result:
			temp += l.append(c)
	result = temp
'''