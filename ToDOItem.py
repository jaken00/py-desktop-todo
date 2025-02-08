

class Todo:
    def __init__(self, id, title, status, priority):
        self.id = id
        self.title = title
        self.status = status
        self.priority = priority
        
    
    def update_status(self, new_status):
        self.status = new_status
        
    def change_priority(self, new_priority):
        self.priority = new_priority