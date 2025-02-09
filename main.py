import tkinter as tk
from ToDOItem import Todo

#The ID needs to be loaded via a settigns file that also holds preivous TODOs most likely JSON FIle
id = 1

def handle_submit(frame):
    pass
def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()
        
        frame.pack_forget



def create_todo():
    
    todo_frame = tk.Frame(root)
    todo_frame.pack(pady=5, padx=10, fill="x")
    
    title_var = tk.StringVar()
    status_var = tk.StringVar()
    priority_var = tk.StringVar()
    
    title_label = tk.Label(todo_frame, text="Title")
    title_entry = tk.Entry(todo_frame, textvariable=title_var)
    
    #Prob switch this to a dropdown
    status_label = tk.Label(todo_frame, text="Status:")
    status_options = ["ToDo", "In Prgrogress", "Completed"]
    status_var.set(status_options[0])
    status_dropdown = tk.OptionMenu(todo_frame, status_var, *status_options)
    
    #Switch this to a dropdown as well
    priority_label = tk.Label(todo_frame, text="Priority")
    priority_options = ["Low", "Medium", "High"]
    priority_var.set(priority_options[1])
    priority_entry = tk.OptionMenu(todo_frame, priority_var, *priority_options)
    
    submit_button = tk.Button(todo_frame, text="Submit", command=lambda: [handle_submit(todo_frame), clear_frame(todo_frame)])
    
    
    title_label.grid(row=0, column=0)
    title_entry.grid(row=0, column=1)

    status_label.grid(row=1, column=0)
    status_dropdown.grid(row=1, column=1)

    priority_label.grid(row=2, column=0)
    priority_entry.grid(row=2, column=1)
    
    submit_button.grid(row=3, column=0)

    
    #Add sumbit button that then creates a new todo and displays to the screen ( new frame )
    #Also unpack? the newly created inputs (using a try catch statement)


root = tk.Tk()
root.title("Your ToDos!")

create_todo = tk.Button(root, text="Create Todo", command=create_todo)
create_todo.pack(padx=20, pady=20)

root.mainloop()






'''
import asyncio
import signal

from desktop_notifier import DesktopNotifier, Urgency, Button, ReplyField, DEFAULT_SOUND


async def main() -> None:
    notifier = DesktopNotifier(
        app_name="Sample App",
        notification_limit=10,
    )

    await notifier.send(
        title="Julius Caesar",
        message="Et tu, Brute?",
        urgency=Urgency.Critical,
        buttons=[
            Button(
                title="Mark as read",
                on_pressed=lambda: print("Marked as read"),
            )
        ],
        reply_field=ReplyField(
            on_replied=lambda text: print("Brutus replied:", text),
        ),
        on_clicked=lambda: print("Notification clicked"),
        on_dismissed=lambda: print("Notification dismissed"),
        sound=DEFAULT_SOUND,
    )

    # Run the event loop forever to respond to user interactions with the notification.
    stop_event = asyncio.Event()
    loop = asyncio.get_running_loop()

    loop.add_signal_handler(signal.SIGINT, stop_event.set)
    loop.add_signal_handler(signal.SIGTERM, stop_event.set)

    await stop_event.wait()

asyncio.run(main())


'''