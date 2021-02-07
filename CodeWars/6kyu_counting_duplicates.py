'''
Write a function that will return the count of distinct case-insensitive alphabetic characters
and numeric digits that occur more than once in the input string. The input string can be assumed
to contain only alphabets (both uppercase and lowercase) and numeric digits
'''


def duplicate_count(text):
	text = text.lower()
	counts = dict()
	total = 0

	for i in text:
		counts[i] = counts.get(i, 0) + 1

	duplicates = list(counts.values())
	duplicates = [x for x in duplicates if x > 1]
	return len(duplicates)

print(duplicate_count("abcde"))
print(duplicate_count("abcdea"))
print(duplicate_count("indivisibility"))

'''
test.assert_equals(duplicate_count("abcde"), 0)
test.assert_equals(duplicate_count("abcdea"), 1)
test.assert_equals(duplicate_count("indivisibility"), 1)
'''
