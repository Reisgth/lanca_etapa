import tkinter as tk
from tkinter import ttk, messagebox

class InfoScreen:
    def __init__(self, root, on_submit):
        self.root = root
        self.root.title("Lançar Etapas")
        self.center_window(500, 280)

        # Frame principal
        frame = ttk.Frame(root, padding=20)
        frame.pack(expand=True)

        # Estilização dos widgets
        style = ttk.Style()
        style.configure("TLabel", font=("Arial", 11))
        style.configure("TEntry", font=("Arial", 11), padding=3)
        style.configure("TButton", font=("Arial", 11, "bold"), padding=3)

        # Labels e Entradas
        ttk.Label(frame, text="Usuário:").grid(row=0, column=0, sticky="w", pady=5)
        self.entry_user = ttk.Entry(frame, width=30)
        self.entry_user.grid(row=0, column=1, pady=5)

        ttk.Label(frame, text="Senha:").grid(row=1, column=0, sticky="w", pady=5)
        self.entry_password = ttk.Entry(frame, width=30, show="*")
        self.entry_password.grid(row=1, column=1, pady=5)

        ttk.Label(frame, text="Data do Documento (DD/MM/AAAA):").grid(row=2, column=0, sticky="w", pady=5)
        self.entry_doc_date = ttk.Entry(frame, width=30)
        self.entry_doc_date.grid(row=2, column=1, pady=5)

        ttk.Label(frame, text="Número do Documento:").grid(row=3, column=0, sticky="w", pady=5)
        self.entry_doc_number = ttk.Entry(frame, width=30)
        self.entry_doc_number.grid(row=3, column=1, pady=5)

        # Botão de Entrada
        btn_sendInfo = ttk.Button(frame, text="Enviar Informações", command=self.submit_data)
        btn_sendInfo.grid(row=5, column=0, columnspan=2, pady=20)
        
        self.entry_doc_date.bind("<KeyRelease>", self.format_date)
        self.on_submit = on_submit
        
    def format_date(self, event):
        date_str = self.entry_doc_date.get().replace("/", "")  # Remove barras para simplificar
        if len(date_str) > 2:
            date_str = date_str[:2] + "/" + date_str[2:]  # Adiciona a primeira barra
        if len(date_str) > 5:
            date_str = date_str[:5] + "/" + date_str[5:]  # Adiciona a segunda barra
        self.entry_doc_date.delete(0, tk.END)
        self.entry_doc_date.insert(0, date_str[:10])  # Limita o tamanho da data para 10 caracteres

    def submit_data(self):
        data = {
            "user": self.entry_user.get(),
            "password": self.entry_password.get(),
            "doc_date": self.entry_doc_date.get(),
            "doc_number": self.entry_doc_number.get(),
        }
        
        if any(value == "" for value in data.values()):
            messagebox.showerror("Atenção", "Todos os campos devem ser preenchidos!")
            return
        
        self.on_submit(data)
        self.root.destroy()

    def center_window(self, width, height):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")
