import tkinter as tk
from tkinter import ttk, filedialog
import csv
import openpyxl
from docx import Document
from bs4 import BeautifulSoup
import os

class MacAFD:
    def __init__(self):
        self.reset()

    def reset(self):
        self.state = 0
        self.mac = ""
        self.separator = None
        self.hex_count = 0
        self.sep_count = 0

    def is_hex(self, char):
        return char.lower() in '0123456789abcdef'

    def is_separator(self, char):
        return char in ':-. '

    def transition(self, char):
        if self.state % 3 == 0 and self.is_hex(char):
            self.state += 1
            self.mac += char
            self.hex_count += 1
        elif self.state % 3 == 1 and self.is_hex(char):
            self.state += 1
            self.mac += char
            self.hex_count += 1
        elif self.state % 3 == 2 and self.is_separator(char):
            if self.separator is None:
                self.separator = char
            if char == self.separator or (self.separator == ' ' and char in ':-.'):
                self.state += 1
                self.mac += char
                self.sep_count += 1
            else:
                self.reset()
        else:
            self.reset()

    def is_accepted(self):
        return self.hex_count == 12 and self.sep_count == 5 and len(self.mac) == 17

def find_valid_macs(text):
    afd = MacAFD()
    valid_macs = []
    current_mac_start = 0

    for i, char in enumerate(text):
        if afd.state == 0:
            current_mac_start = i
        afd.transition(char)
        if afd.is_accepted():
            is_valid = True
            if current_mac_start > 0:
                prev_char = text[current_mac_start - 1]
                if afd.is_hex(prev_char):
                    is_valid = False
            if i + 1 < len(text):
                next_char = text[i + 1]
                if afd.is_hex(next_char):
                    is_valid = False
            
            if is_valid:
                valid_macs.append((afd.mac, current_mac_start))
            afd.reset()
        elif char.isspace() and not afd.is_separator(char):
            afd.reset()
        elif not afd.is_hex(char) and not afd.is_separator(char):
            afd.reset()

    return valid_macs

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

        title_label = ttk.Label(main_frame, text="Reconocedor de direcciones MAC", font=('Arial', 16, 'bold'))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        ttk.Label(main_frame, text="Seleccione el archivo de entrada:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.file_path = tk.StringVar()
        self.file_entry = ttk.Entry(main_frame, textvariable=self.file_path, width=50)
        self.file_entry.grid(row=2, column=0, pady=5, padx=(0, 10))
        self.browse_button = ttk.Button(main_frame, text="Examinar", command=self.browse_file)
        self.browse_button.grid(row=2, column=1, pady=5)

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

    def browse_file(self):
        filetypes = [
            ('Archivos soportados', '*.xlsx *.csv *.docx *.html *.txt'),
            ('Excel', '*.xlsx'),
            ('CSV', '*.csv'),
            ('Word', '*.docx'),
            ('HTML', '*.html'),
            ('TXT', '*.txt'),
            ('Todos los archivos', '*.*')
        ]
        filename = filedialog.askopenfilename(filetypes=filetypes)
        if filename:
            self.file_path.set(filename)

    def read_file(self, file_path):
        _, file_extension = os.path.splitext(file_path)
        
        if file_extension == '.xlsx':
            return self.read_excel(file_path)
        elif file_extension == '.csv':
            return self.read_csv(file_path)
        elif file_extension == '.docx':
            return self.read_docx(file_path)
        elif file_extension == '.html':
            return self.read_html(file_path)
        elif file_extension == '.txt':
            return self.read_txt(file_path)
        else:
            raise ValueError("Formato de archivo no soportado")

    def read_excel(self, file_path):
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook.active
        content = []
        for row in sheet.iter_rows(values_only=True):
            content.append([str(cell) if cell is not None else '' for cell in row])
        return content

    def read_csv(self, file_path):
        with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            return list(reader)

    def read_docx(self, file_path):
        doc = Document(file_path)
        return [[paragraph.text] for paragraph in doc.paragraphs if paragraph.text.strip()]

    def read_html(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as htmlfile:
            soup = BeautifulSoup(htmlfile, 'html.parser')
            return [[element.get_text(strip=True)] for element in soup.find_all(['p', 'div', 'span', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']) if element.get_text(strip=True)]

    def read_txt(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as txtfile:
            return [line.strip() for line in txtfile if line.strip()]

    def start_analysis(self):
        self.start_button.config(state='disabled')
        self.status_label.config(text="Analizando...", foreground="blue")
        self.window.update()

        file_path = self.file_path.get()
        if not file_path:
            self.status_label.config(text="Por favor, seleccione un archivo", foreground="red")
            self.start_button.config(state='normal')
            return

        try:
            content = self.read_file(file_path)
            valid_macs = self.find_macs_in_content(content)
            self.show_results(valid_macs)
            self.save_results_to_csv(valid_macs)
            self.status_label.config(text="Análisis completado. Resultados guardados en 'resultados_mac.csv'", foreground="green")
        except Exception as e:
            self.status_label.config(text=f"Error: {str(e)}", foreground="red")
        finally:
            self.start_button.config(state='normal')

    def find_macs_in_content(self, content):
        valid_macs = []
        for row_num, row in enumerate(content, start=1):
            if isinstance(row, list):
                for col_num, cell in enumerate(row, start=1):
                    macs = find_valid_macs(cell)
                    for mac, position in macs:
                        valid_macs.append((mac, row_num, col_num, position))
            else:
                macs = find_valid_macs(row)
                for mac, position in macs:
                    valid_macs.append((mac, row_num, 1, position))
        return valid_macs

    def show_results(self, valid_macs):
        self.result_text.config(state='normal')
        self.result_text.delete("1.0", tk.END)
        if valid_macs:
            for i, (mac, row, col, position) in enumerate(valid_macs, 1):
                self.result_text.insert(tk.END, f"{i}. MAC válida: ", "bold")
                self.result_text.insert(tk.END, f"{mac} ", "mac")
                self.result_text.insert(tk.END, f"(Fila: {row}, Columna: {col}, Posición: {position})\n")
        else:
            self.result_text.insert(tk.END, "No se encontraron direcciones MAC válidas.", "italic")
        self.result_text.config(state='disabled')

        self.result_text.tag_configure("bold", font=('Arial', 11, 'bold'))
        self.result_text.tag_configure("mac", foreground="blue")
        self.result_text.tag_configure("italic", font=('Arial', 11, 'italic'))

    def save_results_to_csv(self, valid_macs):
        with open('resultados_mac.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['MAC', 'Fila', 'Columna', 'Posición'])
            for mac, row, col, position in valid_macs:
                writer.writerow([mac, row, col, position])

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = MacRecognizer()
    app.run()