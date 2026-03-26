import sys

from PySide6.QtWidgets import QApplication,QWidget

class MainWindows(QWidget):

    def __init__(self):
        super().__init__()
        
        self.setup_ui()

    def setup_ui(self):

        self.setWindowTitle("tes aplikasi")
        self.resize(400,300)

def main():
    app = QApplication(sys.argv)

    window = MainWindows()
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()

    

    
        