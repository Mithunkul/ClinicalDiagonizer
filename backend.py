# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 20:07:00 2023

@author: Supreeth
"""

class Backend:
    
    def submitPatientDetails(self):
        name = self.NAME_PATIENT_LE.text()
        age= self.AGE_PATIENT_LE.text()
        gender= self.GENDER_PATIENT_CB.currentText()
        weight = self.WEIGHT_PATIENT_LE.text()
        history = self.HISTORY_PATIENT_LE.toPlainText()
        print(name, age, gender, weight, history)
    
    
    def addRecord(self):
        patient = self.PATIENT_DISEASE_CB.currentText()
        treatment = self.TREATMENT_DISEASE_TE.toPlainText()
        observation = self.OBSERVATION_DISEASE_TE.toPlainText()
        drugs_used = self.DRUGSUSED_DISEASE_TE.toPlainText()
        side_effects = self.SIDEEFFECTS_DISEASE_TE.toPlainText()
        doc = self.DOCTOR_DISEASE_CB.currentText()
        print(patient, treatment, observation, drugs_used, side_effects, doc)
        
    def submitDrugDetails(self):
        name = self.NAME_DRUG_LE.text()
        composition = self.COMPOSITION_DRUG_LE.text()
        company = self.COMPANY_DRUG_LE.text()
        alternatives = self.ALTERNATIVES_DRUG_LE.text()
        print(name, composition, company, alternatives)