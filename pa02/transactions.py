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
    trans = {'rowid': trans_tuple[0], 
    'item #': trans_tuple[1], 
    'amount': trans_tuple[2], 
    'category': trans_tuple[3], 
    'date': trans_tuple[4],
    'description': trans_tuple[5]}
    return trans

def to_trans_dict_list(trans_tuples):
    ''' convert a list of category tuples into a list of dictionaries'''
    return [to_trans_dict(trans) for trans in trans_tuples]


class Transaction:
    '''Transaction represents a table of transactions'''
    # author: Yiwen
    def __init__(self, dbfile):
      self.dbfile = dbfile
      con = sqlite3.connect(self.dbfile)
      cur = con.cursor()
      cur.execute('''CREATE TABLE IF NOT EXISTS transactions
               (item_number numeric, amount numeric, category int, date text, description text)''')
      con.commit()
      con.close()

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
    def add(self, tx):
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("INSERT INTO transactions VALUES(?,?,?,?,?)", (
            tx['item #'],
            tx['amount'],
            tx['category'],
            tx['date'],
            tx['description'])
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
    
    def get_date_summary(self, month, date):
      con= sqlite3.connect(self.dbfile)
      cur = con.cursor()
      cur.execute("SELECT COUNT(rowid), AVG(amount), MIN(amount), MAX(amount) from transactions WHERE strftime('%m', date) = (?) AND strftime('%d', date) = (?) ",(month, date,) )
      results = cur.fetchall()
      con.commit()
      con.close()
      return {"total": results[0][0], "average_amount": results[0][1], "min_amount": results[0][2],
              "max_amount": results[0][3]}

    #author: Jiefang Li
    def Update(self, rowid, item) :
        '''update the content of a certian transactions'''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''UPDATE transactions
                        SET item #=(?), amount=(?), category=(?), date=(?), description=(?)
                        WHERE rowid=(?);
        ''',(item['item#'],item['amount'],item['category'],item['date'],item['description'],rowid))
        con.commit()
        con.close()
    
    def summarize_by_month(self, month):
        '''summarize the transactions by months'''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute(
            "SELECT COUNT(rowid), AVG(amount), MIN(amount), MAX(amount) from transactions WHERE strftime('%m', date) = (?) ",
            (month,))

        # cur.execute('''SELECT rowid, * from transactions, COUNT(rowid), AVERAGE(amount), MIN(amount), MAX(amount) WHERE strftime('%m', date) = (?);
        # ''',(month,))
        results = cur.fetchall()
        con.commit()
        con.close()
        return {"total": results[0][0], "average_amount": results[0][1], "min_amount": results[0][2], "max_amount": results[0][3]}

    #author: Huijie
    def select_all(self):
        ''' return all of the transactions as a list of dicts.'''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT rowid,* from transactions")
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_trans_dict_list(tuples)
    
    #author: Huijie
    def delete(self,rowid):
        ''' delete a transaction with the input rowid. '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''DELETE FROM transactions WHERE rowid=(?);''',(rowid,))
        con.commit()
        con.close()

    #author: Huijie
    def summary_by_year(self, year):
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute(
            "SELECT COUNT(rowid), AVG(amount), MIN(amount), MAX(amount) from transactions WHERE strftime('%Y', date) = (?)",
            (year,))
        results = cur.fetchall()
        con.commit()
        con.close()
        return {"total": results[0][0], "average_amount": results[0][1], "min_amount": results[0][2], "max_amount": results[0][3]}

    #author: Huijie
    def summary_by_cat(self, cat):
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute(
            "SELECT COUNT(rowid), AVG(amount), MIN(amount), MAX(amount) from transactions WHERE category = (?)",
            (cat,))
        results = cur.fetchall()
        con.commit()
        con.close()
        return {"total": results[0][0], "average_amount": results[0][1], "min_amount": results[0][2], "max_amount": results[0][3]}