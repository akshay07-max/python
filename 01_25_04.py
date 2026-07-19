x = [12, 23, 34, 45, 66, -4, -5, -90]

for i in x:
    if(i<0):
         print("negative Number")
    else:
        print("Positive Number")

if any(n<0 for n in x):
    print("negative number")

else:
    print("Positive Number")