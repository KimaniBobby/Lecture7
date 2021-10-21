#marks

def main():
    print("This program doees an average of students marks")
    print()

    student1 = int(input("enter studnt 1 marks: "))
    student2 = int(input("enter studnt 2 marks: "))
    student3 = int(input("enter studnt 3 marks: "))
    student4 = int(input("enter studnt 4 marks: "))
    student5 = int(input("enter studnt 5 marks: "))

    average = (student1+student2+student3+student4+student5)/5

    print("The average mark for the class is:",average)

main()
