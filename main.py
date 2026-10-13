import sys
from PySide6.QtWidgets import QApplication
from richnote import RichNote

if __name__ == "__main__":
    app = QApplication(sys.argv)
    richnote = RichNote()
    richnote.show()
    sys.exit(app.exec())
