import itertools
import threading
import tkinter as tk
from tkinter import ttk, scrolledtext

class PasswordGenerator:
    def __init__(self, possible_combination: int, combination_type: int, num_threads: int):
        self.possible_combination = possible_combination
        self.combination_type = combination_type
        self.special = '!"#$%&\'()*+,-. /:;?@[]^_`{|}~'
        self.numeric = '0123456789'
        self.alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.get_character = ""
        self.num_threads = num_threads

    def generate_get_character(self):
        if self.combination_type == 1:
            self.get_character = self.numeric + self.alphabet
        elif self.combination_type == 2:
            self.get_character = self.numeric
        elif self.combination_type == 3:
            self.get_character = self.alphabet
        elif self.combination_type == 4:
            self.get_character = self.special
        elif self.combination_type == 5:
            self.get_character = self.special + self.numeric
        elif self.combination_type == 6:
            self.get_character = self.special + self.numeric + self.alphabet
        else:
            raise ValueError("Invalid combination_type")

    def generate_password(self, start: int, end: int, output):
        for x in itertools.product(*([self.get_character] * self.possible_combination))[start:end]:
            output.append(''.join(x))

    def generate_password_thread(self, thread_id, output):
        start = thread_id * self.total_combinations // self.num_threads
        end = (thread_id + 1) * self.total_combinations // self.num_threads
        passwords = []
        self.generate_password(start, end, passwords)
        output += passwords

    def generate_passwords(self):
        self.generate_get_character()
        self.total_combinations = len(self.get_character) ** self.possible_combination
        threads = []
        output = []
        for i in range(self.num_threads):
            threads.append(threading.Thread(target=self.generate_password_thread, args=(i, output)))
            threads[i].start()

        for i in range(self.num_threads):
            threads[i].join()

        return output

class PasswordGeneratorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("500x400")

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.root, text="Possible Combination:").grid(column=0, row=0, padx=10, pady=5, sticky='W')
        self.possible_combination = ttk.Entry(self.root)
        self.possible_combination.grid(column=1, row=0, padx=10, pady=5)

        ttk.Label(self.root, text="Combination Type (1-6):").grid(column=0, row=1, padx=10, pady=5, sticky='W')
        self.combination_type = ttk.Entry(self.root)
        self.combination_type.grid(column=1, row=1, padx=10, pady=5)

        ttk.Label(self.root, text="Number of Threads:").grid(column=0, row=2, padx=10, pady=5, sticky='W')
        self.num_threads = ttk.Entry(self.root)
        self.num_threads.grid(column=1, row=2, padx=10, pady=5)

        self.generate_button = ttk.Button(self.root, text="Generate Passwords", command=self.generate_passwords)
        self.generate_button.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

        self.output_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=50, height=15)
        self.output_area.grid(column=0, row=4, columnspan=2, padx=10, pady=10)

    def generate_passwords(self):
        try:
            possible_combination = int(self.possible_combination.get())
            combination_type = int(self.combination_type.get())
            num_threads = int(self.num_threads.get())
        except ValueError:
            self.output_area.insert(tk.END, "Invalid input! Please enter numeric values.\n")
            return

        generator = PasswordGenerator(possible_combination, combination_type, num_threads)
        passwords = generator.generate_passwords()

        self.output_area.delete(1.0, tk.END)
        for password in passwords:
            self.output_area.insert(tk.END, f"{password}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorGUI(root)
    root.mainloop()
