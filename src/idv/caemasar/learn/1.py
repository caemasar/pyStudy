import random

secret = random.randint(1,10)
print(secret)
print('-------------xxxxx-------------')
temp = input('guess:\n')
guess = int(temp)
i=3;
while i>0:
	if guess == secret:
		print('Y')
		break
	else:
		if guess>secret:
			print('>')
		else:
			print('<')
		i=i-1
		if(i>0):
			temp = input('guess again:\n')
			guess = int(temp)
print(secret)
print('OVER')
