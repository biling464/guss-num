import random
r = random.randint(1, 100)
count = 0
while True:
	count = count +1
	n = input('請猜數字 :')
	n = int(n)
	if n == r :
		print("終於猜對了")
		print("這是你猜的第",count,"次")
		break
	elif n < r :
		print("比答案小")
	else :
		print("比答案大")
	print("這是你猜的第",count,"次")