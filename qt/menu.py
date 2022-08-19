from PyQt5.QtCore import Qt
from datetime import datetime
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import *  # QMainWindow, QApplication, QMessageBox, QPushButton
from schemas.schemas import RegistrationCompany
from connection.connection import session


class Registration:
    def __init__(self):
        self.app = QtWidgets.QApplication([])
        self.window = uic.loadUi(r'qt/company-registration.ui')
        self.window.pushButton.clicked.connect(self.registration)
        self.window.pushButton_2.clicked.connect(self.cancelar)

    def registration(self):
        text1 = self.window.lineEdit.text()
        text2 = self.window.lineEdit_2.text()
        text3 = self.window.lineEdit_3.text()
        text4 = self.window.lineEdit_4.text()
        text5 = self.window.comboBox.currentText()

        list_text = [text1, text2, text3, text4, text5]

        if '' in list_text:
            QMessageBox.about(self.window, "Atenção!", "Preencha todos os campos!")

        else:
            obj = RegistrationCompany(name = list_text[0], code = list_text[1], cnpj = list_text[2], location = list_text[3], certificate = list_text[4])

            session.add(obj)
            session.commit()
            session.close()
            QMessageBox.about(self.window, "Parabéns!", "Registrado com sucesso!")

        """for i in list_text:
                print(i)"""

    def cancelar(self):
        self.window.close()
    
if __name__ == "__main__":
    menu = Registration()
    menu.window.show()
    menu.app.exec_()
