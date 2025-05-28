
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from controller.converter_controller import ConverterController

class AppView:
    def __init__(self, root):
        self.root = root
        self.root.title("Conversor de PDF para Imagem")
        self.root.geometry("600x300")
        self.root.configure(bg="#2e2e2e")

        self.entrada_var = tk.StringVar()
        self.saida_var = tk.StringVar()
        self.status_var = tk.StringVar()

        self.setup_style()
        self.setup_components()

        self.controller = ConverterController(self)

    def setup_style(self):
        style = ttk.Style()
        style.theme_use('default')
        style.configure("TButton", foreground="white", background="#444", font=('Arial', 10, 'bold'))
        style.configure("TLabel", foreground="white", background="#2e2e2e", font=('Arial', 10))
        style.configure("TEntry", foreground="white", fieldbackground="#444", background="#444")
        style.configure("Horizontal.TProgressbar", troughcolor="#444", background="#00ff00", thickness=20)

    def setup_components(self):
        ttk.Label(self.root, text="Pasta de Entrada:").pack(pady=5)
        ttk.Entry(self.root, textvariable=self.entrada_var, width=60).pack()
        ttk.Button(self.root, text="Selecionar Pasta", command=self.selecionar_pasta_entrada).pack(pady=5)

        ttk.Label(self.root, text="Pasta de Saída:").pack(pady=5)
        ttk.Entry(self.root, textvariable=self.saida_var, width=60).pack()
        ttk.Button(self.root, text="Selecionar Pasta", command=self.selecionar_pasta_saida).pack(pady=5)

        ttk.Button(self.root, text="Converter PDFs", command=self.iniciar_conversao).pack(pady=10)

        self.progress_bar = ttk.Progressbar(self.root, orient="horizontal", length=400, mode="determinate")
        self.progress_bar.pack(pady=10)

        ttk.Label(self.root, textvariable=self.status_var).pack(pady=5)

    def selecionar_pasta_entrada(self):
        pasta = filedialog.askdirectory()
        if pasta:
            self.entrada_var.set(pasta)

    def selecionar_pasta_saida(self):
        pasta = filedialog.askdirectory()
        if pasta:
            self.saida_var.set(pasta)

    def iniciar_conversao(self):
        input_folder = self.entrada_var.get()
        output_folder = self.saida_var.get()
        self.controller.iniciar_conversao(input_folder, output_folder)

    def reset_progress(self):
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = 100

    def update_progress(self, atual, total):
        percent = (atual / total) * 100
        self.progress_bar["value"] = percent
        self.set_status(f"Convertendo... {atual}/{total} arquivos")

    def set_status(self, message):
        self.status_var.set(message)

    def show_error(self, message):
        messagebox.showerror("Erro", message)

    def show_warning(self, message):
        messagebox.showwarning("Atenção", message)
