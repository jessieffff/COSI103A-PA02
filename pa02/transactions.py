'''
transactions.py is a Object Relational Mapping to the transactions table

The ORM will work map SQL rows with the schema
    (rowid,item#,amount, category, data, description)
to Python Dictionaries.

This app will store the data in a SQLite database ~/transactions.db

'''

import sqlite3
from datetime import datetime

def to_trans_dict(trans_tuple):
    ''' convert a list of transactionstuples into a dictionary'''
    trans = {'rowid': trans_tuple[0],
    'item #': trans_tuple[1],
    'amount': trans_tuple[2],
    'category': trans_tuple[3],
    'date': trans_tuple[4],
    'description': trans_tuple[5]}
    return trans

def to_trans_dict_list(trans_tuples):
    ''' convert a list of transactions tuples into a list of dictionaries'''
    return [to_trans_dict(trans) for trans in trans_tuples]


class Transaction:
    '''Transaction represents a table of transactions'''
    # author: Yiwen
    def __init__(self, dbfile):
        con = sqlite3.connect(dbfile)
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS transactions
                (item_number numeric, amount numeric, category int, date text, description text)''')
        con.commit()
        con.close()
        self.dbfile = dbfile

    # author: Qing Liu
    def show(self):
        ''' show all transactions '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''SELECT rowid,* FROM transactions;''')
        con.commit()
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_trans_dict_list(tuples)

    # author: Qing Liu
    def add(self, item):
        ''' add one transaction '''
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("INSERT INTO transactions VALUES(?,?,?,?,?)", (
            item['item #'],
            item['amount'],
            item['category'],
            item['date'],
            item['description'])
        )
        con.commit()
        cur.execute("SELECT last_insert_rowid()")
        last_rowid = cur.fetchone()
        con.commit()
        con.close()
        return last_rowid[0]

    # author: Qing Liu
    def delete(self,rowid):
        ''' delete a transaction with the input rowid. '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''DELETE FROM transactions WHERE rowid=(?);''',(rowid,))
        con.commit()
        con.close()

    # author: Yiwen Luo
    def get_date_summary(self, month, date):
        '''summarize the transactions by dates'''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT COUNT(rowid), AVG(amount), MIN(amount), MAX(amount) from transactions WHERE strftime('%m', date) = (?) AND strftime('%d', date) = (?) ",(month, date,) )
        results = cur.fetchall()
        con.commit()
        con.close()
        return {"total": results[0][0], "average_amount": results[0][1], "min_amount": results[0][2],
                "max_amount": results[0][3]}

    #author: Jiefang Li
    def update(self, rowid, item) :
        '''update the content of a certian transactions'''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''UPDATE transactions
                        SET item_number =(?), amount=(?), category=(?), date=(?), description=(?)
                        WHERE rowid=(?);
        ''',(item['item #'],item['amount'],item['category'],item['date'],item['description'],rowid))
        con.commit()
        con.close()

     #author: Jiefang Li
    def summarize_by_month(self, month):
        '''summarize the transactions by months'''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute(
            "SELECT COUNT(rowid), AVG(amount), MIN(amount), MAX(amount) from transactions WHERE strftime('%m', date) = (?) ",
            (month,))
        results = cur.fetchall()
        con.commit()
        con.close()
        return {"total": results[0][0], "average_amount": results[0][1], "min_amount": results[0][2], "max_amount": results[0][3]}

    #author:  Huijie Liu
    def select_all(self):
        ''' return all of the transactions as a list of dicts.'''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT rowid,* from transactions")
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_trans_dict_list(tuples)

    #author: Huijie Liu
    def summary_by_year(self, year):
        '''summarize the transactions by year'''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute(
            "SELECT COUNT(rowid), AVG(amount), MIN(amount), MAX(amount) from transactions WHERE strftime('%Y', date) = (?)",
            (year,))
        results = cur.fetchall()
        con.commit()
        con.close()
        return {"total": results[0][0], "average_amount": results[0][1], "min_amount": results[0][2], "max_amount": results[0][3]}

    #author: Huijie Liu
    def summary_by_cat(self, cat):
        '''summarize the transactions by category'''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute(
            "SELECT COUNT(rowid), AVG(amount), MIN(amount), MAX(amount) from transactions WHERE category = (?)",
            (cat,))
        results = cur.fetchall()
        con.commit()
        con.close()
        return {"total": results[0][0], "average_amount": results[0][1], "min_amount": results[0][2], "max_amount": results[0][3]}

    # author: Yiwen Luo
    def select_one(self, rowid):
        '''select one transaction by row id'''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT rowid,* from transactions where rowid=(?)",(rowid,) )
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_trans_dict(tuples[0])
