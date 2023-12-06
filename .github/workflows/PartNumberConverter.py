import tkinter as tk
from tkinter import scrolledtext, messagebox

def process_text():
    input_text = text_box.get("1.0", "end-1c")
    inside_brackets = False
    processed_lines = []

    for line in input_text.split('\n'):
        line = line.strip()

        for char in line:
            if char == '(':
                inside_brackets = True
                processed_lines.append('[')
            elif char == ')':
                inside_brackets = False
                processed_lines.append(']\n')
            elif inside_brackets:
                processed_lines.append(char)

    cleaned_text = ''.join(processed_lines)
    cleaned_text = cleaned_text.replace('[', '').replace(']', '')

    final_text = '\n'.join([line for line in cleaned_text.split('\n') if not ('.' in line or 'VSP' in line or 'RTF' in line) and line.strip()])

    text_box.delete("1.0", "end")
    text_box.insert("1.0", final_text)

def save_text():
    text_to_save = text_box.get("1.0", "end-1c")
    try:
        with open('converted_text.txt', 'w') as file:
            file.write(text_to_save)
        messagebox.showinfo("Success", "Text saved successfully as 'converted_text.txt'")
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
process_button = tk.Button(root, text="Process Text", command=process_text)
process_button.pack()
save_button = tk.Button(root, text="Save Text", command=save_text)
save_button.pack()

# Start the GUI main loop
root.mainloop()