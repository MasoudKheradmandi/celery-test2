from __future__ import absolute_import , unicode_literals
from proj.celery import app 


@app.task
def add(x,y):
    return x + y


@app.task
def multiply(a,b):
    return a * b

@app.task
def dev(m,n):
    return m / n