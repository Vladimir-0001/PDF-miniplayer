# PDF Viewer Application

## Overview

The **PDF Viewer Application** is a lightweight and efficient tool designed to simplify the way you interact with PDF documents. Built with Python and Tkinter, this application allows you to open and view PDFs from your local system or directly from a URL. It offers essential features like page navigation, zooming, and scrolling, all wrapped in a user-friendly interface.

## Features

- **Open PDFs from File or URL**: Easily load PDF documents from your computer or the internet.
- **Page Navigation**: Navigate through pages using Next and Previous buttons or keyboard arrow keys.
- **Zoom In and Out**: Adjust the zoom level for better readability.
- **Scrollbars**: Navigate within a page using vertical and horizontal scrollbars.
- **Keyboard Shortcuts**:
  - **Zoom In**: `Ctrl` + `+`
  - **Zoom Out**: `Ctrl` + `-`
- **Responsive UI**: The application window is resizable, and the content adjusts accordingly.
- **Efficient Rendering**: Renders only the current page for optimal performance.
- **Error Handling**: Provides informative messages for errors or navigation limits.

## Installation

### Prerequisites

- **Python 3.6** or higher

### Dependencies

Install the required Python libraries using `pip`:

```bash
pip install tkinter Pillow PyMuPDF requests
```

> **Note**: `tkinter` is usually included with Python. If you encounter issues, you may need to install it separately depending on your operating system.

### Clone the Repository

```bash
git clone https://github.com/Vladimir-0001/PDF-miniplayer.git
cd pdf-viewer-application
```

## Usage

Run the application using Python:

```bash
python pdf_viewer.py
```

### Loading a PDF

Upon starting, the application will prompt you to:

- **Open a file**: Enter `'file'` to select a PDF from your local system.
- **Enter a URL**: Provide a direct URL to a PDF document.

### Navigating the PDF

- **Next Page**: Click the **Next** button or press the Right Arrow key.
- **Previous Page**: Click the **Previous** button or press the Left Arrow key.
- **Zoom In**: Click the **Zoom In** button or press `Ctrl` + `+`.
- **Zoom Out**: Click the **Zoom Out** button or press `Ctrl` + `-`.
- **Scrolling**: Use the smouse wheel to navigate within a page.

### Keyboard Shortcuts

- **Zoom In**: `Ctrl` + `+`
- **Zoom Out**: `Ctrl` + `-`

## Code Structure

- **pdf_viewer.py**: The main application file containing the `PDFViewer` class and the `main()` function.

### Key Components

- **PDFViewer Class**: Manages the PDF rendering and user interactions.
  - **setup_ui()**: Initializes the user interface components.
  - **load_pdf()**: Loads a PDF from a file path.
  - **download_and_load_pdf()**: Downloads and loads a PDF from a URL.
  - **show_page()**: Renders the current page.
  - **zoom_in()/zoom_out()**: Adjusts the zoom level and re-renders the page.
  - **show_next_page()/show_previous_page()**: Handles page navigation.
  - **open_file()/open_url()**: Methods to open PDFs from different sources.
- **main() Function**: Entry point of the application that prompts the user for input and initializes the `PDFViewer` instance.

## Future Enhancements

- **Jump to Page**: Allow users to navigate to a specific page by entering the page number.
- **Search Functionality**: Implement text search within the PDF document.
- **Page Rotation**: Add options to rotate pages for better viewing angles.
- **Annotations and Highlights**: Enable users to add notes or highlight text.
- **Printing Support**: Allow printing of the current page or the entire document.
- **Bookmarking**: Let users bookmark pages for quick access.
- **Dark Mode**: Offer a dark theme for comfortable reading in low-light environments.

## Contributing

Contributions are welcome! To contribute:

1. **Fork the repository** on GitHub.
2. **Clone your fork**:
6. **Open a Pull Request** on the original repository.

Please ensure your code adheres to the project's coding standards and includes appropriate documentation.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For questions, suggestions, or issues, please open an issue on GitHub or contact:

- **Chase Recker**
- **Email**: [Vladimir0x45@protonmail.com](Vladimir0x45@protonmail.com)
- **GitHub**: [Vladimir-0001](https://github.com/Vladimir-0001)

## Acknowledgments

- **PyMuPDF**: For providing the tools to render PDF documents.
- **Pillow**: For image processing capabilities.
- **Tkinter**: The standard GUI toolkit for Python.

## References

- [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)
- [PyMuPDF Documentation](https://pymupdf.readthedocs.io/en/latest/)
- [Pillow Documentation](https://pillow.readthedocs.io/en/stable/)

---

*Thank you for using the PDF Viewer Application! If you find this tool helpful, please give it a star on GitHub.*
