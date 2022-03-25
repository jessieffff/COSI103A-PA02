#! /opt/miniconda3/bin/python3
'''
tracker is an app that maintains a list of personal
financial transactions.

It uses Object Relational Mappings (ORM)
to abstract out the database operations from the
UI/UX code.

The ORM, Category, will map SQL rows with the schema
  (rowid, category, description)
to Python Dictionaries as follows:

(5,'rent','monthly rent payments') <-->

{rowid:5,
 category:'rent',
 description:'monthly rent payments'
 }

Likewise, the ORM, Transaction will mirror the database with
columns:
amount, category, date (yyyymmdd), description

In place of SQL queries, we will have method calls.

This app will store the data in a SQLite database ~/tracker.db

Note the actual implementation of the ORM is hidden and so it 
could be replaced with PostgreSQL or Pandas or straight python lists

'''

from datetime import datetime
from transactions import Transaction
import transactions as tx
from category import Category
import sys

transaction = Transaction('tracker.db')
category = Category('tracker.db')


# here is the menu for the tracker app

menu = '''
0. quit
1. show categories
2. add category
3. modify category
4. show transactions
5. add transaction
6. delete transaction
7. summarize transactions by date
8. summarize transactions by month
9. summarize transactions by year
10. summarize transactions by category
11. print this menu
'''

menu_string = "Here's the menu:\n0. quit \n1. show categories\n2. add category \n3. modify category\n4. show transactions\n5. add transaction\n6. delete transaction\n7. summarize transactions by date\n8. summarize transactions by month\n9. summarize transactions by year\n10. summarize transactions by category\n11. print this menu"






def process_choice(choice):

    if choice=='0':
        return
    elif choice=='1':
        cats = category.select_all()
        print_categories(cats)
    elif choice=='2':
        name = input("category name: ")
        desc = input("category description: ")
        cat = {'name':name, 'desc':desc}
        category.add(cat)
    elif choice=='3':
        print("modifying category")
        rowid = int(input("rowid: "))
        name = input("new category name: ")
        desc = input("new category description: ")
        cat = {'name':name, 'desc':desc}
        category.update(rowid,cat)
    elif choice=='4':
        print("show transactions")
        txns = transaction.select_all()
        print_transactions(txns)
    elif choice=='5':
        print("adding transaction")
        itemNumber = int(input("item #: "))
        amount = input("amount: ")
        cat = int(input("category (by rowid): "))
        description = input("description: ")
        date = datetime.now().strftime("%Y-%m-%d")
        transaction.add(tx.to_trans_dict((-1, # a filler value
                                           itemNumber,
                                           amount,
                                           cat,
                                           date,
                                           description,
                                           )))
    elif choice == '6':
        print("deleting transaction")
        rowid = int(input("transaction (by rowid): "))
        transaction.delete(rowid)
    elif choice == '7':
        month = input("input a month")
        date = input("intput a date")
        all_transactions = transaction.get_date_summary(month, date)
        print(all_transactions)
    # Author: Jiefang Li
    elif choice == '8':
        print("the month you would like to summarize (enter a number)")
        month = input("month: ")
        transactions_summarized_by_months = transaction.summarize_by_month(month)
        print(transactions_summarized_by_months)

    # author: Huijie
    elif choice == '9':
        year = input("the year for summary")
        select_transactions = transaction.summary_by_year(year)
        print(select_transactions)

    # author: Huijie
    elif choice == '10':
        cat = int(input('the category for summary'))
        select_transactions = transaction.summary_by_cat(cat)
        print(select_transactions)
    elif choice == '11':
        print(menu_string)
    else:
        print("choice",choice,"not yet implemented")

    choice = input("> ")
    return(choice)


def toplevel():
    ''' handle the user's choice '''

    ''' read the command args and process them'''
    print(menu)
    choice = input("> ")
    while choice !='0' :
        choice = process_choice(choice)
    print('bye')

#
# here are some helper functions
#

def print_transactions(items):
    ''' print the transactions '''
    if len(items)==0:
        print('no items to print')
        return
    print('\n')
    print("%-3s %-10s %-10s %-10s %-10s %-30s"%(
        'id', 'item #','amount','category','date','description'))
    print('-'*60)
    for item in items:
        values = tuple(item.values())
        print("%-3d %-10s %-10s %-10s %-10s %-30s"%values)

def print_category(cat):
    print("%-3d %-10s %-30s"%(cat['rowid'],cat['name'],cat['desc']))

def print_categories(cats):
    print("%-3s %-10s %-30s"%("id","name","description"))
    print('-'*45)
    for cat in cats:
        print_category(cat)


# here is the main call!

toplevel()

