print("GWA Calculator")
no_of_subject = int(input("\nEnter No. of Subjects: "))
excluded_subjects = int(input("How many subjects are excluded?: "))

totalUnits = 0
sumGrades = []
displayList = []
excludedList = []

for i in range(excluded_subjects):
    SUBJECT = input("Excluded Subject Name:\t")
    excludedList.append(SUBJECT)

for j in range(no_of_subject):
    infoList = []
    print("\n--------------------------------")
    SUBJECT = input("Subject Name:\t")

    if SUBJECT in excludedList:
        GRADE = float(input("Enter Grade:\t"))
        UNIT = int(input("Enter No. Unit:\t"))

        infoList.append(SUBJECT)
        infoList.append(GRADE)
        infoList.append(UNIT)

        displayList.append(infoList)

    else:
        GRADE = float(input("Enter Grade:\t"))
        UNIT = int(input("Enter No. Unit:\t"))

        infoList.append(SUBJECT)
        infoList.append(GRADE)
        infoList.append(UNIT)

        displayList.append(infoList)

        sumGrades.append(GRADE * UNIT)
        totalUnits += UNIT
        

print("\nSubject---------Grade---------Unit----")
for index in range(len(displayList)):
    print("--------------------------------------")
    print(f"{displayList[index][0]}\t\t{displayList[index][1]}\t\t{displayList[index][2]}")
    print("--------------------------------------")

GWA = sum(sumGrades) / totalUnits
print(sum(sumGrades))
print(f"\tGWA: {GWA}")