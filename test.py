# -*- coding: utf-8 -*-
"""
Created on Thu May 27 22:56:31 2021

@author: acer
"""

import pandas as pd
wine=pd.read_csv(r'D:\winemag-data-130k-v2.csv')
print(wine.head())
mean_pr=wine.price.mean()
new_price=wine.price.map(lambda x:x-mean_pr)
print(new_price)
print(wine.price)
wine_n=wine.copy()

def star(row):
    if row.country=='Canada':
        return 3
    elif row.points>95:
        return 3
    elif row.points>85:
        return 2
    else:
        return 1
star_ratings=wine_n.apply(star,axis='columns')
print(star_ratings)
wine.info()


def menu_is_boring(meals):
    """Given a list of meals served over some period of time, return True if the
    same meal has ever been served two days in a row, and False otherwise.
    """
    for i in range(len(meals)-1):
        if meals[i]==meals[i+1]:
            return True
    return False

print(menu_is_boring(['x','y','y','z','p']))


A=0.0184
b='Crab'
print('{:.1%} is a very good time for {}'.format(A,b))


datestr = '1956-01-31'
year, month, day = datestr.split('-')
'/'.join([month, day, year])