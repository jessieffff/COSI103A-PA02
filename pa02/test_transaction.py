'''
test_categories runs unit and integration tests on the category module
'''

import pytest
from transactions import Transaction, to_trans_dict

@pytest.fixture
def dbfile(tmpdir):
    ''' create a database file in a temporary file system '''
    return tmpdir.join('test_tracker.db')

@pytest.fixture
def empty_db(dbfile):
    ''' create an empty database '''
    db = Transaction(dbfile)
    yield db


@pytest.fixture
def small_db(empty_db):
    ''' create a small database, and tear it down later'''
    tran1 = {'item #':'1','amount': 25, 'category': 'food', "date": "2022-01-24", "description": "delicious food"} 
    tran2 = {'item #':'2','amount': 30, 'category': 'enterntainment', "date": "2022-04-24", "description": "tickets"} 
    tran3 ={'item #':'3','amount': 50, 'category': 'transportation', "date": "2022-04-24", "description": "gas"} 
    id1=empty_db.add(tran1)
    id2=empty_db.add(tran2)
    id3=empty_db.add(tran3)
    yield empty_db
    empty_db.delete(id3)
    empty_db.delete(id2)
    empty_db.delete(id1)

#author: Qing Liu
@pytest.mark.add
def test_add(small_db):
    ''' add a category to db, the select it, then delete it'''

    tran4 ={'item #':'3','amount': 50, 'category': 'transportation', "date": "2022-04-24", "description": "gas"} 

    prev_db= small_db.select_all()
    rowid = small_db.add(tran4)
    current_db = small_db.select_all()
    assert len(current_db) == len(prev_db) + 1

#author: Huijie Liu
@pytest.mark.select_all
def test_add(small_db):
    ''' add a category to db, the select it, then delete it'''
    assert len(small_db.select_all()) == 4

#author: Yiwen Luo
@pytest.mark.select_one
def test_add(small_db):
    ''' add a category to db, the select it, then delete it'''
    t1= small_db.select_one(1)
    assert t1['amount'] == 25

#author: Jiefang Li
@pytest.mark.summary_month
def test_summary_month(small_db):
    transactions = small_db.summarize_by_month('01')
    assert transactions["total"]==1

#author: Jiefang Li
def test_update(small_db) :
        tran4 ={'item #':'8','amount': 50, 'category': 'transportation', "date": "2022-03-24", "description": "train"} 
        rowid = small_db.add(tran4)

        tran5 ={'item #':'9','amount': 90, 'category': 'transportation', "date": "2022-03-22", "description": "ship"} 

        small_db.update(rowid, tran5)

        tran6 = small_db.select_one(rowid)

        assert tran6['amount'] == tran5['amount']

#author: Huijie Liu
@pytest.mark.delete
def test_delete(small_db):
    ''' add a category to db, delete it, and see that the size changes'''
   
    trans0 = small_db.select_all()
    tran0 = {'item #':'food','amount': 25, 'category': 'food', "date": "2022-01-24", "description": "delicious food"} 
    rowid = small_db.add(tran0)
    trans1 = small_db.select_all()
    small_db.delete(rowid)
    trans2 = small_db.select_all()

    assert len(trans0)==len(trans2)
    assert len(trans2) == len(trans1)-1

#author: Huijie Liu
@pytest.mark.summary_year
def test_summary_year(small_db):
    transactions = small_db.summary_by_year('2022')
    assert transactions["total"]==3

#author: Huijie Liu 
@pytest.mark.category
def test_summary_cat(small_db):
    transactions = small_db.summary_by_cat('food')
    assert transactions["total"] == 1