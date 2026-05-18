tasks_definitions = [
    ("T1", "Compile Code", 1, []),
    ("T2", "Run Unit Tests", 2, ["T1"]),
    ("T3", "Generate Report", 3, ["T2"]),
    ("T4", "Deploy Artifacts", 2, ["T1"]),
    ("T5", "Urgent Patch", 0, []),
]

task_queue = list(tasks_definitions)

print("Initial Task Queue:")
for task in task_queue:
    print(task)


task_queue.sort(key=lambda task: (task[2], task[0]))

print("\nTask Queue Sorted by Priority:")
for task in task_queue:
    print(task)


completed_tasks = []

print("\nProcessing Tasks:")

processing_queue = task_queue.copy()

while processing_queue:
    task = processing_queue.pop(0)

    task_id, description, priority, dependencies = task

    if all(dep in completed_tasks for dep in dependencies):
        print(f"Processing Task: {task_id} - {description}")
        completed_tasks.append(task_id)
    else:
        print(f"Skipping Task: {task_id} (Dependencies not met: {dependencies})")

print("\nCompleted Tasks:")
print(completed_tasks)


new_task = ("T6", "Emergency DB Backup", 0, [])

task_queue.insert(0, new_task)

print("\nTask Queue After Adding High-Priority Task:")
for task in task_queue:
    print(task)


reverse_queue = sorted(tasks_definitions, key=lambda task: task[2])


reverse_queue.reverse()

print("\nReverse Order Processing:")

while reverse_queue:
    task = reverse_queue.pop()   # Highest priority comes first
    print(f"Executing: {task[0]} - {task[1]}")


priorities = [task[2] for task in tasks_definitions]

min_priority = min(priorities)
max_priority = max(priorities)
sum_priority = sum(priorities)

print("\nPriority Analysis:")
print("Minimum Priority:", min_priority)
print("Maximum Priority:", max_priority)
print("Sum of Priorities:", sum_priority)

updated_tasks = []

for task in tasks_definitions:
    if task[0] == "T4":
        updated_task = ("T4", "Deploy Artifacts", 2, [])
        updated_tasks.append(updated_task)
    else:
        updated_tasks.append(task)

print("\nUpdated Tasks After Removing Dependency from T4:")
for task in updated_tasks:
    print(task)