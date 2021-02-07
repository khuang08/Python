def sort_array(source_array):
	if source_array == []:
		return []
	else:
		even = [(source_array.index(x), x) for x in source_array if x % 2 == 0]

#		for item in source_array:
#			if item % 2 == 0:
#				source_array.remove(item)

		source_array = [x for x in source_array if x % 2 != 0]
	
		source_array.sort()

		for (x, y) in even:
			source_array.insert(x, y)

	return(source_array)

print(sort_array([5, 3, 2, 8, 1, 4]))
print(sort_array([5, 3, 1, 8, 0]))
print(sort_array([]))

'''
Test.assert_equals(sort_array([5, 3, 2, 8, 1, 4]), [1, 3, 2, 8, 5, 4])
Test.assert_equals(sort_array([5, 3, 1, 8, 0]), [1, 3, 5, 8, 0])
Test.assert_equals(sort_array([]),[])
'''