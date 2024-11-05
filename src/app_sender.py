import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from sender import encrypt_dhies, gen_key

# Define encryption, decryption, and key generation functions

def generate_key():
    gen_key()
    messagebox.showinfo("Success", "Key generation complete")

# Function to handle "Encrypt" button click
def start_encryption():
    m_path = m_entry.get()
    pk_path = pk_entry.get()
    sk_path = sk_entry.get()
    if not m_path or not pk_path:
        messagebox.showerror("Error", "Please select both files for encryption")
    else:
        print(m_path)
        print(pk_path)
        encrypt_dhies(m_path=m_path, pk_path=pk_path, sk_path=sk_path)
        messagebox.showinfo("Success", "Encryption complete")

# Function to handle "Decrypt" button click
# Update the form based on selected action (Encrypt/Decrypt/Gen Key)
def update_form():
    if action_var.get() == "encrypt":
        encrypt_frame.grid(row=1, column=0, columnspan=3, padx=20, pady=10)
        action_button.config(text="Encrypt", command=start_encryption)
    else:  # Gen Key selected
        encrypt_frame.grid_forget()
        action_button.config(text="Generate Key", command=generate_key)

# Create the main GUI window
root = tk.Tk()
root.title("DHIES Encryption")
root.geometry("650x300")
root.configure(bg="#f0f8ff")  # Light blue background

# Apply a modern theme to `ttk` widgets
style = ttk.Style()
style.theme_use("clam")

# Define colors
bg_color = "#f0f8ff"  # light blue for background
button_color = "#4682B4"  # steel blue for buttons
text_color = "#ffffff"  # white for button text

# Frame for action selection with styled buttons
action_var = tk.StringVar(value="encrypt")
action_frame = ttk.Frame(root, padding="10")
action_frame.grid(row=0, column=0, columnspan=3)
action_frame.configure(style="Custom.TFrame")

# Styled radio buttons
encrypt_radio = ttk.Radiobutton(action_frame, text="Encrypt", variable=action_var, value="encrypt", command=update_form)
gen_key_radio = ttk.Radiobutton(action_frame, text="Gen Key", variable=action_var, value="gen_key", command=update_form)
encrypt_radio.grid(row=0, column=0, padx=10)
gen_key_radio.grid(row=0, column=2, padx=10)

# Configure background for labels and radio buttons
style.configure("Custom.TRadiobutton", background=bg_color)
style.configure("Custom.TLabelframe.Label", background=bg_color, foreground="black", font=("Helvetica", 10, "bold"))

encrypt_radio.configure(style="Custom.TRadiobutton")
gen_key_radio.configure(style="Custom.TRadiobutton")

# Frame for encryption parameters
encrypt_frame = ttk.LabelFrame(root, text="Encryption Parameters", padding="10", style="Custom.TLabelframe")
m_label = tk.Label(encrypt_frame, text="Plaintext", bg=bg_color)
m_label.grid(row=0, column=0, sticky="e", padx=5, pady=5)
m_entry = ttk.Entry(encrypt_frame, width=40)
m_entry.grid(row=0, column=1, padx=5, pady=5)
m_browse = ttk.Button(encrypt_frame, text="Browse", command=lambda: m_entry.insert(0, filedialog.askopenfilename()), style="Custom.TButton")
m_browse.grid(row=0, column=2, padx=5, pady=5)

pk_label = tk.Label(encrypt_frame, text="Ephermal Public Key ", bg=bg_color)
pk_label.grid(row=1, column=0, sticky="e", padx=5, pady=5)
pk_entry = ttk.Entry(encrypt_frame, width=40)
pk_entry.grid(row=1, column=1, padx=5, pady=5)
pk_browse = ttk.Button(encrypt_frame, text="Browse", command=lambda: pk_entry.insert(0, filedialog.askopenfilename()), style="Custom.TButton")
pk_browse.grid(row=1, column=2, padx=5, pady=5)

sk_label = tk.Label(encrypt_frame, text="Secret Key", bg=bg_color)
sk_label.grid(row=2, column=0, sticky="e", padx=5, pady=5)
sk_entry = ttk.Entry(encrypt_frame, width=40)
sk_entry.grid(row=2, column=1, padx=5, pady=5)
sk_browse = ttk.Button(encrypt_frame, text="Browse", command=lambda: sk_entry.insert(0, filedialog.askopenfilename()), style="Custom.TButton")
sk_browse.grid(row=2, column=2, padx=5, pady=5)

# Main action button
action_button = ttk.Button(root, text="Encrypt", command=start_encryption, style="Custom.TButton")
action_button.grid(row=2, column=0, columnspan=3, pady=20)

# Style configurations for a custom theme
style.configure("Custom.TButton", background=button_color, foreground=text_color, font=("Helvetica", 10), padding=5)
style.map("Custom.TButton", background=[("active", "#5A9")])

style.configure("Custom.TLabelframe", background=bg_color, foreground="black", font=("Helvetica", 10))
style.configure("TLabel", background=bg_color, font=("Helvetica", 10))
style.configure("TFrame", background=bg_color)

# Initial form setup
update_form()

root.mainloop()
