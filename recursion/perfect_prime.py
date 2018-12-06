list_int = int(input())
int_len = len(str(list_int))
def prime(n):
    if n <= 1:
        return 0
    
    for i in range(2,n):
        if n%i == 0:
            return 0
    return 1

def per_prime(n):
	global num
	if prime(n) == 0 :
		return 0
	else:
		for x in range(int_len):
			for y in range(int_len-x):
				if x==int_len-y:
					break
				n_new = str(n)[x:int_len-y]
				n_new = int(n_new)
				if prime(n_new)==0:
					break
				elif x== int_len-1 and y==0 and prime(n_new)==1 :
					num +=1
num =0 
number = 0
while(num<list_int):
	per_prime(number)
	number += 1

print(number-1)




