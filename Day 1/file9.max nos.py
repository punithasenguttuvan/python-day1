time=int(input("Enter the number of time slots:"))
entry=[int(input("Enter the number of guests entering at time slot {}: ".format(i+1))) for i in range (time)]
exit=[int(input("Enter the number of guests exiting at time slot {}: ".format(i+1))) for i in range(time)]

count=0
guests=[]
for i in range(len(entry)):
    count=count+entry[i]-exit[i]
    guests.append(count)

print("The maximum number of guests present at any time:",max(guests))
