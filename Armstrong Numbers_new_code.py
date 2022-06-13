while True:
    num=input('Enter a positive number for Amstrong number check: ')
    if num.isnumeric():
        break
    else:
        print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
        continue
 
num_list=list(num)
num=int(num)
n=len(num_list)
sum=0
for i in num_list:
    sum+=int(i)**n
if num==sum:
    print(f'{num} is an Amstrong number.')
else:
    print(f'{num} is not an Amstrong number.')