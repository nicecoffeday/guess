import random
r = random.randint(1,100)
count = 0
while True:
	count += 1 
	a = int(input('請猜一個數字'))
	if a == r: 
		print('您猜對了')
		break 
	elif a < r:
		print('比答案小')
	elif a > r:
		print('比答案大')
	print('這是你猜的第', count, '次')

		
		

