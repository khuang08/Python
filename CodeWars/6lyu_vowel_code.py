def encode(st):
	vowels = {'a':'1', 'e':'2', 'i':'3', 'o':'4', 'u':'5'}
	string = ''.join([vowels[x] if x in vowels else x for x in list(st)])
	return string
    
def decode(st):
    numbers = {'1':'a', '2':'e', '3':'i', '4':'o', '5':'u'}
    string = ''.join([numbers[x] if x in numbers else x for x in list(st)])
    return string


print(encode('hello')) #'h2ll4'
print(encode('How are you today?')) #'H4w 1r2 y45 t4d1y?'
print(encode('This is an encoding test.')) #'Th3s 3s 1n 2nc4d3ng t2st.'
print(decode('h2ll4')) #'hello'

