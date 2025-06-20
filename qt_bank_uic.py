import sys
from PyQt6.QtCore import QSize, pyqtSlot
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit, QVBoxLayout, QWidget, QLabel
import tp_oo

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Formation Python")
        self.setMinimumSize(QSize(800, 600))
        self.credit_button = QPushButton("Créditer")
        self.credit_input = QLineEdit()
        self.debit_button = QPushButton("Débiter")
        self.debit_input = QLineEdit()
        self.solde_label = QLabel("Votre solde est à 0€")
        self.error_label = QLabel("Erreur")
        self.error_label.setVisible(False)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.credit_button)
        self.layout.addWidget(self.credit_input)
        self.layout.addWidget(self.debit_button)
        self.layout.addWidget(self.debit_input)
        self.layout.addWidget(self.solde_label)
        self.layout.addWidget(self.error_label)
        self.container = QWidget()
        self.container.setLayout(self.layout)
        self.setCentralWidget(self.container)
        self.credit_button.clicked.connect(self.credit_button_clicked)
        self.debit_button.clicked.connect(self.debit_button_clicked)
        self.i = 0
        self.bank_account = tp_oo.BankAccount("CEA", tp_oo.Personne("Cyril", "Vincent"))

    @pyqtSlot()
    def credit_button_clicked(self):
        try:
            value = float(self.credit_input.text())
            self.bank_account.crediter(value)
            self.solde_label.setText(f"Votre solde est de {self.bank_account.solde} {self.bank_account.devise}" )
            self.error_label.setVisible(False)
        except ValueError as ex:
            self.error_label.setText(str(ex))
            self.error_label.setVisible(True)

    @pyqtSlot()
    def debit_button_clicked(self):
        try:
            value = float(self.debit_input.text())
            self.bank_account.debiter(value)
            self.solde_label.setText(f"Votre solde est de {self.bank_account.solde} {self.bank_account.devise}" )
            self.error_label.setVisible(False)
        except ValueError as ex:
            self.error_label.setText(str(ex))
            self.error_label.setVisible(True)
        except tp_oo.BankAccountError as ex:
            self.error_label.setText(f"Erreur de la banque: {ex}")
            self.error_label.setVisible(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()