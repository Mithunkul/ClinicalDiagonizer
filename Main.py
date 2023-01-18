# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 21:22:35 2023

@author: Supreeth
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QSizePolicy, QStyleFactory
import sys
from backend import *

class Main(QtWidgets.QWidget, Backend):

    def __init__(self):
        super(Main, self).__init__()
        self.setWindowTitle("Clinical Diagonizer")
        self.setFixedWidth(750)
        self.setFixedHeight(750)
        #self.setWindowState(self.windowState()|QtCore.Qt.WindowMaximized)
        
# =============================================================================
        self.MAIN_VBOX = QtWidgets.QVBoxLayout()
        self.MAIN_VBOX.setContentsMargins(0, 0, 0, 0)
        self.MAIN_VBOX.setSpacing(0)
        
        self.GRID_BOX = QtWidgets.QGridLayout()
        
        self.DICT_FRAMES = {}
        self.DICT_FRAMES["Credentials"] = QtWidgets.QFrame()
        self.DICT_FRAMES["Main"] = QtWidgets.QFrame()
        
        #### Credentials Widgets
        
        CREDENTIALS_VBOX = QtWidgets.QVBoxLayout(self.DICT_FRAMES["Credentials"])
        USERNAME_HBOX = QtWidgets.QHBoxLayout()
        PASSWORD_HBOX = QtWidgets.QHBoxLayout()
        SUBMIT_HBOX = QtWidgets.QHBoxLayout()
         
        
        username_label = QtWidgets.QLabel("Username : ")
        password_label = QtWidgets.QLabel("Password : ")
        
        self.username_le = QtWidgets.QLineEdit()
        self.password_le = QtWidgets.QLineEdit()
        
        submit_pb = QtWidgets.QPushButton("Submit")
        submit_pb.clicked.connect(self.Login)
        
        USERNAME_HBOX.addStretch(1)
        USERNAME_HBOX.addWidget(username_label)
        USERNAME_HBOX.addWidget(self.username_le)
        USERNAME_HBOX.addStretch(1)
        
        PASSWORD_HBOX.addStretch(1)
        PASSWORD_HBOX.addWidget(password_label)
        PASSWORD_HBOX.addWidget(self.password_le)
        PASSWORD_HBOX.addStretch(1)
        
        SUBMIT_HBOX.addStretch(1)
        SUBMIT_HBOX.addWidget(submit_pb)
        SUBMIT_HBOX.addStretch(1)
        
        CREDENTIALS_VBOX.addStretch(1)
        CREDENTIALS_VBOX.addLayout(USERNAME_HBOX)
        CREDENTIALS_VBOX.addLayout(PASSWORD_HBOX)
        CREDENTIALS_VBOX.addLayout(SUBMIT_HBOX)
        CREDENTIALS_VBOX.addStretch(1)
        
        #### Main Frame Widgets
        MAINFRAME_VBOX = QtWidgets.QVBoxLayout(self.DICT_FRAMES["Main"])
        
        tabs_mainframe = QtWidgets.QTabWidget()
        tab1 = QtWidgets.QWidget()
        tab2 = QtWidgets.QWidget()
        
        tabs_mainframe.addTab(tab1, " Create ")
        tabs_mainframe.addTab(tab2, " Search ")
        
        #### Create Tab Widgets
        # Patient widgets
        PATIENT_GROUPBOX = QtWidgets.QGroupBox(" Patient ")
        
        NAME_PATIENT_LBL = QtWidgets.QLabel("Name : ")
        AGE_PATIENT_LBL = QtWidgets.QLabel("Age : ")
        GENDER_PATIENT_LBL = QtWidgets.QLabel("Gender : ")
        WEIGHT_PATIENT_LBL = QtWidgets.QLabel("Weight : ")
        HISTORY_PATIENT_LBL = QtWidgets.QLabel("History/Keywords : ")
        
        self.NAME_PATIENT_LE = QtWidgets.QLineEdit()
        self.AGE_PATIENT_LE = QtWidgets.QLineEdit()
        self.GENDER_PATIENT_CB = QtWidgets.QComboBox()
        self.WEIGHT_PATIENT_LE = QtWidgets.QLineEdit()
        self.HISTORY_PATIENT_LE = QtWidgets.QLineEdit()
        
        self.GENDER_PATIENT_CB.addItems(["Male", "Female", "Others"])
        
        SUBMI_PATIENT_PB = QtWidgets.QPushButton("Submit")
        SUBMI_PATIENT_PB.clicked.connect(self.submitPatientDetails)
        
        PATIENT_GRIDBOX = QtWidgets.QGridLayout()
        PATIENT_GRIDBOX.addWidget(NAME_PATIENT_LBL,0,0)
        PATIENT_GRIDBOX.addWidget(self.NAME_PATIENT_LE,0,1)
        PATIENT_GRIDBOX.addWidget(AGE_PATIENT_LBL,1,0)
        PATIENT_GRIDBOX.addWidget(self.AGE_PATIENT_LE,1,1)
        PATIENT_GRIDBOX.addWidget(GENDER_PATIENT_LBL,2,0)
        PATIENT_GRIDBOX.addWidget(self.GENDER_PATIENT_CB,2,1)
        PATIENT_GRIDBOX.addWidget(WEIGHT_PATIENT_LBL,3,0)
        PATIENT_GRIDBOX.addWidget(self.WEIGHT_PATIENT_LE,3,1)
        PATIENT_GRIDBOX.addWidget(HISTORY_PATIENT_LBL,4,0)
        PATIENT_GRIDBOX.addWidget(self.HISTORY_PATIENT_LE,4,1)
        PATIENT_GRIDBOX.addWidget(SUBMI_PATIENT_PB,5,0)
        
        PATIENT_GROUPBOX.setLayout(PATIENT_GRIDBOX)
        
        #Disease Widgets
        DISEASE_GROUPBOX = QtWidgets.QGroupBox(" Disease ")
        
        PATIENT_DISEASE_LBL = QtWidgets.QLabel("Patient : ")
        SYMPTOMS_DISEASE_LBL = QtWidgets.QLabel("Symptoms : ")
        TREATMENT_DISEASE_LBL = QtWidgets.QLabel("Treatment : ")
        DRUGSUSED_DISEASE_LBL = QtWidgets.QLabel("Drugs used : ")
        SIDEEFFECTS_DISEASE_LBL = QtWidgets.QLabel("Side Effects : ")
        DOCTOR_DISEASE_LBL = QtWidgets.QLabel("Doctor : ")
        
        self.PATIENT_DISEASE_CB = QtWidgets.QComboBox()
        self.SYMPTOMS_DISEASE_TE = QtWidgets.QLineEdit()
        self.TREATMENT_DISEASE_TE = QtWidgets.QLineEdit()
        self.DRUGSUSED_DISEASE_TE = QtWidgets.QLineEdit()
        self.SIDEEFFECTS_DISEASE_TE = QtWidgets.QLineEdit()
        self.DOCTOR_DISEASE_CB = QtWidgets.QComboBox()
        
        self.PATIENT_DISEASE_CB.setEditable(True)
        
        SUBMI_DISEASE_PB = QtWidgets.QPushButton("Submit")
        SUBMI_DISEASE_PB.clicked.connect(self.addRecord)
        
        DISEASE_GRIDBOX = QtWidgets.QGridLayout()
        DISEASE_GRIDBOX.addWidget(PATIENT_DISEASE_LBL,0,0)
        DISEASE_GRIDBOX.addWidget(self.PATIENT_DISEASE_CB,0,1)
        DISEASE_GRIDBOX.addWidget(SYMPTOMS_DISEASE_LBL,1,0)
        DISEASE_GRIDBOX.addWidget(self.SYMPTOMS_DISEASE_TE,1,1)
        DISEASE_GRIDBOX.addWidget(TREATMENT_DISEASE_LBL,2,0)
        DISEASE_GRIDBOX.addWidget(self.TREATMENT_DISEASE_TE,2,1)
        DISEASE_GRIDBOX.addWidget(DRUGSUSED_DISEASE_LBL,3,0)
        DISEASE_GRIDBOX.addWidget(self.DRUGSUSED_DISEASE_TE,3,1)
        DISEASE_GRIDBOX.addWidget(SIDEEFFECTS_DISEASE_LBL,4,0)
        DISEASE_GRIDBOX.addWidget(self.SIDEEFFECTS_DISEASE_TE,4,1)
        DISEASE_GRIDBOX.addWidget(DOCTOR_DISEASE_LBL,5,0)
        DISEASE_GRIDBOX.addWidget(self.DOCTOR_DISEASE_CB,5,1)
        DISEASE_GRIDBOX.addWidget(SUBMI_DISEASE_PB,6,0)
        
        DISEASE_GROUPBOX.setLayout(DISEASE_GRIDBOX)
        
        # Drugs Widgets
        DRUGS_GROUPBOX = QtWidgets.QGroupBox(" Drugs ")
        
        NAME_DRUG_LBL = QtWidgets.QLabel("Name : ") 
        COMPOSITION_DRUG_LBL = QtWidgets.QLabel("Composition : ") 
        COMPANY_DRUG_LBL = QtWidgets.QLabel("Company : ") 
        ALTERNATIVES_DRUG_LBL = QtWidgets.QLabel("Alternatives : ")
        
        self.NAME_DRUG_LE = QtWidgets.QLineEdit()
        self.COMPOSITION_DRUG_LE = QtWidgets.QLineEdit()
        self.COMPANY_DRUG_LE = QtWidgets.QLineEdit()
        self.ALTERNATIVES_DRUG_LE = QtWidgets.QLineEdit()
        
        SUBMI_DRUG_PB = QtWidgets.QPushButton("Submit")
        SUBMI_DRUG_PB.clicked.connect(self.submitDrugDetails)
        
        DRUGS_GRIDBOX = QtWidgets.QGridLayout()
        DRUGS_GRIDBOX.addWidget(NAME_DRUG_LBL,0,0)
        DRUGS_GRIDBOX.addWidget(self.NAME_DRUG_LE,0,1)
        DRUGS_GRIDBOX.addWidget(COMPOSITION_DRUG_LBL,1,0)
        DRUGS_GRIDBOX.addWidget(self.COMPOSITION_DRUG_LE,1,1)
        DRUGS_GRIDBOX.addWidget(COMPANY_DRUG_LBL,2,0)
        DRUGS_GRIDBOX.addWidget(self.COMPANY_DRUG_LE,2,1)
        DRUGS_GRIDBOX.addWidget(ALTERNATIVES_DRUG_LBL,3,0)
        DRUGS_GRIDBOX.addWidget(self.ALTERNATIVES_DRUG_LE,3,1)
        DRUGS_GRIDBOX.addWidget(SUBMI_DRUG_PB,4,0)
        
        DRUGS_GROUPBOX.setLayout(DRUGS_GRIDBOX)
        
        tab1.layout = QtWidgets.QVBoxLayout()
        
        tab1.layout.addWidget(PATIENT_GROUPBOX)
        tab1.layout.addWidget(DISEASE_GROUPBOX)
        tab1.layout.addWidget(DRUGS_GROUPBOX)
        
        tab1.setLayout(tab1.layout)
        
        #### Search Tab Widgets
        HBOX_SEARCH = QtWidgets.QHBoxLayout()
        SEARCH_LABEL = QtWidgets.QLabel(" Search by keyword(use commas to seperate) : ")
        self.SEARCH_LE = QtWidgets.QLineEdit()
        SEARCH_PB = QtWidgets.QPushButton("Search")
        SEARCH_PB.clicked.connect(self.searchByKeywords)
        
        HBOX_SEARCH.addWidget(SEARCH_LABEL)
        HBOX_SEARCH.addWidget(self.SEARCH_LE)
        HBOX_SEARCH.addWidget(SEARCH_PB)
        
        self.SEARCH_TABLE = QtWidgets.QTableWidget()
        self.SEARCH_TABLE.setColumnCount(7)
        
        tab2.layout = QtWidgets.QVBoxLayout()
        tab2.layout.addLayout(HBOX_SEARCH)
        tab2.layout.addWidget(self.SEARCH_TABLE)
        tab2.setLayout(tab2.layout)
        
        MAINFRAME_VBOX.addWidget(tabs_mainframe)
        self.GRID_BOX.addWidget(self.DICT_FRAMES["Credentials"],0,0)
        self.MAIN_VBOX.addLayout(self.GRID_BOX)

        self.setLayout(self.MAIN_VBOX)
        
# =============================================================================
        self.setContentsMargins(0, 0, 0, 0)
        self.show()
        
    def CreateMainPage(self):
        self.DICT_FRAMES["Credentials"].hide()
        self.GRID_BOX.addWidget(self.DICT_FRAMES["Main"],0,0)
        print(self.hospital)
    
    
if __name__ == "__main__":
    app = QtCore.QCoreApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)
    ui = Main()
    app.setStyle(QStyleFactory.create('Fusion'))
    try:
        sys.exit(app.exec_())
    except SystemExit:
        pass