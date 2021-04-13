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

def add():
    form = SQLFORM(db.contacts).process()
    return locals()

def view():
    if request.args(0) is None:
        rows = db(db.contacts).select(orderby=db.contacts.last_name | db.contacts.first_name)
    else:
        letter = request.args(0)
        rows = db(db.contacts.last_name.startswith(letter)).select(orderby=db.contacts.last_name | db.contacts.first_name)
        
    return locals()


def update():
    record = db.contacts(request.args(0)) or redirect(URL('view'))
    form = SQLFORM(db.contacts, record)
    if form.process().accepted:
        response.flash = T('Record Updated')
    else:
        response.flash = T('Please complete the form.')
    return locals()
