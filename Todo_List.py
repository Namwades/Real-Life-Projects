def read_tasks():
    try:
        with open('tasks.txt', 'r') as file:
            tasks = file.read().splitlines()
        return tasks
    except FileNotFoundError:
        return []

def write_tasks(tasks):
    with open('tasks.txt', 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def add_task():
    task = input('Enter the task: ')
    tasks.append(task)
    write_tasks(tasks)
    print('Task added successfully!')

def complete_task():
    print('Tasks:')
    display_tasks()
    task_index = int(input('Enter the task number to mark as complete: ')) - 1
    if 0 <= task_index < len(tasks):
        tasks[task_index] += ' [DONE]'
        write_tasks(tasks)
        print('Task marked as complete!')
    else:
        print('Invalid task number.')

def display_tasks():
    if len(tasks) > 0:
        for index, task in enumerate(tasks, start=1):
            print(f'{index}. {task}')
    else:
        print('No tasks.')

def main():
    global tasks
    tasks = read_tasks()

    while True:
        print('Todo List')
        print('1. Add Task')
        print('2. Mark Task as Complete')
        print('3. Display Tasks')
        print('4. Quit')

        choice = input('Enter your choice: ')

        if choice == '1':
            add_task()
        elif choice == '2':
            complete_task()
        elif choice == '3':
            display_tasks()
        elif choice == '4':
            break
        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()