import json
import os
from datetime import datetime, timedelta
import threading
import time

class TaskAutomation:
    """Handles task management and reminders"""
    
    def __init__(self, filename='tasks.json'):
        """Initialize task automation"""
        self.filename = filename
        self.tasks = self.load_tasks()
        self.reminders = []
        self.reminder_thread = None
        self.running = True
    
    def load_tasks(self):
        """Load tasks from JSON file"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    return json.load(f)
            except:
                return []
        return []
    
    def save_tasks(self):
        """Save tasks to JSON file"""
        with open(self.filename, 'w') as f:
            json.dump(self.tasks, f, indent=4)
    
    def add_task(self, task_name, priority="normal"):
        """Add a new task"""
        task = {
            'name': task_name,
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'completed': False,
            'priority': priority
        }
        self.tasks.append(task)
        self.save_tasks()
        return f"Task '{task_name}' added"
    
    def get_tasks(self):
        """Get all tasks"""
        return self.tasks
    
    def complete_task(self, task_index):
        """Mark a task as completed"""
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]['completed'] = True
            self.save_tasks()
            return f"Task '{self.tasks[task_index]['name']}' completed"
        return "Task not found"
    
    def delete_task(self, task_index):
        """Delete a task"""
        if 0 <= task_index < len(self.tasks):
            task_name = self.tasks[task_index]['name']
            self.tasks.pop(task_index)
            self.save_tasks()
            return f"Task '{task_name}' deleted"
        return "Task not found"
    
    def get_pending_tasks(self):
        """Get all pending (incomplete) tasks"""
        return [task for task in self.tasks if not task.get('completed', False)]
    
    def set_reminder(self, reminder_text, seconds):
        """Set a reminder for a specific time"""
        reminder_time = datetime.now() + timedelta(seconds=seconds)
        reminder = {
            'text': reminder_text,
            'time': reminder_time.strftime('%Y-%m-%d %H:%M:%S'),
            'triggered': False
        }
        self.reminders.append(reminder)
        return f"Reminder set for {seconds} seconds"
    
    def get_reminders(self):
        """Get all active reminders"""
        return [r for r in self.reminders if not r.get('triggered', False)]
    
    def check_reminders(self):
        """Check if any reminders need to be triggered"""
        current_time = datetime.now()
        for reminder in self.reminders:
            if not reminder.get('triggered', False):
                reminder_time = datetime.strptime(reminder['time'], '%Y-%m-%d %H:%M:%S')
                if current_time >= reminder_time:
                    reminder['triggered'] = True
                    return reminder['text']
        return None
    
    def clear_completed_tasks(self):
        """Remove all completed tasks"""
        initial_count = len(self.tasks)
        self.tasks = [task for task in self.tasks if not task.get('completed', False)]
        self.save_tasks()
        removed = initial_count - len(self.tasks)
        return f"Removed {removed} completed tasks"
