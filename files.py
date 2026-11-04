file = open("bucket-list.txt", "w")
file.write("1. Play football\n")
file.write("2. Go sleep\n")
file.write("3. Watch movie\n")
file.close()
print("Our file")

file = open("bucket-list.txt", "r")
text = file.read()
print("\nThe content of file")
print(text)
file.close()

file = open("bucket-list.txt", "r")
fileline = file.readlines()
print(f"Your file has {len(fileline)} lines.")
file.close()

file = open("bucket-list.txt", "a")
file.write("4. Buy a new watch\n")
file.write("5. Buy Porche 9/11\n")
file.close()
print("\n 2 Items added")

file = open("bucket-list.txt", "r")
print("Updated file")
print(file.read())
file.close()



file = open("Something.html" ,"w")
file.write("<html>\n" \
"<body>\n" \
"<h1>Hello</h1>\n" \
"</body>\n" \
"</html>\n")
file.close()

