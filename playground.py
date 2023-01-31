# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 13:55:00 2023

@author: amogha
"""

import sqlite3

# conn = sqlite3.connect("CDDB.db", timeout = 120.0)
# c = conn.cursor()
# with conn:
#     c.execute('update patients SET age=16 where patient_id=15')
#     data = c.fetchall()
#     for item in data:
#         print(item)
    
# conn.close()

conn = sqlite3.connect("CDDB.db", timeout = 120.0)
c = conn.cursor()
with conn:
    c.execute('select * from drugs')
    data = c.fetchall()
    for item in data:
        print(item)
    
# conn.close()

# conn = sqlite3.connect("CDDB.db", timeout = 120.0)
# c = conn.cursor()
# with conn:
#     c.execute('delete from patients where patient_id=13')
#     data = c.fetchall()
#     for item in data:
#         print(item)
    
conn.close()

# conn = sqlite3.connect("CDDB.db", timeout = 120.0)
# c = conn.cursor()
# with conn:
#     c.execute('select * from record')
#     data = c.fetchall()
#     for item in data:
#         print(item)
    
# conn.close()

# conn = sqlite3.connect("CDDB.db", timeout = 120.0)
# c = conn.cursor()
# with conn:
#     c.execute('select * from drugs')
#     data = c.fetchall()
#     for item in data:
#         print(item)
    
# conn.close()

# conn = sqlite3.connect("CDDB.db", timeout = 120.0)
# c = conn.cursor()
# with conn:
#     c.execute('select * from login_details')
#     data = c.fetchall()
#     for item in data:
#         print(item)
    
# conn.close()