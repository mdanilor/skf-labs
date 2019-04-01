#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

#Let's set up some database!!!

with lite.connect('Database.db') as con:
    cur = con.cursor()
    cur.execute("CREATE TABLE users(UserId INT, UserName TEXT, Password TEXT, SessionToken TEXT)")
    cur.execute("INSERT INTO users VALUES (1, 'admin', 'f865b53623b121fd34ee5426c792e5c33af8c227', NULL)")
    cur.execute("INSERT INTO users VALUES (2, 'user', '95c946bf622ef93b0a211cd0fd028dfdfcf7e39e', NULL)")
    cur.execute("INSERT INTO users VALUES (3, 'guest', '7cf7eddb174125539dd241cd745391694250e526', NULL)")
    
    con.commit()


