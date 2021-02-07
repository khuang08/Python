def up_array(arr):
	if arr == [] or type(arr) != list or [x for x in arr if type(x) != int] != [] or min(arr) < 0 or max(arr) > 9:
		return None

	result = str(int(''.join(map(str,arr))) + 1)
	return [int(x) for x in result]

print(up_array([9])) #[1,0]
print(up_array([2,3,9])) #[2,4,0]
print(up_array([9,9,9])) #[1,0,0,0]
print(up_array([4,3,2,5])) #[4,3,2,6]
print(up_array([1,-9])) #None