'''
test_categories runs unit and integration tests on the category module
'''

import pytest
from transactions import Transactions, to_trans_dict

@pytest.fixture
def dbfile(tmpdir):
    ''' create a database file in a temporary file system '''
    return tmpdir.join('test_tracker.db')

@pytest.fixture
def empty_db(dbfile):
    ''' create an empty database '''
    db = Transactions(dbfile)
    yield db


@pytest.fixture
def small_db(empty_db):
    ''' create a small database, and tear it down later'''
    tran1 = {'item #':'food','amount': 25, 'category': 'food', "date": "2022-01-24", "description": "delicious food"} 
    tran2 = {'item #':'transportation','amount': 30, 'category': 'food', "date": "2022-04-24", "description": "tickets"} 
    tran3 ={'item #':'food','transportation': 100, 'category': 'food', "date": "2022-04-24", "description": "gas"} 
    id1=empty_db.add(tran1)
    id2=empty_db.add(tran2)
    id3=empty_db.add(tran3)
    yield empty_db
    empty_db.delete(id3)
    empty_db.delete(id2)
    empty_db.delete(id1)

@pytest.fixture
def med_db(small_db):
    ''' create a database with 10 more elements than small_db'''
    rowids=[]
    # add 10 categories
    for i in range(10):
        s = str(i)
        cat ={'name':'name'+s,
               'desc':'description '+s,
                }
        rowid = small_db.add(cat)
        rowids.append(rowid)

    yield small_db

    # remove those 10 categories
    for j in range(10):
        small_db.delete(rowids[j])



@pytest.mark.simple
def test_to_cat_dict():
    ''' teting the to_cat_dict function '''
    a = to_cat_dict((7,'testcat','testdesc'))
    assert a['rowid']==7
    assert a['name']=='testcat'
    assert a['desc']=='testdesc'
    assert len(a.keys())==3


@pytest.mark.add
def test_add(med_db):
    ''' add a category to db, the select it, then delete it'''

    cat0 = {'name':'testing_add',
            'desc':'see if it works',
            }
    cats0 = med_db.select_all()
    rowid = med_db.add(cat0)
    cats1 = med_db.select_all()
    assert len(cats1) == len(cats0) + 1
    cat1 = med_db.select_one(rowid)
    assert cat1['name']==cat0['name']
    assert cat1['desc']==cat0['desc']


@pytest.mark.delete
def test_delete(med_db):
    ''' add a category to db, delete it, and see that the size changes'''
    # first we get the initial table
    cats0 = med_db.select_all()

    # then we add this category to the table and get the new list of rows
    cat0 = {'name':'testing_add',
            'desc':'see if it works',
            }
    rowid = med_db.add(cat0)
    cats1 = med_db.select_all()

    # now we delete the category and again get the new list of rows
    med_db.delete(rowid)
    cats2 = med_db.select_all()

    assert len(cats0)==len(cats2)
    assert len(cats2) == len(cats1)-1

@pytest.mark.update
def test_update(med_db):
    ''' add a category to db, updates it, and see that it changes'''

    # then we add this category to the table and get the new list of rows
    cat0 = {'name':'testing_add',
            'desc':'see if it works',
            }
    rowid = med_db.add(cat0)

    # now we upate the category
    cat1 = {'name':'new cat','desc':'new desc'}
    med_db.update(rowid,cat1)

    # now we retrieve the category and check that it has changed
    cat2 = med_db.select_one(rowid)
    assert cat2['name']==cat1['name']
    assert cat2['desc']==cat1['desc']

@pytest.mark.summary_date
def test_summary_date(small_db):
    transactions = Transactions(small_db).test_summary_date("Jan", 24)
    expected = [
      {'item #':'1','amount': 25, 'category': 'food', "date": "2022-01-24", "description": "delicious food"} 
    ]
    assert transactions["item #"]==expected[0]["item #"]

