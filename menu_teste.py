"""from PyQt5.QtCore import Qt
from datetime import datetime
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import *  # QMainWindow, QApplication, QMessageBox, QPushButton
from schemas.schemas import RegistrationCompany
from connection.connection import session
import sys


class Registration(QWidget):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi(r'qt/company-registration.ui', self)
        self.pushButton.clicked.connect(self.registration)
        self.pushButton_2.clicked.connect(self.cancelar)
    
    def registration(self):
        text1 = self.lineEdit.text()
        text2 = self.lineEdit_2.text()
        text3 = self.lineEdit_3.text()
        text4 = self.lineEdit_4.text()
        text5 = self.comboBox.currentText()

        self.list_text = [text1, text2, text3, text4, text5]

        if '' in self.list_text:
            QMessageBox.about(self.window, "Atenção!", "Preencha todos os campos!")

        elif not self.list_text[1].isnumeric() or not self.list_text[2].isnumeric():
            QMessageBox.about(self.window, "Atenção!", "Você deu mole")

        else:
            obj = RegistrationCompany(name = self.list_text[0], code = self.list_text[1], cnpj = self.list_text[2], location = self.list_text[3], certificate = self.list_text[4])

            session.add(obj)
            session.commit()
            session.close()
            QMessageBox.about(self.window, "Parabéns!", "Registrado com sucesso!")
            
            self.window.lineEdit.setText('')
            self.window.lineEdit_2.setText('')
            self.window.lineEdit_3.setText('')
            self.window.lineEdit_4.setText('')

    
    def cancelar(self):
        print('Cancelando')


class App(QApplication):
    def __init__(self, sys_args=sys.argv):
        super().__init__(sys_args)
    
    def tela_cadastro(self):
        window = Registration()
        window.show()
        self.exec_()

App().tela_cadastro()"""