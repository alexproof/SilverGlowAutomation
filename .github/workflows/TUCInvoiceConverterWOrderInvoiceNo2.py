import tkinter as tk
from tkinter import messagebox
import re

def convert_text():
    input_text_content = input_text.get("1.0", tk.END).splitlines()
    converted_lines = []

    for line in input_text_content:
        line = line.strip()  # Remove leading and trailing spaces
        line = re.sub(r"[^a-zA-Z0-9-]", "", line)  # Keep only alphabets, numbers, and "-"
        
        if ((line.startswith("L") or line.startswith("P")) and ("TU" in line or "TN" in line) or "ORDERNO" in line or "INVOICENO" in line or "INVOICE-NO" in line):
            if line.startswith("L"):
                second_l_index = line.find("L", 1)
                if second_l_index != -1 and line[second_l_index + 1] != "-":
                    line = line[second_l_index:]  # Remove the portion up to the second "L"

            if "ORDERNO" in line:
                line = line.rstrip('-')  # Remove trailing "-" characters
                line = line[:7] + " " + line[7:]  # Add a space after the 7th character

            if "INVOICENO" in line:
                line = line[:9] + " " + line[9:]  # Add a space after the 9th character    

            if "INVOICE-NO" in line:
                line = line[:10] + " " + line[10:]  # Add a space after the 10th character     
            
            if line.startswith("P"):
                second_P_index = line.find("P", 1)
                if second_P_index != -1 and line[second_P_index + 1] != "-":
                    line = line[second_P_index:]  # Remove the portion up to the second "P"

            converted_lines.append(line)

    converted_text = "\n".join(converted_lines)

    input_text.delete("1.0", tk.END)
    input_text.insert(tk.END, converted_text)

def save_file():
    converted_text = input_text.get("1.0", tk.END)
    with open("ConvertedInvoice.txt", "w", encoding="utf-8") as file:
        file.write(converted_text)
    messagebox.showinfo("Saved", "File saved as ConvertedInvoice.txt")

# Create main window
root = tk.Tk()
root.title("Invoice Converter")
root.geometry("700x800")

# Create a scrollable text box that fills the entire window
input_text = tk.Text(root, wrap="word")
input_text.pack(expand=True, fill="both")

# Create convert and save buttons
convert_button = tk.Button(root, text="Convert", command=convert_text)
convert_button.pack(pady=10)

save_button = tk.Button(root, text="Save", command=save_file)
save_button.pack()

# Start GUI
root.mainloop()
