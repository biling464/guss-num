import random
start = input("請輸入開始值 :")
end = input("請輸入結束值 :")
start = int(start)
end = int(end)
r = random.randint(start, end)
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