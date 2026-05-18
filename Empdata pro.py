employee_data = [
    (101, "Alice Smith", "Engineering", 90000, 5),
    (102, "Bob Johnson", "Marketing", 75000, 3),
    (103, "Charlie Brown", "Engineering", 120000, 8),
    (104, "Diana Prince", "HR", 65000, 2),
    (105, "Edward King", "Marketing", 80000, 5),
    (106, "Frank Castle", "Engineering", 95000, 0),
]

print("Employee Records:\n")

for emp_id, name, dept, salary, years in employee_data:
    print(f"ID: {emp_id}, Name: {name}, Department: {dept}, Salary: {salary}, Years: {years}")

salary_sorted = sorted(employee_data, key=lambda x: x[3])

print("\nEmployees Sorted by Salary:\n")
for emp in salary_sorted:
    print(emp)

service_sorted = sorted(employee_data, key=lambda x: x[4], reverse=True)

print("\nEmployees Sorted by Years of Service:\n")
for emp in service_sorted:
    print(emp)

total_salary = sum(emp[3] for emp in employee_data)
min_salary = min(emp[3] for emp in employee_data)
max_salary = max(emp[3] for emp in employee_data)

print("\nSalary Statistics:")
print("Total Salary:", total_salary)
print("Minimum Salary:", min_salary)
print("Maximum Salary:", max_salary)
engineering_employees = [
    emp for emp in employee_data if emp[2] == "Engineering"
]

print("\nEngineering Employees:\n")
for emp in engineering_employees:
    print(emp)
all_experienced = all(emp[4] > 0 for emp in employee_data)

print("\nDo all employees have more than 0 years of service?")
print(all_experienced)
high_salary = any(emp[3] > 100000 for emp in employee_data)

print("\nIs any employee salary greater than 100000?")
print(high_salary)

del employee_data[3]

print("\nEmployee Data After Deletion:\n")
for emp in employee_data:
    print(emp)
employee_data = [
    (101, "Alice Smith", "Engineering", 90000, 5),
    (102, "Bob Johnson", "Marketing", 75000, 3),
    (103, "Charlie Brown", "Engineering", 120000, 8),
    (104, "Diana Prince", "HR", 65000, 2),
    (105, "Edward King", "Marketing", 80000, 5),
    (106, "Frank Castle", "Engineering", 95000, 0),
]
salary_sorted = sorted(employee_data, key=lambda emp: emp[3], reverse=True)

print("Employees Sorted by Salary (Descending):")
for emp in salary_sorted:
    print(emp)
service_name_sorted = sorted(
    employee_data,
    key=lambda emp: (-emp[4], emp[1])
)

print("\nEmployees Sorted by Years of Service and Name:")
for emp in service_name_sorted:
    print(emp)
total_salary = sum(emp[3] for emp in employee_data)
min_salary = min(emp[3] for emp in employee_data)
max_salary = max(emp[3] for emp in employee_data)
average_service = sum(emp[4] for emp in employee_data) / len(employee_data)

print("\nSalary and Service Statistics:")
print("Total Salary Expenditure:", total_salary)
print("Minimum Salary:", min_salary)
print("Maximum Salary:", max_salary)
print("Average Years of Service:", average_service)

high_earners = [emp[1] for emp in employee_data if emp[3] > 90000]

print("\nHigh Earners:")
print(high_earners)


for index, emp in enumerate(employee_data):
    if emp[0] == 104:
        del employee_data[index]
        break

print("\nEmployee Data After Removing Employee ID 104:")
for emp in employee_data:
    print(emp)


all_service = all(emp[4] >= 1 for emp in employee_data)


engineering_low_salary = any(
    emp[2] == "Engineering" and emp[3] < 70000
    for emp in employee_data
)

print("\nValidation Checks:")
print("All employees have at least 1 year of service:", all_service)
print("Any Engineering employee earns less than 70000:", engineering_low_salary)