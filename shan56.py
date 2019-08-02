n=input()
for i in n:
	if i.isdigit():
		flag=0
	else:
		flag=1
		break
if flag==0:
	print("yes")
else:
	print("no")
