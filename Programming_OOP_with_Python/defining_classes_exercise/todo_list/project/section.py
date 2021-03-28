
class Section:
    def __init__(self,name):
        self.name = name
        self.tasks = []

    def add_task(self , new_task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        find = [t for t in self.tasks if t.name == task_name]
        if find:
            initial_task = find[0]
            initial_task.completed = True
            return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        initial_len = len(self.tasks)
        self.tasks = [t for t in self.tasks if not t.completed]
        return f"Cleared {initial_len - len(self.tasks)} tasks."

    def view_section(self):
        result = f"Section {self.name}:\n"
        result += '\n'.join([t.details() for t in self.tasks])
        return result



