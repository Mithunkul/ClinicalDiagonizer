# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 13:55:00 2023

@author: Supreeth
"""

import sqlite3

conn = sqlite3.connect("CDDB.db", timeout = 120.0)
c = conn.cursor()
with conn:
    c.execute(r'INSERT INTO Patients VALUES(,"supreeth", 26, "male", 89,"ghvhjyvfgjgfyug", "12-12-2022")')
    data = c.fetchall()
conn.close()