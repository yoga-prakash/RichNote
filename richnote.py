from PySide6.QtWidgets import QMainWindow, QFileDialog, QTextEdit, QInputDialog, QWidget, QVBoxLayout, QMessageBox, QLabel
from PySide6.QtCore import QTimer
from datetime import datetime
import os

file = QFileDialog()

class RichNote(QMainWindow):
    def __init__(self):
        super().__init__()
        self.file_path = None
        self.count = 1
        self.windows = []
        self.resize(1000, 700)
        self.setWindowTitle("Untitled")

        self.date = QLabel()
        now = datetime.now()
        self.date.setText(now.strftime("%d-%m-%Y"))

        self.clock_label = QLabel()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        self.update_time()

        self.statusBar().addWidget(self.date)
        self.statusBar().addPermanentWidget(self.clock_label)

        central = QWidget()
        layout = QVBoxLayout()

        self.textbox = QTextEdit()
        self.textbox.setPlaceholderText("Type here!")

        layout.addWidget(self.textbox)

        central.setLayout(layout)
        self.setCentralWidget(central)

        menubar = self.menuBar()

        filemenu = menubar.addMenu("File")

        Exit = filemenu.addAction("Exit", self.exit_app)
        Exit.setShortcut("Ctrl+E")

        save = filemenu.addAction("Save")
        save.setShortcut("Ctrl+S")
        save.triggered.connect(lambda: self.save_file(self.textbox.toPlainText()))

        New = filemenu.addAction("New File")
        New.setShortcut("Ctrl+N")
        New.triggered.connect(self.new_window)

        Open = filemenu.addAction("Open")
        Open.setShortcut("Ctrl+O")
        Open.triggered.connect(self.open_file)

        Edit = menubar.addMenu("Edit")

        Table = Edit.addAction("Table")
        Table.setShortcut("Ctrl+T")
        Table.triggered.connect(self.create_table)

        Image = Edit.addAction("Image")
        Image.setShortcut("Ctrl+I")
        Image.triggered.connect(self.insert_image)

        Hyperlink = Edit.addAction("Hyperlink")
        Hyperlink.setShortcut("Ctrl+H")
        Hyperlink.triggered.connect(self.create_link)

    def has_rich_content(self):
        # True if the note contains a table, an image or a link
        html = self.textbox.toHtml()
        return any(tag in html for tag in ("<table", "<img", "<a href"))

    def save_file(self, contents):
        rich = self.has_rich_content()

        # Tables, images and links are saved as Markdown, plain text as it is
        if rich:
            contents = self.textbox.toMarkdown()

        # Ask for a location on first save, or when a .txt note now needs to become .md
        if self.file_path is None or (rich and not self.file_path.lower().endswith(".md")):
            if rich:
                default = (os.path.splitext(self.file_path)[0] if self.file_path else "untitled") + ".md"
                filters = "Markdown Files (*.md)"
            else:
                default = "untitled"
                filters = "Text Files (*.txt);;Markdown Files (*.md);;Python Files (*.py);;All Files (*)"

            filename, _ = file.getSaveFileName(self.window(), "Save File", default, filters)
            if not filename:
                return
            if rich and not filename.lower().endswith(".md"):
                filename += ".md"
            self.file_path = filename
            self.setWindowTitle(os.path.basename(filename))

        with open(self.file_path, "w", encoding="utf-8") as textfile:
            textfile.write(contents)

    def create_table(self):
        row, condition1 = QInputDialog.getInt(self.window(), "Rows", "Enter number of rows:")
        column, condition2 = QInputDialog.getInt(self, "Columns", "Enter number of columns:")
        if condition1 and condition2:
            cursor = self.textbox.textCursor()
            cursor.insertTable(row, column)

    def insert_image(self):
        path, _ = file.getOpenFileName(self.window(), "Open Image", "", "All Images (*.png *.jpg *.jpeg)")
        if path:
            self.textbox.insertHtml(f'<img src="{path}" width = "300" height = "300">')

    def create_link(self):
        cursor = self.textbox.textCursor()
        selected = cursor.selectedText()
        link, condition = QInputDialog.getText(self.window(), "Insert Link", "Enter Url: ")
        if condition and link:
            if selected:
                cursor.insertHtml(f'<a href = "{link}" >{selected}</a>')
            else:
                self.textbox.insertHtml(f'<a href = "{link}" >{link}</a>')

    def exit_app(self):
        reply = QMessageBox.question(
            self.window(), "Exit", "Save before exiting?",
            QMessageBox.StandardButton.Yes |
            QMessageBox.StandardButton.No |
            QMessageBox.StandardButton.Cancel
        )
        if reply == QMessageBox.StandardButton.Yes:
            self.save_file(self.textbox.toPlainText())
            self.close()
        elif reply == QMessageBox.StandardButton.No:
            self.close()

    def new_window(self):
        new = RichNote()
        self.windows.append(new)
        new.show()

    def open_file(self):
        path, _ = file.getOpenFileName(self.window(), "Open File", "", "Text and Markdown Files (*.txt *.md);;Text Files (*.txt);;Markdown Files (*.md)")
        if path:
            with open(path, mode="r", encoding="utf-8") as textfile:
                contents = textfile.read()

            # Markdown files are displayed with their tables, images and links
            if path.lower().endswith(".md"):
                self.textbox.setMarkdown(contents)
            else:
                self.textbox.setPlainText(contents)

            self.file_path = path
            self.setWindowTitle(os.path.basename(path))

    def update_time(self):
        now = datetime.now()
        self.clock_label.setText(now.strftime("%H:%M:%S"))
