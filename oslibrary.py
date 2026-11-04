import os
print("---Notes---")
with open("notes.txt","r")as f:
    for line in f:
        print(line.strip())
    print()

print("--words--")
with open("notteees.txt","r") as f:
    for line in f:
        words = line.split()
        print(words)
        print(len(words),"words ->",line.strip())
    print()

print("--Merge--")
if os.path.exists("all-notes.txt"):
    print("all-notes.txt already exists - overwriting the file")
else:
    print("all-notes.txt not found so creating it")

content = ""
with open ("notes.txt", "r")as f:
    content += "--Notes.txt-- \n"
    content += f.read() + "\n"
with open ("notteees.txt","r")as f:
    content += "--Notteees.txt--\n"
    content += f.read() + "\n"
with open ("all-notes.txt", "w")as og:
    og.write(content)
print("Saved to all-notes.txt")
print()

if os.path.exists("all-notes.txt"):
    os.remove("all-notes.txt")
    print("all-notes.txt deleted")
else:
    print("all-notes.txt does not exists ")

