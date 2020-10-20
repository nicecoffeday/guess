import random
start = int(input('請決定隨機數字開始值:'))
end = int(input('請決定隨機數字結束值:'))
r = random.randint(start,end)
count = 0
while True:
	count += 1 
	a = int(input('請猜一個數字'))
	if a == r: 
		print('您猜對了')
		print('這是你猜的第', count, '次')
		break 
	elif a < r:
		print('比答案小')
	elif a > r:
		print('比答案大')
	print('這是你猜的第', count, '次')

		
		

