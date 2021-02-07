def count(string):
	characters = dict()
	string = list(string)

	for i in string:
		characters[i] = string.count(i)
	return(characters)


print(count('aba')) #{'a': 2, 'b': 1}
print(count('')) #{}