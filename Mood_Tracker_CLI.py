
# Task 5: Enhance the CRUD application to store task data persistently using file I/O.
# 😄 Mood Tracker CLI 

import os
from datetime import datetime

# Define MoodEntry class
class MoodEntry:
    def __init__(self, id, date, mood, trigger, note):
        self.id = id
        self.date = date
        self.mood = mood
        self.trigger = trigger
        self.note = note

    def to_string(self):
        return f"{self.id}|{self.date}|{self.mood}|{self.trigger}|{self.note}"

    @staticmethod
    def from_string(data_line):
        parts = data_line.strip().split("|")
        return MoodEntry(int(parts[0]), parts[1], parts[2], parts[3], parts[4])


# 🗂️ Global Variables
mood_entries = []
filename = "mood_logs.txt"
next_id = 1


# 📥 Load moods from file
def load_data():
    global next_id
    if not os.path.exists(filename):
        return
    with open(filename, "r") as file:
        for line in file:
            entry = MoodEntry.from_string(line)
            mood_entries.append(entry)
            next_id = max(next_id, entry.id + 1)


# 💾 Save moods to file
def save_data():
    with open(filename, "w") as file:
        for entry in mood_entries:
            file.write(entry.to_string() + "\n")


# ➕ Add a new mood
def add_mood():
    global next_id
    print("\n-- Log New Mood --")
    mood = input("How do you feel? (e.g., Happy 😊, Anxious 😟): ")
    trigger = input("What triggered this mood?: ")
    note = input("Write a short note (optional): ")
    date = datetime.now().strftime("%Y-%m-%d")
    entry = MoodEntry(next_id, date, mood, trigger, note)
    mood_entries.append(entry)
    next_id += 1
    save_data()
    print("✅ Mood log added!")


# 📖 View all moods
def view_moods():
    if not mood_entries:
        print("\nNo mood logs found.")
        return
    print("\n-- All Mood Logs --")
    for entry in mood_entries:
        print(f"\nID: {entry.id}\nDate: {entry.date}\nMood: {entry.mood}\nTrigger: {entry.trigger}\nNote: {entry.note}")


# ✏️ Update mood log
def update_mood():
    view_moods()
    try:
        uid = int(input("\nEnter ID of the mood log to update: "))
        for entry in mood_entries:
            if entry.id == uid:
                entry.mood = input("New Mood: ")
                entry.trigger = input("New Trigger: ")
                entry.note = input("New Note: ")
                save_data()
                print("✅ Mood updated.")
                return
        print("❌ ID not found.")
    except ValueError:
        print("❌ Invalid input.")


# ❌ Delete mood log
def delete_mood():
    view_moods()
    try:
        uid = int(input("\nEnter ID of the mood log to delete: "))
        for entry in mood_entries:
            if entry.id == uid:
                mood_entries.remove(entry)
                save_data()
                print("🗑️ Mood log deleted.")
                return
        print("❌ ID not found.")
    except ValueError:
        print("❌ Invalid input.")


# 🧭 Main Menu
def main():
    load_data()
    while True:
        print("\n======= 🧠 Mood Tracker CLI =======")
        print("1. Add Mood")
        print("2. View Mood Logs")
        print("3. Update Mood Log")
        print("4. Delete Mood Log")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_mood()
        elif choice == "2":
            view_moods()
        elif choice == "3":
            update_mood()
        elif choice == "4":
            delete_mood()
        elif choice == "5":
            print("👋 Goodbye! Stay mindful.")
            break
        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    main()
