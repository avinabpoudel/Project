import datetime
today = datetime.datetime.now()
print (today)


# Problem 1
marks = int(input("Enter your marks: "))
if marks > 90:
    print("Outstanding")
elif marks>60:
    print("Good")
elif marks>40:
    print("Pass")
else:
    print("Fail")