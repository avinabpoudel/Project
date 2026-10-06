names = ["Aditya" , "Aalok" , "Arbin", "Aashok", "Arjun"]
names.append("Shiv")
names.remove("Arbin")
names.sort()
names.reverse()
print(names)


#Dictionary
teacher = {
    "name":"Navraj",
    "Subject":"Maths",
    "Experience":"4"
}
print("Subject:", teacher["Subject"])
print("Experience: ", teacher.get("Experience"))

teacher["Experience"] = 6
teacher["age"] = 24
teacher.pop ("name")
print("Updated:" , teacher)


rollnum = [1, 2, 3, 4, 5]
nam = ["Aditya" , "Aalok" , "Arbin", "Aashok", "Arjun"]
student = dict(zip(rollnum , nam))
print("Names of student and roll: " , student)
print(student[2])

