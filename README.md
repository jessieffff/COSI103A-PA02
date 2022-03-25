# CS103a Spring 22

# PA02: tracker.py and the Transaction class

This git repository is for sharing code developed in the course lessons.
Each Lesson will be a different branch with the name L??.
Not all lessons have branches.


### Transcripts

Script started on Thu Mar 24 22:35:20 2022
[1m[7m%[27m[1m[0m                                                                                                                                                                                                                                     
 

[0m[27m[24m[J(base) jiefang@Jiefangs-MBP pa02 % [K[?2004hexit pylint transactions.py -> typescript[13D             [14D[?2004l

************* Module transactions
transactions.py:87:0: C0301: Line too long (180/100) (line-too-long)
transactions.py:91:0: C0301: Line too long (101/100) (line-too-long)
transactions.py:112:0: C0301: Line too long (125/100) (line-too-long)
transactions.py:117:0: C0301: Line too long (130/100) (line-too-long)
transactions.py:136:0: C0301: Line too long (124/100) (line-too-long)
transactions.py:141:0: C0301: Line too long (130/100) (line-too-long)
transactions.py:149:0: C0301: Line too long (112/100) (line-too-long)
transactions.py:154:0: C0301: Line too long (130/100) (line-too-long)
transactions.py:13:0: W0611: Unused datetime imported from datetime (unused-import)

------------------------------------------------------------------
Your code has been rated at 9.04/10 (previous run: 9.04/10, +0.00)

[0m[1m[7m%[27m[1m[0m                                                                                                                                                                                                                                     
 

[0m[27m[24m[J(base) jiefang@Jiefangs-MBP pa02 % [K[?2004hpylint transactions.py[22Dexit                  [18D pylint transactions.py -> typescript[13D             [14D[22Dsq[2Cte3               [15D py[2Cnt transactions.py -> typescript[13D             [14D[22Dexit                  [18D     e    p pytest[?2004l

[1m======================================================================================================== test session starts =========================================================================================================[0m
platform darwin -- Python 3.8.5, pytest-6.1.1, py-1.9.0, pluggy-0.13.1
rootdir: /Users/jiefang/Library/Mobile Documents/com~apple~CloudDocs/BrandeisCourses/Spring2022/COSI103A/PA02/pa02, configfile: pytest.ini
[1mcollecting ... [0m[1m
collected 7 items                                                                                                                                                                                                                    [0m

test_category.py [32m.[0m[32m                                                                                                                                                                                                             [ 14%][0m
test_transaction.py [32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m                                                                                                                                                                                                     [100%][0m

[32m========================================================================================================= [32m[1m7 passed[0m[32m in 0.16s[0m[32m ==========================================================================================================[0m
[1m[7m%[27m[1m[0m                                                                                                                                                                                                                                     
 

[0m[27m[24m[J(base) jiefang@Jiefangs-MBP pa02 % [K[?2004hp python3 tracker.py[?2004l


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

> 5
adding transaction
item #: 1
amount: 5
category (by rowid): 1
description: bread
> 5
adding transaction
item #: 2
amount: 10
category (by rowid): 2
description: book
> 5
adding transaction
item #: 3
amount: 60
category (by rowid): 3
description: gas
> 5
adding transaction
item #: 4
amount: 8
category (by rowid): 2
description: dictionary
> 4
show transactions


id  item #     amount     category   date       description                   
------------------------------------------------------------
1   1          5          1          2022-03-24 bread                         
2   2          10         2          2022-03-24 book                          
3   3          60         3          2022-03-24 gas                           
4   4          8          2          2022-03-24 dictionary                    
> 7
input a month03
intput a date24
{'total': 4, 'average_amount': 20.75, 'min_amount': 5, 'max_amount': 60}
> 8
the month you would like to summarize (enter a number)
month: 03
{'total': 4, 'average_amount': 20.75, 'min_amount': 5, 'max_amount': 60}
> 9
the year for summary2022
{'total': 4, 'average_amount': 20.75, 'min_amount': 5, 'max_amount': 60}
> 10
the category for summary2
{'total': 2, 'average_amount': 9.0, 'min_amount': 8, 'max_amount': 10}
> 11
Here's the menu:
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
> exit         6
deleting transaction
transaction (by rowid): 1
> 4





