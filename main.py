import tkinter as tk
from tkinter import messagebox
from ToDOItem import Todo

# The ID should persist across todos (use a global counter for now)
todo_id = 1

def handle_submit(title_var, status_var, priority_var):
    global todo_id  # Access the global counter
    
    todo_container = tk.Frame(root)
    todo_container.pack(pady=60, padx=10, fill="x")
    
    todo_dictionary = {
        "title": title_var.get(),
        "status": status_var.get(),
        "priority": priority_var.get()
    }
    
    if todo_dictionary["title"] == "":
        messagebox.showerror("Error", "You must enter a title!")
        return
        



    new_todo = Todo(todo_id, todo_dictionary["title"], todo_dictionary["status"], todo_dictionary["priority"])
    todo_id += 1  

    todo_item = tk.Label(todo_container, text=new_todo.title)
    todo_item.grid(column=0, row=0)

    print(new_todo.title) 

def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    frame.pack_forget()


def create_todo():
    todo_frame = tk.Frame(root)
    todo_frame.pack(pady=5, padx=10, fill="x")

    # Use StringVar() to track input values
    title_var = tk.StringVar()
    status_var = tk.StringVar()
    priority_var = tk.StringVar()

    title_label = tk.Label(todo_frame, text="Title")
    title_entry = tk.Entry(todo_frame, textvariable=title_var)

    # Status dropdown
    status_label = tk.Label(todo_frame, text="Status:")
    status_options = ["ToDo", "In Progress", "Completed"]
    status_var.set(status_options[0])
    status_dropdown = tk.OptionMenu(todo_frame, status_var, *status_options)

    # Priority dropdown
    priority_label = tk.Label(todo_frame, text="Priority")
    priority_options = ["Low", "Medium", "High"]
    priority_var.set(priority_options[1])
    priority_dropdown = tk.OptionMenu(todo_frame, priority_var, *priority_options)

    # Submit button now passes references to StringVars
    submit_button = tk.Button(todo_frame, text="Submit", command=lambda: (handle_submit(title_var, status_var, priority_var), clear_frame(todo_frame))
    )

    # Layout
    title_label.grid(row=0, column=0)
    title_entry.grid(row=0, column=1)

    status_label.grid(row=1, column=0)
    status_dropdown.grid(row=1, column=1)

    priority_label.grid(row=2, column=0)
    priority_dropdown.grid(row=2, column=1)

    submit_button.grid(row=3, column=0, columnspan=2, pady=5)


# Main Window
root = tk.Tk()
root.title("Your ToDos!")
root.geometry("1280x960")
root.resizable(False, False)
create_todo_button = tk.Button(root, text="Create Todo", command=create_todo)
create_todo_button.pack(padx=20, pady=20)

root.mainloop()
