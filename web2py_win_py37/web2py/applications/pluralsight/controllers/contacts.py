# -*- coding: utf-8 -*-
# try something like
def index(): return dict(message="hello from contacts.py")

def data():
    rows = db(db.contacts).select()
    return locals()
