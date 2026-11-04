file = open("notes.txt", "w")
file.write("1. Visit somewhere nice\n")
file.write("2. Go to paris\n")
file.write("3. Play football\n")
file.close()

inpput = int(input("How many lines to preview?"))
file = open("notes.txt", "r")
print(file.read(inpput))
file.close()

file = open("notes.txt", "r")
lines = file.readlines()
file.close()
print(f"Total lines{len(lines)}")
for i in range(len(lines)):
    print(i + 1, "==>", lines[i].strip())

word = input("Skip lines which start with: ")
file = open("notes.txt", "r")
for line in file:
    if line.startswith(word): 
        print("Skip ==>", line.strip())
    else:
        print("keep ==>", line.strip())
file.close()
print()

file = open("notes.txt", "r")
lines = file.readlines()
file.close()
out = open("odd.txt", "w")
for i in range(0,len(lines),2):
    out.write(lines[i])
out.close
print("Odd lines saved to odd")

file.close()