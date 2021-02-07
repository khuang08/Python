def work_on_strings(a,b):
	temp_a = [x for x in a]
	temp_b = [y for y in b]

	for i in range(len(temp_a)):
		for j in range(len(temp_b)):
			if temp_a[i].lower() == temp_b[j].lower():
				if temp_b[j].islower():
					temp_b[j] = temp_b[j].upper()
				else:
					temp_b[j] = temp_b[j].lower()

	for i in range(len(temp_b)):
		for j in range(len(temp_a)):
			if temp_b[i].lower() == temp_a[j].lower():
				if temp_a[j].islower():
					temp_a[j] = temp_a[j].upper()
				else:
					temp_a[j] = temp_a[j].lower()

	result = ''.join(temp_a) + ''.join(temp_b)
	return result


print(work_on_strings("abc","cde"), "abCCde")
print(work_on_strings("abcdeFgtrzw", "defgGgfhjkwqe"), "abcDeFGtrzWDEFGgGFhjkWqE")
print(work_on_strings("abcdeFg", "defgG"), "abcDEfgDEFGg")
print(work_on_strings("abab", "bababa"), "ABABbababa")
