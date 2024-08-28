person = ["John", "Alice", "James", "Liam", "Michael"]

John = ["Name : John", "Age : 15", "Gender : Male"]
Alice = ["Name : Alice", "Age : 17", "Gender : Female"]
James = ["Name : James", "Age : 12", "Gender: Male"]
Liam = ["Name : Liam", "Age : 18", "Gender : Male"]
Michael = ["Name : Michael", "Age : 22", "Gender : Male"]

for i in person:
    print(i)

print("\n\nEnter Name")
name = input()

if name == "John":
    print("\n\n")
    for i in John:
        print(i)

if name == "Alice":
    print("\n\n")
    for i in Alice:
        print(i)
        
if name == "James":
    print("\n\n")
    for i in James:
        print(i)
        
if name == "Liam":
    print("\n\n")
    for i in Liam:
        print(i)

if name == "Michael":
    print("\n\n")
    for i in Michael:
        print(i)