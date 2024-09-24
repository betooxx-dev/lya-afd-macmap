import tkinter as tk
from tkinter import ttk
import re

class MacRecognizer:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("MacMap - Reconocedor de direcciones MAC")
        self.window.geometry("650x550")
        self.window.configure(bg="#f0f0f0")

        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.configure_styles()

        self.create_widgets()

    def configure_styles(self):
        self.style.configure('TFrame', background="#f0f0f0")
        self.style.configure('TLabel', background="#f0f0f0", font=('Arial', 12))
        self.style.configure('TButton', font=('Arial', 12, 'bold'), background="#4CAF50", foreground="white")
        self.style.map('TButton', background=[('active', '#45a049')])

    def create_widgets(self):
        main_frame = ttk.Frame(self.window, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_rowconfigure(0, weight=1)

        title_label = ttk.Label(main_frame, text="Expresiones Regulares", font=('Arial', 16, 'bold'))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        ttk.Label(main_frame, text="Ingrese el texto:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.input_text = tk.Text(main_frame, height=10, width=70, font=('Arial', 11), bg="white")
        self.input_text.grid(row=2, column=0, columnspan=2, pady=5)

        self.start_button = ttk.Button(main_frame, text="Empezar Análisis", command=self.start_analysis)
        self.start_button.grid(row=3, column=0, columnspan=2, pady=15)

        self.status_label = ttk.Label(main_frame, text="", font=('Arial', 11, 'italic'))
        self.status_label.grid(row=4, column=0, columnspan=2, pady=5)

        result_frame = ttk.Frame(main_frame, padding="10")
        result_frame.grid(row=5, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=10)
        result_frame.grid_columnconfigure(0, weight=1)
        result_frame.grid_rowconfigure(0, weight=1)

        self.result_text = tk.Text(result_frame, height=12, width=70, font=('Arial', 11), bg="white", state='disabled')
        self.result_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        scrollbar = ttk.Scrollbar(result_frame, orient="vertical", command=self.result_text.yview)
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        self.result_text.configure(yscrollcommand=scrollbar.set)

    def start_analysis(self):
        self.start_button.config(state='disabled')
        self.status_label.config(text="Analizando...", foreground="blue")
        self.window.update()

        input_text = self.input_text.get("1.0", tk.END)
        valid_macs = self.find_valid_macs(input_text)

        self.show_results(valid_macs)
        self.status_label.config(text="Análisis completado", foreground="green")
        self.start_button.config(state='normal')

    def find_valid_macs(self, text):
        pattern = r'(?:(?:[0-9A-Fa-f]{2}[:-]){5}[0-9A-Fa-f]{2})|(?:(?:[0-9A-Fa-f]{2}\s){5}[0-9A-Fa-f]{2})'
        return [(match.group(), match.start()) for match in re.finditer(pattern, text)]

    def show_results(self, valid_macs):
        self.result_text.config(state='normal')
        self.result_text.delete("1.0", tk.END)
        if valid_macs:
            for i, (mac, position) in enumerate(valid_macs, 1):
                self.result_text.insert(tk.END, f"{i}. MAC válida: ", "bold")
                self.result_text.insert(tk.END, f"{mac} ", "mac")
                self.result_text.insert(tk.END, f"(posición: {position})\n")
        else:   
            self.result_text.insert(tk.END, "No se encontraron direcciones MAC válidas.", "italic")
        self.result_text.config(state='disabled')

        self.result_text.tag_configure("bold", font=('Arial', 11, 'bold'))
        self.result_text.tag_configure("mac", foreground="blue")
        self.result_text.tag_configure("italic", font=('Arial', 11, 'italic'))

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = MacRecognizer()
    app.run()