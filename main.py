import tkinter as tk
from ToDOItem import Todo

#The ID needs to be loaded via a settigns file that also holds preivous TODOs most likely JSON FIle
id = 1

def create_todo():
    title_var = tk.StringVar()
    status_var = tk.StringVar()
    priority_var = tk.StringVar()
    
    title_label = tk.Label(root, text="Title")
    title_entry = tk.Entry(root, textvariable=title_var)
    
    #Prob switch this to a dropdown
    status_label = tk.Label(root, text="Current Status")
    status_entry = tk.Entry(root, textvariable=status_var)
    
    #Switch this to a dropdown as well
    priority_label = tk.Label(root, text="Priority")
    priority_entry = tk.Entry(root, textvariable=priority_var)
    
    title_label.grid(row=0, column=0)
    title_entry.grid(row=0, column=1)
    status_label.grid(row=1, column=1)
    status_entry.grid(row=1, column=1)
    priority_label.grid(row=2, column=2)
    priority_entry.grid(row=2, column=1)
    
    #Need to update the main scren byu adding a "Frame" Into this to then update inside of ROot


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