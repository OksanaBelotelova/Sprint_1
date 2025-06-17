new_tasks = ['task_001', 'task_011', 'task_007', 'task_015', 'task_005']
completed_tasks = ['task_002', 'task_012', 'task_006']

# 1.Перенести 'task_005' из списка new_tasks в список completed_tasks:

for task in new_tasks:
    if task == 'task_005':
        new_tasks.remove(task)
        completed_tasks.append(task)

        print(new_tasks)
        print(completed_tasks)

# 2. Удалить'task_007' из списка new_tasks:

new_tasks.remove('task_007')
print(new_tasks)

# 3. Вывести последнюю задачу из списка new_tasks на экран:

print(new_tasks[-1])
