employees = [
    (1001, "Alice Johnson", "Sales", 15000, 4.2),
    (1002, "Bob Smith", "Sales", 12000, 3.8),
    (1003, "Carol Davis", "Marketing", 8000, 4.5),
    (1004, "David Brown", "Sales", 18000, 4.0),
    (1005, "Eva Wilson", "Marketing", 9500, 3.2),
    (1006, "Frank Miller", "IT", 11000, 3.9),
    (1007, "Grace Lee", "Sales", 13500, 2.1),
    (1008, "Henry Taylor", "IT", 10500, 4.1),
    (1009, "Ivy Chen", "Marketing", 7800, 3.7),
    (1010, "Jack Davis", "IT", 12500, 3.5)
]



departments = {}

for emp in employees:
    emp_id, name, dept, sales, rating = emp

    if dept not in departments:
        departments[dept] = []

    departments[dept].append(emp)

print("Top 3 Performers by Department:\n")

for dept, emp_list in departments.items():

    sorted_employees = sorted(
        emp_list,
        key=lambda x: x[3],
        reverse=True
    )

    print(f"{dept} Department:")

    for index, emp in enumerate(sorted_employees[:3], start=1):
        print(f"{index}. {emp[1]}: ${emp[3]}")

    print()



print("Department Average Ratings:")

for dept, emp_list in departments.items():

    avg_rating = sum(emp[4] for emp in emp_list) / len(emp_list)

    print(f"{dept}: {avg_rating:.2f}")



print("\nEmployees Needing Improvement (Rating < 3.0):")

for emp in employees:

    if emp[4] < 3.0:
        print(f"{emp[1]} ({emp[2]}): Rating {emp[4]}")



performance_scores = []

for emp in employees:

    performance_score = emp[3] * emp[4]

    performance_scores.append(
        (emp[1], performance_score)
    )

ranked_employees = sorted(
    performance_scores,
    key=lambda x: x[1],
    reverse=True
)

print("\nPerformance Ranking (Sales × Rating):")

for rank, emp in enumerate(ranked_employees, start=1):
    print(f"{rank}. {emp[0]}: {emp[1]}")

print("\nDepartment Performance Summary:\n")

for dept, emp_list in departments.items():

    total_employees = len(emp_list)

    avg_sales = sum(emp[3] for emp in emp_list) / total_employees

    avg_rating = sum(emp[4] for emp in emp_list) / total_employees

    print(
        f"{dept}: {total_employees} employees, "
        f"Avg Sales: ${avg_sales:.2f}, "
        f"Avg Rating: {avg_rating:.2f}"
    )