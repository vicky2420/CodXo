import datetime
import time
import tkinter as tk
from tkinter import messagebox, filedialog
from threading import Thread
import pickle

# Class representing the alarm clock application
class AlarmClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Alarm Clock")

        # List to store alarms with their details
        self.alarms = []

        # variable to track if alarms are paused
        self.paused = False

        # Default alarm sound file
        self.current_sound = 'alarm_sound.mp3'  

        # Load exixting alarms from file if available
        self.load_alarms()

        # GUI elements for entering alarm time
        self.time_label = tk.Label(root, text="Enter time (HH:MM:SS)", font=("Helvetica", 12))
        self.time_label.pack(pady=10)

        self.time_entry = tk.Entry(root, font=("Helvetica", 12))
        self.time_entry.pack(pady=5)

        # GUI elements for entering alarm Description 
        self.desc_label = tk.Label(root, text="Alarm Description", font=("Helvetica", 12))
        self.desc_label.pack(pady=10)

        self.desc_entry = tk.Entry(root, font=("Helvetica", 12))
        self.desc_entry.pack(pady=5)

        # Checkbox for setting alarm repeat
        self.repeat_var = tk.IntVar()
        self.repeat_checkbox = tk.Checkbutton(root, text="Repeat Daily", variable=self.repeat_var, font=("Helvetica", 12))
        self.repeat_checkbox.pack(pady=5)

        # Button to set a new alarm
        self.add_alarm_button = tk.Button(root, text="Set Alarm", command=self.add_alarm, font=("Helvetica", 12))
        self.add_alarm_button.pack(pady=10)

        # Label and Listbox to display all set alarms
        self.alarm_list_label = tk.Label(root, text="Alarms:", font=("Helvetica", 12))
        self.alarm_list_label.pack(pady=10)

        self.alarm_listbox = tk.Listbox(root, font=("Helvetica", 12))
        self.alarm_listbox.pack(pady=5)

        # Button to remove selected alarm from the list 
        self.remove_alarm_button = tk.Button(root, text="Remove Selected Alarm", command=self.remove_alarm, font=("Helvetica", 12))
        self.remove_alarm_button.pack(pady=10)

        # Button to pause and resume alarm checking
        self.pause_resume_button = tk.Button(root, text="Pause Alarms", command=self.pause_resume_alarms, font=("Helvetica", 12))
        self.pause_resume_button.pack(pady=10)

        # Button to snooze the current alarm
        self.snooze_button = tk.Button(root, text="Snooze", command=self.snooze_alarm, font=("Helvetica", 12))
        self.snooze_button.pack(pady=10)

        # Label to display the current time, updated every second
        self.current_time_label = tk.Label(root, text="", font=("Helvetica", 12))
        self.current_time_label.pack(pady=10)
        self.update_current_time()

        # Start a separate thread to continuously check for alarms
        self.check_alarms_thread = Thread(target=self.check_alarms)
        self.check_alarms_thread.daemon = True
        self.check_alarms_thread.start()

    def add_alarm(self):
        # Retrieve the entered alarm time and description
        alarm_time = self.time_entry.get()
        description = self.desc_entry.get()
        repeat = bool(self.repeat_var.get())
        try:
            # Validate the time format

            datetime.datetime.strptime(alarm_time, "%H:%M:%S")

            # Add alarm to the list and display in the listbox

            self.alarms.append((alarm_time, description, repeat))
            self.alarm_listbox.insert(tk.END, f"{alarm_time} - {description}")

            # Clear the entry fields
            self.time_entry.delete(0, tk.END)
            self.desc_entry.delete(0, tk.END)
            self.repeat_var.set(0)
            self.save_alarms()
        except ValueError:
            # Show error if the time format is invalid

            messagebox.showerror("Invalid Time Format!", "Please enter time in HH:MM:SS format")

    def remove_alarm(self):
        # Get the selected alarm index
        selected_alarm_index = self.alarm_listbox.curselection()

        if selected_alarm_index:
            # Remove the alarm from the list and listbox
            del self.alarms[selected_alarm_index[0]]
            self.alarm_listbox.delete(selected_alarm_index)
            self.save_alarms()
        else:
            # Show error if no alarm is selected
            messagebox.showerror("No Selection", "Please select an alarm to remove")

    def pause_resume_alarms(self):
        # Toggle the paused state and update button text
        if self.paused:
            self.paused = False
            self.pause_resume_button.config(text="Pause Alarms")
        else:
            self.paused = True
            self.pause_resume_button.config(text="Resume Alarms")

    def snooze_alarm(self):
        # Set a new alarm for 5 minutes later
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        snooze_time = (datetime.datetime.now() + datetime.timedelta(minutes=5)).strftime("%H:%M:%S")
        self.alarms.append((snooze_time, "Snooze", False))
        self.alarm_listbox.insert(tk.END, f"{snooze_time} - Snooze")
        self.save_alarms()

    def check_alarms(self):
        while True:
            if not self.paused:
                current_time = datetime.datetime.now().strftime("%H:%M:%S")
                for alarm in self.alarms:
                    alarm_time, description, repeat = alarm
                    if current_time == alarm_time:

                        # Show notification message box
                        messagebox.showinfo("Alarm", f"Time: {alarm_time}\nDescription: {description}")

                        # Reschedule repeating alarm for the next day
                        if repeat:
                            next_day = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%H:%M:%S")
                            self.alarms.append((next_day, description, repeat))

                        # Remove the triggered alarm from the list    
                        self.alarms.remove(alarm)
                        self.update_alarm_listbox()
                        self.save_alarms()
            time.sleep(1)

    def update_alarm_listbox(self):
        # Update the listbox with the current alarms
        self.alarm_listbox.delete(0, tk.END)
        for alarm_time, description, repeat in self.alarms:
            self.alarm_listbox.insert(tk.END, f"{alarm_time} - {description}")

    def update_current_time(self):
        # Update the current time display every second
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.current_time_label.config(text="Current Time: " + current_time)
        self.root.after(1000, self.update_current_time)

    def save_alarms(self):
        # Save the alarms list to a file
        with open('alarms.pkl', 'wb') as f:
            pickle.dump(self.alarms, f)

    def load_alarms(self):
        #Load the alarms list from a file
        try:
            with open('alarms.pkl', 'rb') as f:
                self.alarms = pickle.load(f)
        except FileNotFoundError:
        # Initialize an empty list if no file is found    
            self.alarms = []

# Main block to run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = AlarmClock(root)
    root.mainloop()
