# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 13:55:00 2023

@author: amogha
"""

import sqlite3

conn = sqlite3.connect("CDDB.db", timeout = 120.0)
c = conn.cursor()
with conn:
    c.execute('select * from patients')
    data = c.fetchall()
    for item in data:
        print(item)
    
conn.close()

conn = sqlite3.connect("CDDB.db", timeout = 120.0)
c = conn.cursor()
with conn:
    c.execute('select * from hospital')
    data = c.fetchall()
    for item in data:
        print(item)
    
conn.close()

conn = sqlite3.connect("CDDB.db", timeout = 120.0)
c = conn.cursor()
with conn:
    c.execute('select * from doctor')
    data = c.fetchall()
    for item in data:
        print(item)
    
conn.close()

conn = sqlite3.connect("CDDB.db", timeout = 120.0)
c = conn.cursor()
with conn:
    c.execute('select * from record')
    data = c.fetchall()
    for item in data:
        print(item)
    
conn.close()

conn = sqlite3.connect("CDDB.db", timeout = 120.0)
c = conn.cursor()
with conn:
    c.execute('select * from drugs')
    data = c.fetchall()
    for item in data:
        print(item)
    
conn.close()

conn = sqlite3.connect("CDDB.db", timeout = 120.0)
c = conn.cursor()
with conn:
    c.execute('select * from login_details')
    data = c.fetchall()
    for item in data:
        print(item)
    
conn.close()