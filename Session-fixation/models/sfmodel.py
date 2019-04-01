#!/usr/bin/python
from config.sqlite import *
import hashlib

class Users:
    def authenticateUser(self, userName, password, sessionToken):
        db = database_con()
        hashedPw = hashlib.sha1(password).hexdigest()
        sql = ''' UPDATE users SET SessionToken=? WHERE UserName=? AND Password=? '''
        params = (sessionToken, userName, hashedPw)
        cur = db.cursor()
        cur.execute(sql, params)
        print (sql, params)
        #db.commit()

    def getUserFromSessionToken(self, sessionToken):
        db = database_con()
        sql = ''' SELECT userName FROM users WHERE SessionToken=? '''
        params = (sessionToken, )
        cur = db.cursor()
        cur.execute(sql, params)
        rows = cur.fetchall()
        if len(rows) > 0:
            return rows[0][0]
        return None
