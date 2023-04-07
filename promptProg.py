import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title("IMAC Prompt")

# Create a list to store the user's answers
answers = []

# Create a list to store the Entry widgets
entries = []


# Func to save the answers to a text file
def save_answers():
    # Prompt the user to choose where to save the file, and what to name it.
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, "w") as f:
            # Write the first 19 questions, and answers to the file with no empty spaces between them
            for i in range(19):
                f.write(f"{questions[i]}: {answers[i].get()}\n")
            # Add 2 empty spaces after the 19th answer
            f.write("\n\n")
            # Write the last 12 questions, and answers to the file with no empty spaces between them
            for i in range(19, 32):
                f.write(f"{questions[i]}: {answers[i].get()}\n")
        # Clear the entry widgets
        for entry in entries:
            entry.delete(0, tk.END)


# List of Questions
questions = [
    "Build",
    "Deploy",
    "Data Retention",
    "Retrieval",
    "RITM No",
    "User's Email Address",
    "New Asset (Delivered)",
    "Cost Center",
    "User Name",
    "User ID",
    "Asset Mfg",
    "Asset Type/Model",
    "Asset Serial Number",
    "Asset Tag",
    "Asset Location",
    "Docking Station",
    "Dock Power Supply",
    "PC Power Supply",
    "Software Installations",
    "Old Asset (Removed)",
    "Cost Center",
    "User Name",
    "User ID",
    "Asset Mfg",
    "Asset Type/Model",
    "Asset Serial Number",
    "Asset Tag",
    "Asset Location",
    "Docking Station",
    "Dock Power Supply",
    "PC Power Supply",
    "Lease Contract"
]

# Create a grid of Label and Entry widgets for the prompts and user input
for i in range(32):
    label = tk.Label(root, text=questions[i], anchor="e", width=20)
    label.grid(row=i, column=-0)
    entry = tk.Entry(root)
    entry.grid(row=i, column=1)
    # Add a StringVar to the list of answers to store the user's input
    answers.append(tk.StringVar())
    entry["textvariable"] = answers[-1]
    # Add the Entry widget to the list of entries
    entries.append(entry)

# Create a Button widget to save the answers when clicked
save_button = tk.Button(root, text="Save Answers", command=save_answers)
save_button.grid(row=32, column=0, columnspan=2)

root.mainloop()
