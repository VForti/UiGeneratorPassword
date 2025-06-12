import tkinter as tk
from tkinter import messagebox
from logic import generate_password

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Генератор паролів")

        #checkbox
        self.use_upper = tk.BooleanVar(value=True)
        self.use_lower = tk.BooleanVar(value=True)
        self.use_digits = tk.BooleanVar(value=True)
        self.use_specials = tk.BooleanVar(value=False)

        tk.Checkbutton(root, text="Великі літери", variable=self.use_upper).pack(anchor='w')
        tk.Checkbutton(root, text="Малі літери", variable=self.use_lower).pack(anchor='w')
        tk.Checkbutton(root, text="Цифри", variable=self.use_digits).pack(anchor='w')
        tk.Checkbutton(root, text="Спецсимволи", variable=self.use_specials).pack(anchor='w')

        
        tk.Label(root, text="Довжина пароля:").pack()
        self.length_entry = tk.Entry(root)
        self.length_entry.insert(0, "12")
        self.length_entry.pack()

       
        tk.Button(root, text="Згенерувати пароль", command=self.generate).pack(pady=10)

        tk.Label(root, text="Згенеровані паролі:").pack()
        self.password_list = tk.Listbox(root, width=40)
        self.password_list.pack()


        self.length_error = tk.Label(root, text="Напиши довжину меншу за 1000!!!", fg='red')
        self.length_error.pack_forget() 


    #generator
    def generate(self):
        try:
            length = int(self.length_entry.get())
            if length > 1000:
                self.length_error.pack() 
            else:
                self.length_error.pack_forget()

                password = generate_password(
                    length,
                    self.use_upper.get(),
                    self.use_lower.get(),
                    self.use_digits.get(),
                    self.use_specials.get()
                )
                self.password_list.insert(tk.END, password)

        except ValueError as e:
            messagebox.showerror("Помилка", str(e))
