import tkinter as tk
from tkinter import filedialog, simpledialog
import fitz  # PyMuPDF
from PIL import Image, ImageTk
import requests
import io

class PDFMiniPlayer:
    def __init__(self, root, pdf_path=None, pdf_url=None):
        self.root = root
        root.withdraw()  # Hide the root window
        self.zoom_level = 1.0
        self.pdf_document = None
        self.images = []  # To store references to the images
        # Window setup
        self.root.overrideredirect(True)  # Removes the title bar
        self.root.geometry("600x500")
        self.root.configure(bg="#2D2D2D")
        self.root.attributes("-topmost", True)  # Always on top

        # Resizing button
        resize_button = tk.Button(root, text="⤡", bg="#3C3C3C", fg="white")
        resize_button.place(x=0, y=0)
        resize_button.bind("<B1-Motion>", self.on_resize)
        resize_button.bind("<ButtonRelease-1>", self.on_resize_release)

        # Close button
        close_button = tk.Button(root, text="X", command=self.close_app, bg="#3C3C3C", fg="white")
        close_button.pack(anchor=tk.NE)

        # Canvas for PDF display (without scrollbars)
        self.canvas = tk.Canvas(root, bg="#2D2D2D")
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Keyboard shortcuts for zoom
        self.root.bind("<Control-Key-equal>", lambda event: self.zoom_in())
        self.root.bind("<Control-Key-minus>", lambda event: self.zoom_out())
        
        self.root.bind("<ButtonPress-1>", self.start_move)
        self.root.bind("<ButtonRelease-1>", self.stop_move)
        self.root.bind("<B1-Motion>", self.on_move)

        # Load PDF
        if pdf_path:
            self.pdf_document = fitz.open(pdf_path)
        elif pdf_url:
            self.download_and_show_pdf(pdf_url)

        if self.pdf_document:
            root.deiconify()
            self.show_all_pages()

        # Scroll functionality
        self.canvas.bind("<MouseWheel>", self.on_mousewheel)
        self.canvas.bind("<Shift-MouseWheel>", self.on_horizontal_scroll)
        
    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def stop_move(self, event):
        self.x = None
        self.y = None

    def on_move(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.root.winfo_x() + deltax
        y = self.root.winfo_y() + deltay
        self.root.geometry(f"+{x}+{y}")
        

    def on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def on_horizontal_scroll(self, event):
        self.canvas.xview_scroll(int(-1 * (event.delta / 120)), "units")
        
    def on_resize(self, event):
        if not hasattr(self, 'drag_data'): 
            self.drag_data = {'x': event.x_root, 'y': event.y_root, 
                              'width': self.root.winfo_width(), 'height': self.root.winfo_height()} 

        dx = event.x_root - self.drag_data['x']
        dy = event.y_root - self.drag_data['y']
        new_width = self.drag_data['width'] - dx  
        new_height = self.drag_data['height'] - dy  

        self.root.geometry(f"{int(new_width)}x{int(new_height)}")

        if self.pdf_document:
            self.show_all_pages()

    def on_resize_release(self, event):
        if hasattr(self, 'drag_data'):
            del self.drag_data
    

    # def on_resize(self, event):
    #     # Calculate the new top-left corner's X and Y coordinates
    #     new_x = self.root.winfo_x() + event.x 
    #     new_y = self.root.winfo_y() + event.y
        
    #     print(new_x, new_y)

    #     # Calculate the new width and height
    #     new_width = self.root.winfo_width() + self.root.winfo_x() - new_x
    #     new_height = self.root.winfo_height() + self.root.winfo_y() - new_y

    #     # Apply the new geometry
    #     self.root.geometry(f"{new_width}x{new_height}+{new_x}+{new_y}")
    #     if self.pdf_document:
    #         self.show_all_pages()

    def close_app(self):
        self.root.destroy()

    def download_and_show_pdf(self, url):
        response = requests.get(url)
        pdf_stream = io.BytesIO(response.content)
        self.pdf_document = fitz.open(stream=pdf_stream, filetype="pdf")
        self.show_all_pages()

    def show_all_pages(self):
        self.canvas.delete("all")
        self.images.clear()
        if self.pdf_document:
            for page_num in range(len(self.pdf_document)):
                self.show_pdf(page_num)

    def show_pdf(self, page_number):
        page = self.pdf_document.load_page(page_number)
        pix = page.get_pixmap(matrix=fitz.Matrix(self.zoom_level, self.zoom_level))
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        photo = ImageTk.PhotoImage(image=img)
        self.images.append(photo)  # Store the image reference
        self.canvas.create_image(0, page_number * pix.height, image=photo, anchor=tk.NW)
        self.canvas.config(scrollregion=self.canvas.bbox(tk.ALL))

    def zoom_in(self):
        if self.pdf_document:
            self.zoom_level += 0.2
            self.show_all_pages()

    def zoom_out(self):
        if self.pdf_document and self.zoom_level > 0.4:
            self.zoom_level -= 0.2
            self.show_all_pages()

def ask_pdf_source():
    choice = simpledialog.askstring("PDF Source", "Enter 'file' to open a PDF from your system or a URL to download the PDF:")
    if choice:
        if choice.lower() == 'file':
            file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
            if file_path:
                return file_path, None
        else:
            return None, choice
    return None, None

if __name__ == "__main__":
    root = tk.Tk()
    pdf_path, pdf_url = ask_pdf_source()
    if pdf_path or pdf_url:
        app = PDFMiniPlayer(root, pdf_path=pdf_path, pdf_url=pdf_url)
        root.mainloop()
    else:
        root.destroy()
