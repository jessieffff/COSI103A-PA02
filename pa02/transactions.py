'''
transactions.py is a Object Relational Mapping to the transactions table

The ORM will work map SQL rows with the schema
    (rowid,item#,amount, category, data, description)
to Python Dictionaries.

This app will store the data in a SQLite database ~/transactions.db

'''

import sqlite3

def to_trans_dict(trans_tuple):
    ''' trans is a category tuple (rowid, name, desc)'''
    trans = {'rowid':trans_tuple[0], 'item#':trans_tuple[1], 'amount':trans_tuple[2], 
            'category':trans_tuple[3], 'data':trans_tuple[4], 'description':trans_tuple[5]}
    return trans

def to_trans_dict_list(trans_tuples):
    ''' convert a list of category tuples into a list of dictionaries'''
    return [to_trans_dict(trans) for trans in trans_tuples]


class Transactions ():
    '''Transactions represens a table of transactions'''


    #author: Jiefang Li
    def Update(self, rowid, item) :
        '''update the content of a certian transaction'''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''UPDATE transactions
                        SET item#=(?), amount=(?), category=(?), date=(?), description=(?)
                        WHERE rowid=(?);
        ''',(item['item#'],item['amount'],item['category'],item['date'],item['description'],rowid))
        con.commit()
        con.close()
    
    #Do we need to add a new function named grouped by? For example group by category, or month?