from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QVBoxLayout, QLineEdit, QLabel
import sys
import tp_function
import house_library as house

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
        self.df = house.load("data/house/house.csv")


    def button_clicked(self): # Slot
        # print("Clicked")
        # self.button.setText("TOTO")
        try:
            value = self.input.text()
            value = int(value)
            # result = tp_function.is_prime(value)
            # self.label.setText(f"Le nombre {value} est premier: {result}")
            self.df = house.filter(self.df, value)
            surface_mean, surface_std, loyer_mean, loyer_std = house.stats(self.df)
            self.label.setText(f"Surface mean={surface_mean:.2f} Surface std={surface_std:.2f} Loyer mean={loyer_mean:.2f} Loyer std={loyer_std:.2f}")
        except:
            self.label.setText(f"Erreur merci de saisir un entier")
            self.label_2.setVisible(True)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()