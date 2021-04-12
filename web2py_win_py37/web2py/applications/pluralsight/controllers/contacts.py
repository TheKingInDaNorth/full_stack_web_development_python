# -*- coding: utf-8 -*-
# try something like
def index(): return dict(message="hello from contacts.py")

def filter():
    rows1_count = db(db.contacts.state_name=='CA').count()
    
    rows2_all_sorted_by_name = db(db.contacts).select(orderby=~db.contacts.last_name | db.contacts.first_name)
    
    row3_startswith = db(db.contacts.last_name.startswith('M')).select(orderby=db.contacts.state_name | db.contacts.last_name)
    
    row4_by_state = db(~(db.contacts.state_name=='CA')).select(orderby=db.contacts.last_name | db.contacts.first_name)
    
    row5_combo = db((db.contacts.state_name=='CA') & (db.contacts.last_name.startswith('A'))).select(orderby=db.contacts.last_name)

    return locals()
