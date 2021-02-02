n1 = 16
n2 = 55
n3 = 118
count1 = 0
count2 = 0 
count3 = 0

# count the numbers between 1 and 5000000 that are divisible by 16, 55, 118
for num in range(1,5000001):
    if (num % n1 == 0):
        count1+=1 
    elif (num % n2 == 0):
        count2+=1 
    elif (num % n3 == 0):
        count3+=1 
print(count1+count2+count3)
