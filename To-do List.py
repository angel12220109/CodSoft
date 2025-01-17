import tkinter as tk

class TODO:
    def __init__(self, root):
        self.root = root
        self.root.title("TO-DO LIST")
        self.root.geometry('650x410+300+150')

        self.label = tk.Label(self.root, text="TO-DO LIST APP", font='arial 25 bold', width=20, bd=5, bg='orange', fg='black')
        self.label.pack(side='top', fill=tk.BOTH)

        self.label2 = tk.Label(self.root, text="Add Task", font='arial 18 bold', width=10, bd=5, bg='orange', fg='black')
        self.label2.place(x=40, y=54)

        self.label3 = tk.Label(self.root, text="Tasks", font='arial 18 bold', width=10, bd=5, bg='orange', fg='black')
        self.label3.place(x=320, y=54)

        self.main_text = tk.Listbox(self.root, height=9, bd=5, width=23, font='arial 20 italic bold')
        self.main_text.place(x=280, y=100)

        self.text = tk.Text(self.root, height=2, bd=5, width=30, font='arial 10 bold')
        self.text.place(x=20, y=120)

        def add():
            content = self.text.get(1.0, tk.END).strip()
            if content:
                self.main_text.insert(tk.END, content)
                with open('data.txt', 'a') as file:
                    file.write(content + '\n')
                self.text.delete(1.0, tk.END)

        def delete():
            selected_index = self.main_text.curselection()
            if selected_index:
                delete_index = selected_index[0]
                task = self.main_text.get(delete_index)
                self.main_text.delete(delete_index)
                with open('data.txt', 'r+') as f:
                    lines = f.readlines()
                    f.seek(0)
                    for line in lines:
                        if line.strip() != task:
                            f.write(line)
                    f.truncate()

        
        try:
            with open('data.txt', 'r') as file:
                for line in file:
                    self.main_text.insert(tk.END, line.strip())
        except FileNotFoundError:
            pass

        self.button = tk.Button(self.root, text="Add", font=('sarif', 20, 'bold italic'), width=10, bd=5, bg='orange', fg='black', command=add)
        self.button.place(x=30, y=180)

        self.button2 = tk.Button(self.root, text="Delete", font=('sarif', 20, 'bold italic'), width=10, bd=5, bg='orange', fg='black', command=delete)
        self.button2.place(x=30, y=280)

def main():
    root = tk.Tk()
    ui = TODO(root)
    root.mainloop()

if __name__ == "__main__":
    main()
