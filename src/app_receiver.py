import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from receiver import decrypt_dhies, gen_key

# Define encryption, decryption, and key generation functions





def start_decryption():
    em_path = em_entry.get()
    sk_path = sk_entry.get()
    if not em_path or not sk_path:
        messagebox.showerror("Error", "Please select both files for decryption")
    else:
        m = decrypt_dhies(em_path=em_path, sk_path=sk_path)
        if m == 'BAD' : 
            messagebox.showerror("Error", "Validate Failed")
        else:
            messagebox.showinfo("Success", "Decryption complete")

def start_gen_key():
    gen_key()
    messagebox.showinfo("Success", "Gen key complete")

# Update the form based on selected action (Encrypt/Decrypt/Gen Key)
def update_form():
    if action_var.get() == "decrypt":
        decrypt_frame.grid(row=1, column=0, columnspan=3, padx=20, pady=10)
        action_button.config(text="Decrypt", command=start_decryption)
    else:  # Gen Key selected
        decrypt_frame.grid_forget()
        action_button.config(text="Generate Key", command=start_gen_key)
        

# Create the main GUI window
root = tk.Tk()
root.title("DHIES Decryption")
root.geometry("500x300")
root.configure(bg="#f0f8ff")  # Light blue background

# Apply a modern theme to `ttk` widgets
style = ttk.Style()
style.theme_use("clam")

# Define colors
bg_color = "#f0f8ff"  # light blue for background
button_color = "#4682B4"  # steel blue for buttons
text_color = "#ffffff"  # white for button text

# Frame for action selection with styled buttons
action_var = tk.StringVar(value="decrypt")
action_frame = ttk.Frame(root, padding="10")
action_frame.grid(row=0, column=0, columnspan=3)
action_frame.configure(style="Custom.TFrame")

# Styled radio buttons
decrypt_radio = ttk.Radiobutton(action_frame, text="Decrypt", variable=action_var, value="decrypt", command=update_form)
gen_key_radio = ttk.Radiobutton(action_frame, text="Gen Key", variable=action_var, value="gen_key", command=update_form)
decrypt_radio.grid(row=0, column=1, padx=10)
gen_key_radio.grid(row=0, column=2, padx=10)

# Configure background for labels and radio buttons
style.configure("Custom.TRadiobutton", background=bg_color)
style.configure("Custom.TLabelframe.Label", background=bg_color, foreground="black", font=("Helvetica", 10, "bold"))

decrypt_radio.configure(style="Custom.TRadiobutton")
gen_key_radio.configure(style="Custom.TRadiobutton")

# Frame for decryption parameters
decrypt_frame = ttk.LabelFrame(root, text="Decryption Parameters", padding="10", style="Custom.TLabelframe")
em_label = tk.Label(decrypt_frame, text="Encrypted Message Path:", bg=bg_color)
em_label.grid(row=0, column=0, sticky="e", padx=5, pady=5)
em_entry = ttk.Entry(decrypt_frame, width=40)
em_entry.grid(row=0, column=1, padx=5, pady=5)
em_browse = ttk.Button(decrypt_frame, text="Browse", command=lambda: em_entry.insert(0, filedialog.askopenfilename()), style="Custom.TButton")
em_browse.grid(row=0, column=2, padx=5, pady=5)

sk_label = tk.Label(decrypt_frame, text="Secret Key Path:", bg=bg_color)
sk_label.grid(row=1, column=0, sticky="e", padx=5, pady=5)
sk_entry = ttk.Entry(decrypt_frame, width=40)
sk_entry.grid(row=1, column=1, padx=5, pady=5)
sk_browse = ttk.Button(decrypt_frame, text="Browse", command=lambda: sk_entry.insert(0, filedialog.askopenfilename()), style="Custom.TButton")
sk_browse.grid(row=1, column=2, padx=5, pady=5)

# Main action button
action_button = ttk.Button(root, text="Decrypt", command=start_decryption, style="Custom.TButton")
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
