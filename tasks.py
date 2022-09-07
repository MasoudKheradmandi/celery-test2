from celery import Celery

app = Celery('tasks',backend='redis://localhost:6379',broker='redis://localhost:6379')

@app.task
def add(x,y):
    return x + y


@app.task
def multiply(a,b):
    return a * b

@app.task
def dev(m,n):
    return m - n
