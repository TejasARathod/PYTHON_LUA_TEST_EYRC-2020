def fn(x,length):
	num2 = 0
	for i in x:
		if(i>100 or i<-100):
			r=0
			return
	
	print(x[::-1])
	for i in x[::-1]:
		print(i,end=" ")
	print()
	for i in range(1,length):
		if(i%3==0):
			print(x[i]+3,end=" ")
		

	print()
	for i in range(1,length):

		num2 = i
		if(num2%5==0):
			print(x[i]-7,end=" ")
		
	print()

				
					

	print(sum(x[3:8]))



test_cases = int(input())
if(test_cases>=1 and test_cases <= 25):
	for case in range(test_cases):

		length = int(input())
		if(length >=8 and length <= 50):
			x = list(map(int,input().split(" ")))[0:length:]
			if(len(x)!=length):
				break

			fn(x,length)
			

		
		else:
			break