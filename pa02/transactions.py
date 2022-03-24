'''
transactions.py is a Object Relational Mapping to the transactions table

The ORM will work map SQL rows with the schema
    (rowid,item#,amount, category, data, description)
to Python Dictionaries.

This app will store the data in a SQLite database ~/transactions.db

'''

import sqlite3

def to_trans_dict(trans_tuple):
    trans = {'rowid': trans_tuple[0], 
    'item_number': trans_tuple[1], 
    'amount': trans_tuple[2], 
    'category': trans_tuple[3], 
    'date': trans_tuple[4], 
    'description': trans_tuple[5]}
    return trans

class Transactions ():
    '''Transactions represents a table of transactions'''
    # author: Yiwen
    def __init__(self, dbfile):
      con = sqlite3.connect(self.dbfile)
      cur = con.cursor()
      cur.execute('''CREATE TABLE IF NOT EXISTS transactions 
                (item_number numeric, amount numeric, category text, date date, description text)''')
      con.commit()
      con.close()
      self.dbfile = dbfile

    # author: Yiwen
    def select_one(self, rowid):
      con= sqlite3.connect(self.dbfile)
      cur = con.cursor()
      cur.execute("SELECT rowid,* from categories where rowid=(?)",(rowid,) )
      tuples = cur.fetchall()
      con.commit()
      con.close()
      return to_trans_dict(tuples[0])

    #author: Jiefang Li
    def Update(self, rowid, item) :
        '''update the content of a certian transactions'''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''UPDATE transaction
                        SET item#=(?), amount=(?), category=(?), date=(?), description=(?)
                        WHERE rowid=(?);
        ''',(item['item#'],item['amount'],item['category'],item['date'],item['description'],rowid))
        con.commit()
        con.close()