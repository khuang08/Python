def two_sum(numbers, target):
	result = []
	if numbers == [] or target == None:
		return []
	else:
		for i in numbers[:-1]:
			for j in numbers[1:]:
				if i + j == target:
					result.append(numbers.index(i))
					result.append(numbers.index(j,1,len(numbers)))
					return result

print(sorted(two_sum([1,2,3], 4)))
print(sorted(two_sum([1234,5678,9012], 14690)))
print(sorted(two_sum([2,2,3], 4)))

'''
Test.assert_equals(sorted(two_sum([1,2,3], 4)), [0,2])
Test.assert_equals(sorted(two_sum([1234,5678,9012], 14690)), [1,2])
Test.assert_equals(sorted(two_sum([2,2,3], 4)), [0,1])
'''
