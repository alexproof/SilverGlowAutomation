import tkinter as tk
from tkinter import scrolledtext, messagebox
import re

def process_text():
    input_text = text_box.get("1.0", "end-1c")
    lines = input_text.split('\n')

    # Process lines to remove lines without "L-", "GRAND TOTAL", "TU", and "TN"
    processed_lines = [line for line in lines if any(keyword in line for keyword in ["L-", "GRAND TOTAL", "TU", "TN"])]

    # Remove lines with just numbers
    processed_lines = [line for line in processed_lines if not re.match(r'^\d+$', line)]

    processed_text = '\n'.join(processed_lines)

    text_box.delete("1.0", "end")
    text_box.insert("1.0", processed_text)

def save_text():
    text_to_save = text_box.get("1.0", "end-1c")
    try:
        with open('PODConverter.txt', 'w') as file:
            file.write(text_to_save)
        messagebox.showinfo("Success", "Processed text saved successfully as 'PODConverter.txt'")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while saving the text: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("Text Processor")
root.geometry("700x1000")

# Create a scrolled text widget
text_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=40)
text_box.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# Create a button to process text and save it
process_button = tk.Button(root, text="Convert Text", command=process_text)
process_button.pack()
save_button = tk.Button(root, text="Save Text", command=save_text)
save_button.pack()

# Start the GUI main loop
root.mainloop()
