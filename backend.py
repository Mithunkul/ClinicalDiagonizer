# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 20:07:00 2023

@author: Supreeth
"""

import sqlite3
import datetime

class Backend:
    
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
        treatment = self.TREATMENT_DISEASE_TE.text()
        observation = self.OBSERVATION_DISEASE_TE.text()
        drugs_used = self.DRUGSUSED_DISEASE_TE.text()
        side_effects = self.SIDEEFFECTS_DISEASE_TE.text()
        doc = self.DOCTOR_DISEASE_CB.currentText()
        
        print(patient, treatment, observation, drugs_used, side_effects, doc)
        
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