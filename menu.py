from distutils.command import clean
from turtle import update
from PyQt5.QtCore import Qt
from datetime import datetime
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import *  # QMainWindow, QApplication, QMessageBox, QPushButton
from schemas.schemas import RegistrationCompany
from connection.connection import session


class Registration:
    def __init__(self):
        self.session = session
        self.app = QtWidgets.QApplication([])
        #tela inicial
        self.window_main = uic.loadUi(r'qt/main-company.ui')
        self.window_main.pushButton.clicked.connect(self.show_registration)
        self.window_main.pushButton_2.clicked.connect(self.show_update)
        #tela de cadastro
        self.window = uic.loadUi(r'qt/company-registration.ui')
        self.window.pushButton.clicked.connect(self.registration)
        self.window.pushButton_2.clicked.connect(self.cancelar)
        #tela de atualização
        self.window2 = uic.loadUi(r'qt/company-update.ui')
        self.window2.pushButton_3.clicked.connect(self.set_values_to_update)
        #abrindo tela main
        self.window_main.show()
        #chamando o metodo no init para setar as empresas na comboBox antes da tela aparecer.
        self.get_info_companies()

    def get_info_companies(self):   
        query_company = self.session.query(RegistrationCompany).all()
        self.dict_info_companies = {}

        for company in query_company:
            self.dict_info_companies[company.name] = [company.code, company.cnpj, company.location, company.certificate]
            

        self.window2.comboBox_2.addItems(self.dict_info_companies.keys())
        
    #função criada para mostrar a tela de cadastro
    def show_registration(self):
        self.window.show()

    #função criada para mostrar a tela de atualização
    def show_update(self):
        self.window2.show()
     
    #função criada para cadastrar determinada empresa no banco de dados através de uma lista
    def registration(self):
        text1 = self.window.lineEdit.text()
        text2 = self.window.lineEdit_2.text()
        text3 = self.window.lineEdit_3.text()
        text4 = self.window.lineEdit_4.text()
        text5 = self.window.comboBox.currentText()

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

    def set_values_to_update(self):

        self.company = self.window.comboBox_2.setText()
        self.code = self.window.lineEdit_2.setText(self.list_text[1])
        self.cnpj = self.window.lineEdit_3.setText(self.list_text[2])
        self.location = self.window.lineEdit_4.setText(self.list_text[3])
        self.certificate = self.window.comboBox.setText(self.list_text[4])

    def update(self):
        obj = session.query(RegistrationCompany).where(name=self.company).one()

        obj.code = 12
        session.refresh(obj)
        session.commit()
        session.close()
        
    def cancelar(self):
        self.window.close()
    
if __name__ == "__main__":
    menu = Registration()
    #menu.main()
    menu.app.exec_()
