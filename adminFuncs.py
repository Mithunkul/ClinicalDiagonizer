# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 22:30:22 2023

@author: Supreeth
"""

import sqlite3
import datetime

class adminFuncs:
    
    def createHospital(name, address="", phone="", Type="", extra_details=""):
        conn = sqlite3.connect("CDDB.db", timeout = 120.0)
        c = conn.cursor()
        with conn:
            c.execute("SELECT MAX(hospital_id) FROM Hospital")
            hospital_id = c.fetchone()
            hospital_id = hospital_id[0]
            if hospital_id == None:
                hospital_id = 1
            else:
                hospital_id = hospital_id+ 1
        
        with conn:
            c.execute("INSERT INTO Hospital VALUES(:hospital_id,:name, :address, :phone, :type, :extra_details, :date)",
                      {"hospital_id":hospital_id,
                       "name": name,
                       "address":address,
                       "phone":phone,
                       "type":Type,
                       "extra_details":extra_details,
                       "date":str(datetime.datetime.now())
                       })
            
        conn.close()
        
    def createLogin(username, access, password, hospital_id):
        conn = sqlite3.connect("CDDB.db", timeout = 120.0)
        c = conn.cursor()
        with conn:
            c.execute("INSERT INTO Login_Details VALUES(:username, :access,:password, :hospital_id, :date)",
                      {"username":username,
                       "access":access,
                       "password":password,
                       "hospital_id":hospital_id,
                       "date": str(datetime.datetime.now())
                       })
        conn.close()
    
    def createDoctor(doctor_id, hospital_id, name, qualification):
        conn = sqlite3.connect("CDDB.db", timeout = 120.0)
        c = conn.cursor()
        with conn:
            c.execute("INSERT INTO Doctor VALUES(:doctor_id, :hospital_id,:name, :qualification, :date)",
                      {"doctor_id":doctor_id,
                       "hospital_id":hospital_id,
                       "name":name,
                       "qualification":qualification,
                       "date":str(datetime.datetime.now())
                       })
        conn.close()
        

#adminFuncs.createLogin(username="ammu123", access="Y", password="ammupwd", hospital_id=1)
#adminFuncs.createHospital(name="Apollo Hospitals, South Bangalore", address="Bannerghatta Road")
#adminFuncs.createDoctor(doctor_id=3, hospital_id=1, name="Suresh Babu", qualification="Family Physician")

