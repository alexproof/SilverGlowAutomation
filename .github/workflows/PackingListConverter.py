import tkinter as tk
from tkinter import scrolledtext, messagebox
import re

def process_text():
    input_text = text_box.get("1.0", "end-1c")
    lines = input_text.split('\n')
    
    # Process lines according to specified rules
    processed_lines = []
    
    for line in lines:
        # Remove lines without "PCE"
        if "PCE" not in line:
            continue
        
        # Remove "KGS," "P/O," "NO.," and "PCE" text
        line = re.sub(r'KGS|P/O|NO\.|PCE', '', line)
        
        # Remove numbers with "." except those with "L" text
        line = re.sub(r'(?<![L\d])\d+\.\d+(?![L\d])', '', line)
        
        # Check if this line has a range to duplicate
        if '-' in line:
            match = re.search(r'(\d+)-(\d+)', line)
            if match:
                start, end = map(int, match.groups())
                for i in range(start, end + 1):
                    processed_lines.append(line.replace(f'-{start}-', f'-{i}-@'))
            else:
                processed_lines.append(line)
        else:
            processed_lines.append(line)
    
    # Remove excess line breaks and spacing
    processed_text = '\n'.join(processed_lines)
    processed_text = re.sub(r'\n{3,}', '\n\n', processed_text)  # Replace 3 or more consecutive line breaks with 2
    processed_text = re.sub(r'\n\n', '\n', processed_text)      # Remove any remaining double line breaks
    processed_text = re.sub(r'\n\n$', '\n', processed_text)     # Remove trailing double line breaks
    processed_text = processed_text.strip()                     # Remove leading/trailing whitespace
    
    text_box.delete("1.0", "end")
    text_box.insert("1.0", processed_text)

def save_text():
    text_to_save = text_box.get("1.0", "end-1c")
    try:
        with open('ConvertedLines.txt', 'w') as file:
            file.write(text_to_save)
        messagebox.showinfo("Success", "Processed text saved successfully as 'ConvertedLines.txt'")
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
