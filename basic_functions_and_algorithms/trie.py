# build a trie with a list of string


def buildTrie(words):
	root = {}
	for w in words:
		curr = root
		for c in w:
			if c not in curr:
				curr[c] = {}
			curr = curr[c]
		curr['#'] = w
	return root


def search(root, word):
	curr = root
	for c in word:
		if c not in curr:
			return False
		curr = curr[c]
	return '#' in curr


ls = 'my list is very long'.split(' ')
tree = buildTrie(ls)
print search(tree, 'very')
