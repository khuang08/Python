def queue_time(customers, n):
	time = 0
	tills = [0]*n
	for i in range(len(customers)):
		tills.sort()
		tills[0] += customers[i]
		time = max(tills)
	return time

print(queue_time([], 1))
print(queue_time([5], 1))
print(queue_time([2], 5))
print(queue_time([1,2,3,4,5], 1))
print(queue_time([1,2,3,4,5], 100)) #5
print(queue_time([2,2,3,3,4,4], 2)) #9
print(queue_time([43, 27, 50, 48, 1, 49, 12, 44, 13, 15, 2, 15, 18, 20, 41, 21, 18, 44, 30, 14], 3)) #186
print(queue_time([50, 16, 7, 35, 11, 8, 13, 14, 25, 10, 37, 44, 45, 40, 16, 37],4)) #126
