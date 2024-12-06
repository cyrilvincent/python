from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QVBoxLayout, QLineEdit, QLabel
import sys
import tp_function

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Formation")
        self.button = QPushButton("OK")
        self.button.clicked.connect(self.button_clicked) # clicked = Signal, connect lie le signal au slot
        self.input = QLineEdit()
        self.label = QLabel("Hello")
        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.button)
        layout.addWidget(self.label)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


    def button_clicked(self): # Slot
        # print("Clicked")
        # self.button.setText("TOTO")
        value = self.input.text()
        value = int(value)
        result = tp_function.is_prime(value)
        self.label.setText(f"Le nombre {value} est premier: {result}")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()