# -*- coding: utf-8 -*-
# try something like

def request_args():
    arg1 = float(request.args(0))
    arg2 = float(request.args(1))
    total = arg1 + arg2
    return locals()
    

def helloworld():
    msg = "Hello from the Controller!"
    return locals()


def index(): 
    return dict(message="hello from basics.py")
