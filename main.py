import tkinter as tk
from tkinter import messagebox
from ToDOItem import Todo
import sqlite3
import datetime
from tkcalendar import Calendar

'''
TODO: 
 - ADD DATES
 - ADD DUE DATES
 - UPDATE / DELETE TODOs IN THE TABLE
 - PERSISTANCE ACORSS SESSIONS (UI)
 - DESKTOP NOTIFICATIONS
 - POINT SYSTEM?
'''



todo_id = 1
db_conn = None    # DIRECT DB CONNECTION
db_cursor = None  # THE CURSOR

def handle_submit(title_var, status_var, priority_var, date_var):
    global todo_id  
    
    todo_container = tk.Frame(root, bd=2, relief="solid", padx=10, pady=5, bg="#f8f9fa")
    todo_container.pack(pady=10, padx=20, fill="x")
    
    todo_dictionary = {
        "title": title_var.get(),
        "status": status_var.get(),
        "priority": priority_var.get(),
        "date": date_var
    }
    
    print(f"THIS IS THE DATE: {date_var}")
    
    if todo_dictionary["title"] == "":
        messagebox.showerror("Error", "You must enter a title!")
        todo_container.destroy()
        return

    new_todo = Todo(todo_id, todo_dictionary["title"], todo_dictionary["status"], todo_dictionary["priority"])
    todo_id += 1  

    add_task_to_db(new_todo)
    tk.Label(todo_container, text=new_todo.title, font=("Arial", 12, "bold"), bg="#f8f9fa").grid(column=0, row=0, padx=5, pady=5, sticky="w")
    tk.Label(todo_container, text=f"Status: {new_todo.status}", font=("Arial", 10), bg="#f8f9fa").grid(column=1, row=0, padx=5, pady=5)
    tk.Label(todo_container, text=f"Priority: {new_todo.priority}", font=("Arial", 10), bg="#f8f9fa").grid(column=2, row=0, padx=5, pady=5)
    #tk.Label(todo_container, text=f"Date: {todo_dictionary.date}", font=("Arial", 10), bg="#f8f9fa").grid(column=3, row=0, padx=5, pady=5)
    
    delete_button = tk.Button(todo_container, text='Remove', command=lambda: (todo_container.destroy(), delete_todo(new_todo)), bg="#ff6b6b", fg="white", font=("Arial", 10, "bold"))
    edit_button = tk.Button(todo_container, text='Edit', command=lambda: edit_todo(new_todo, todo_container), bg="#4caf50", fg="white", font=("Arial", 10, "bold"))
    
    delete_button.grid(column=3, row=0, padx=5, pady=5)
    edit_button.grid(column=4, row=0, padx=5, pady=5)

def add_task_to_db(todo_item):
    global db_cursor
    
    db_cursor.execute("INSERT INTO tasks (title, priority, status) VALUES (?, ? , ?)", (todo_item.title, todo_item.priority, todo_item.status))
    
    
    data = db_cursor.execute('''SELECT * FROM tasks''')
    commit_table()
    for row in data:
        print(row)

def drop_table(cursor):
    # DROP THE TABLE FOR TESTING PURPOSES
    cursor.execute("DROP TABLE IF EXISTS tasks")

def commit_table():
    global db_conn
    if db_conn:
        db_conn.commit()
    
def edit_todo(todo, todo_container):
    editPopup = tk.Toplevel(root)
    editPopup.title("Edit Todo")
    editPopup.geometry("300x200")
    editPopup.configure(bg="#f8f9fa")
    
    title_var = tk.StringVar(value=todo.title)
    status_var = tk.StringVar(value=todo.status)
    priority_var = tk.StringVar(value=todo.priority)
    
    tk.Label(editPopup, text="Title", bg="#f8f9fa").pack(pady=5)
    title_entry = tk.Entry(editPopup, textvariable=title_var)
    title_entry.pack(pady=5)

    tk.Label(editPopup, text="Status", bg="#f8f9fa").pack(pady=5)
    status_options = ["ToDo", "In Progress", "Completed"]
    status_dropdown = tk.OptionMenu(editPopup, status_var, *status_options)
    status_dropdown.pack(pady=5)

    tk.Label(editPopup, text="Priority", bg="#f8f9fa").pack(pady=5)
    priority_options = ["Low", "Medium", "High"]
    priority_dropdown = tk.OptionMenu(editPopup, priority_var, *priority_options)
    priority_dropdown.pack(pady=5)
    
    def saveChanges():
        todo.title = title_var.get()
        todo.status = status_var.get()
        todo.priority = priority_var.get()

        for widget in todo_container.winfo_children():
            widget.destroy()

        tk.Label(todo_container, text=todo.title, font=("Arial", 12, "bold"), bg="#f8f9fa").grid(column=0, row=0, padx=5, pady=5, sticky="w")
        tk.Label(todo_container, text=f"Status: {todo.status}", font=("Arial", 10), bg="#f8f9fa").grid(column=1, row=0, padx=5, pady=5)
        tk.Label(todo_container, text=f"Priority: {todo.priority}", font=("Arial", 10), bg="#f8f9fa").grid(column=2, row=0, padx=5, pady=5)

        delete_button = tk.Button(todo_container, text='Remove', command=lambda: (todo_container.destroy(), delete_todo(todo)), bg="#ff6b6b", fg="white", font=("Arial", 10, "bold"))
        edit_button = tk.Button(todo_container, text='Edit', command=lambda: edit_todo(todo, todo_container), bg="#4caf50", fg="white", font=("Arial", 10, "bold"))
        
        delete_button.grid(column=3, row=0, padx=5, pady=5)
        edit_button.grid(column=4, row=0, padx=5, pady=5)
        
        editPopup.destroy()
    
    confirm_button = tk.Button(editPopup, text="Confirm", command=saveChanges, bg="#4caf50", fg="white")
    confirm_button.pack(pady=10)

def delete_todo(todo):
    del todo

def create_todo():
    todo_frame = tk.Frame(root, bd=2, relief="ridge", padx=10, pady=10)
    todo_frame.pack(pady=10, padx=20, fill="x")
    
    title_var = tk.StringVar()
    status_var = tk.StringVar(value="ToDo")
    priority_var = tk.StringVar(value="Medium")
    
    
    tk.Label(todo_frame, text="Title:", font=("Arial", 12, "bold")).grid(row=0, column=0, padx=5, pady=5, sticky="w")
    tk.Entry(todo_frame, textvariable=title_var, width=30).grid(row=0, column=1, padx=5, pady=5)

    tk.Label(todo_frame, text="Status:", font=("Arial", 12, "bold")).grid(row=1, column=0, padx=5, pady=5, sticky="w")
    tk.OptionMenu(todo_frame, status_var, "ToDo", "In Progress", "Completed").grid(row=1, column=1, padx=5, pady=5)

    tk.Label(todo_frame, text="Priority:", font=("Arial", 12, "bold")).grid(row=2, column=0, padx=5, pady=5, sticky="w")
    tk.OptionMenu(todo_frame, priority_var, "Low", "Medium", "High").grid(row=2, column=1, padx=5, pady=5)
    
    # TODO CHANGE THE START OF THE CALANDER TO DATE.TODAY()
    
    tk.Label(todo_frame, text="Due Date:", font=("Arial", 12, "bold")).grid(row=3, column=0, padx=5, pady=5, sticky="w")
    calendar = Calendar(todo_frame, selectmode = 'day', year = 2025, month = 1, day = 20)
    calendar.grid(row=3, column=1,padx=5, pady=5)
    
    tk.Button(todo_frame, text="Submit", command=lambda: (handle_submit(title_var, status_var, priority_var, calendar.get_date()), todo_frame.destroy()), bg="#2196F3", fg="white", font=("Arial", 10, "bold")).grid(row=4, column=0, columnspan=2, pady=10)

def init_table():
    global db_conn, db_cursor
    db_conn = sqlite3.connect('todo.db')
    db_cursor = db_conn.cursor()
    db_cursor.execute('DROP TABLE IF EXISTS tasks')  # Remove this after testing
    db_cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, title TEXT, priority TEXT, status TEXT)''')

def main():
    global root
    init_table()  # Initialize database

    root = tk.Tk()
    root.title("Your ToDos!")
    root.geometry("600x600")
    root.configure(bg="#e9ecef")

    create_todo_button = tk.Button(root, text="Create Todo", command=create_todo, bg="#2196F3", fg="white", font=("Arial", 12, "bold"))
    create_todo_button.pack(padx=20, pady=20)

    root.mainloop()
    db_conn.close()


if __name__ == "__main__":
    main()