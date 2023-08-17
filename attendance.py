import pandas as pd

data = pd.DataFrame(columns=['Name', 'Branch Number', 'Department', 'Age'])

number = int(input("Enter the number of students: "))

for i in range(number):
    print(f"\nEnter details for student #{i+1}:")
    name = input("Enter your name: ")
    branch_number = input("Enter your Branch Number: ")
    department = input("Enter your department: ")
    age = input("Enter your Age: ")

    data = data._append({
            'Name': name,
            'Branch Number': branch_number,
            'Department': department,
            'Age': age
        }, ignore_index=True)

filename = input("\nEnter the filename to save the data (without extension): ")
data.to_csv(f"{filename}.csv", index=False)
print(f"\nStudent data has been saved to {filename}.csv")
