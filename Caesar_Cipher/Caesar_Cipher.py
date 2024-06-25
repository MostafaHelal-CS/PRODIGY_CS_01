import customtkinter as ctk

# Global variable to store the encrypted message
encrypted_message = ""

def caesar_cipher(text, shift, encrypt=True):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            shift_amount = shift if encrypt else -shift
            if char.isupper():
                result += chr((ord(char) + shift_amount - 65) % 26 + 65)
            else:
                result += chr((ord(char) + shift_amount - 97) % 26 + 97)
        else:
            result += char
    return result

def process_text():
    global encrypted_message
    text = text_entry.get()
    shift = int(shift_entry.get())
    if operation.get() == "encrypt":
        encrypted_message = caesar_cipher(text, shift, encrypt=True)
        result_label.configure(text=f"Encrypted Text: {encrypted_message}")
    elif operation.get() == "decrypt":
        if encrypted_message:
            decrypted_text = caesar_cipher(encrypted_message, shift, encrypt=False)
            result_label.configure(text=f"Decrypted Text: {decrypted_text}")
        else:
            result_label.configure(text="No encrypted message to decrypt")

# Create the main window
root = ctk.CTk()
root.title("Caesar Cipher")
root.geometry("500x400")

# Set the appearance mode and color theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Create and place the widgets
operation = ctk.StringVar(value="encrypt")

ctk.CTkLabel(root, text="Select operation:",font=("Cursive", 16, "bold")).pack(anchor="nw", pady=5, padx=5)
encrypt_radio = ctk.CTkRadioButton(root, text="Encrypt", variable=operation, value="encrypt")
encrypt_radio.pack(pady=5)
decrypt_radio = ctk.CTkRadioButton(root, text="Decrypt", variable=operation, value="decrypt")
decrypt_radio.pack( pady=5)

ctk.CTkLabel(root, text="Enter text:",font=("Cursive", 16, "bold")).pack(anchor="nw", pady=5, padx=5)
text_entry = ctk.CTkEntry(root, width=300 , height=50)
text_entry.pack(pady=5)

ctk.CTkLabel(root, text="Enter shift value:",font=("Cursive", 16, "bold")).pack(anchor="nw", pady=5, padx=5)
shift_entry = ctk.CTkEntry(root, width=50)
shift_entry.pack(pady=5)

process_button = ctk.CTkButton(root, text="Process", command=process_text)
process_button.pack(pady=10)

result_label = ctk.CTkLabel(root, text="Result will be shown here",font=("Cursive", 16, "bold"))
result_label.pack(pady=10)

# Start the GUI event loop
root.mainloop()
