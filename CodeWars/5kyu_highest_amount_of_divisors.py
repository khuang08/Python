'''
An array of different positive integers is given. We should create a code that gives us the number (or the numbers) that has (or have) the highest number of divisors among other data.

The function proc_arrInt(), (Javascript: procArrInt()) will receive an array of unsorted integers and should output a list with the following results:
[(1), (2), (3)]

(1) - Total amount of numbers received
(2) - Total prime numbers received
(3) - a list [(a), (b)]
      (a)- The highest amount of divisors that a certain number (or numbers) of the given  
           array have
      (b)- A sorted list with the numbers that have the largest amount of divisors. The list may  
           have only one number

'''
def isPrime(number):
    if number < 1 or number % 1 > 0:
        return False
    else:
        for n in range(2, number//2):
            if (number % n) == 0:
                return False
        return True       

def tau(n):
        sqroot,t = int(n**0.5),0
        for factor in range(1,sqroot+1):
                if n % factor == 0:
                        t += 2
        if sqroot*sqroot == n: t = t - 1
        return t

def proc_arrInt(listNum):
    length = len(listNum)

    max_count = 0
    highest_divisor = []

    prime_count = len([x for x in listNum if isPrime(x)])
    divisors = sorted([x for x in listNum if isPrime(x) == False])

    for i in divisors:
        temp_count = tau(i)
        if temp_count > max_count:
            max_count = temp_count
            highest_divisor = [i]
        elif temp_count == max_count:
            highest_divisor.append(i)

    return [length, prime_count, [max_count, highest_divisor]]

arr1 = [66, 36, 49, 40, 73, 12, 77, 78, 76, 8, 50, 20, 85, 22, 24, 68, 26, 59, 92, 93, 30] 
print(proc_arrInt(arr1)) #[21, 2, [9, [36]]]

arr2 = [267, 273, 271, 145, 275, 150, 487, 169, 428, 50, 314, 444, 445, 67, 458, 211, 58, 95, 357, 486, 359, 491, 108, 493, 247, 379] 
print(proc_arrInt(arr2)) #[26, 7, [12, [108, 150, 444, 486]]]


