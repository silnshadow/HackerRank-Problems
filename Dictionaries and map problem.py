n = int(input())
d = dict()
for _ in range(0,n):
    name=str(input())
    phone[name]=input()
	d[name] = number
for _ in range (0,n):
	name = input()
	if name in d:
		print(name + "=" + d[name]) 
	else:
		print("Not found")


