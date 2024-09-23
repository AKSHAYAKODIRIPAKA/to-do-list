import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        # Listbox to display tasks
        self.task_listbox = tk.Listbox(root, width=50, height=10, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)

        # Entry box for new tasks
        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.pack(pady=5)

        # Buttons
        self.add_task_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_task_button.pack(side=tk.LEFT, padx=5)
        
        self.remove_task_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_task_button.pack(side=tk.LEFT, padx=5)

        self.clear_all_button = tk.Button(root, text="Clear All", command=self.clear_all)
        self.clear_all_button.pack(side=tk.LEFT, padx=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def remove_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_index)
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to remove.")

    def clear_all(self):
        self.task_listbox.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
