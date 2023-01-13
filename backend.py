# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 20:07:00 2023

@author: Supreeth
"""

import sqlite3
import datetime
from PyQt5 import QtCore, QtGui, QtWidgets

class Backend:
    
    def Login(self):
        entered_username = self.username_le.text()
        entered_password = self.password_le.text()
        
        conn = sqlite3.connect("CDDB.db", timeout = 120.0)
        c = conn.cursor()
        with conn:
            c.execute("SELECT username, access, password, hospital_id FROM Login_Details WHERE username=:username", {"username":entered_username})
            data = c.fetchone()
            try:
                username, access, password, hospital_id = data
            except:
                QtWidgets.QMessageBox.information(self, 'Info', "Wrong credentials")
                return
                
            if entered_username!=username or entered_password!=password:
                QtWidgets.QMessageBox.information(self, 'Info', "Wrong credentials")
                return
            if access != "Y":
                QtWidgets.QMessageBox.information(self, 'Info', "Access Denied")
                return
        with conn:
            c.execute("SELECT name FROM  Hospital WHERE hospital_id=:hospital_id", {'hospital_id': hospital_id})
            hosp = c.fetchone()
            self.hospital = {'name':hosp[0], 'id': hospital_id}
        conn.close()
        QtWidgets.QMessageBox.information(self, 'Info', "Welcome \n" + self.hospital['name'])
        self.CreateMainPage()
        docs = self.fetchDocsfromHispitalId(hospital_id)
        self.DOCTOR_DISEASE_CB.addItems(docs)
        patients = self.fetchAllPatients()
        self.PATIENT_DISEASE_CB.addItems(patients)
        
    def fetchDocsfromHispitalId(self, hid):
        conn = sqlite3.connect("CDDB.db", timeout = 120.0)
        c = conn.cursor()
        with conn:
            c.execute("SELECT doctor_id, name FROM Doctor WHERE hospital_id=:hospital_id", {"hospital_id":hid})
            data = c.fetchall()
        conn.close()
        docs=[]
        for item in data:
            idname = str(item[0]) +"-"+ str(item[1])
            docs.append(idname)
        return docs
    
    def fetchAllPatients(self):
        conn = sqlite3.connect("CDDB.db", timeout = 120.0)
        c = conn.cursor()
        with conn:
            c.execute("SELECT patient_id, name FROM Patients")
            data = c.fetchall()
        conn.close()
        pats=[]
        for item in data:
            idname = str(item[0]) +"-"+ str(item[1])
            pats.append(idname)
        return pats
    
    def flatten(self, llist):
        ret = [ ]
        for sublist in llist:
            for subelement in sublist:
                ret.append(subelement)
        return ret
        
        
    
    def submitPatientDetails(self):
        name = self.NAME_PATIENT_LE.text()
        age= self.AGE_PATIENT_LE.text()
        gender= self.GENDER_PATIENT_CB.currentText()
        weight = self.WEIGHT_PATIENT_LE.text()
        keywords = self.HISTORY_PATIENT_LE.text()
        
        
        conn = sqlite3.connect("CDDB.db", timeout = 120.0)
        c = conn.cursor()
        with conn:
            c.execute("SELECT MAX(patient_id) FROM Patients")
            patient_id = c.fetchone()
            patient_id = patient_id[0]
            if patient_id == None:
                patient_id = 1
            else:
                patient_id = patient_id+ 1
        
        with conn:
            c.execute("INSERT INTO Patients VALUES(:patient_id,:name, :age, :gender, :weight, :keywords, :date)",
                      {"patient_id":patient_id,
                       "name": name,
                       "age":age,
                       "gender":gender,
                       "weight":weight,
                       "keywords":keywords,
                       "date":str(datetime.datetime.now())
                       })
        conn.close()
    
    
    def addRecord(self):
        patient = self.PATIENT_DISEASE_CB.currentText()
        patient = patient.split("-")
        patient_id = int(patient[0])
        name = patient[1]
        
        doctor = self.DOCTOR_DISEASE_CB.currentText()
        doctor = doctor.split("-")
        doctor_id = doctor[0]
        
        symptoms = self.SYMPTOMS_DISEASE_TE.text()
        treatment = self.TREATMENT_DISEASE_TE.text()
        drugs_used = self.DRUGSUSED_DISEASE_TE.text()
        side_effects = self.SIDEEFFECTS_DISEASE_TE.text()
        
        
        conn = sqlite3.connect("CDDB.db", timeout = 120.0)
        c = conn.cursor()
        with conn:
            c.execute("INSERT INTO Record VALUES(:name, :symptoms, :patient_id, :doctor_id, :treatment,	:side_effects,	:drugs_used	, :date)", 
                      {"name": name,
                        "symptoms":symptoms,
                        "patient_id":patient_id,
                        "doctor_id":doctor_id,
                        "treatment":treatment,
                        "side_effects":side_effects,
                        "drugs_used": drugs_used,
                        "date": str(datetime.datetime.now())                       
                        })
        conn.close()
        
    def submitDrugDetails(self):
        name = self.NAME_DRUG_LE.text()
        composition = self.COMPOSITION_DRUG_LE.text()
        company = self.COMPANY_DRUG_LE.text()
        alternatives = self.ALTERNATIVES_DRUG_LE.text()
        
        print(name, composition, company, alternatives)
        
        conn = sqlite3.connect("CDDB.db", timeout = 120.0)
        c = conn.cursor()
        with conn:
            c.execute("SELECT MAX(drugs_id) FROM Drugs")
            drugs_id = c.fetchone()
            drugs_id = drugs_id[0]
            if drugs_id == None:
                drugs_id = 1
            else:
                drugs_id = drugs_id+ 1
        with conn:
            c.execute("INSERT INTO Drugs VALUES(:drugs_id, :name, :contents, :manufacturer, :alternatives, :date)",
                      {"drugs_id":drugs_id,
                       "name":name,
                       "contents":composition,
                       "manufacturer":company,
                       "alternatives":alternatives,
                       "date":str(datetime.datetime.now())
                       })
        conn.close()
        print("done")
        
    def searchByKeywords(self):
        keywords = self.SEARCH_LE.text()
        keywords = keywords.split(",")
        print(keywords)
        
# =============================================================================
#         conn = sqlite3.connect("CDDB.db", timeout = 120.0)
#         c = conn.cursor()
#         with conn:
#             c.execute("SELECT * FROM Record")
#         conn.close()
# =============================================================================
        