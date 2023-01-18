# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 13:55:00 2023

@author: Supreeth
"""

import sqlite3

conn = sqlite3.connect("CDDB.db", timeout = 120.0)
c = conn.cursor()
with conn:
    c.execute("SELECT Patients.name,Doctor.name, Hospital.name, Record.symptoms from Record, Patients, Doctor, Hospital WHERE Patients.patient_id=Record.patient_id AND Record.doctor_id=Doctor.doctor_id AND Hospital.hospital_id=Doctor.hospital_id AND Record.symptoms LIKE '%fever%' AND Record.symptoms like '%cough%'")
    data = c.fetchall()
conn.close()
print(data)