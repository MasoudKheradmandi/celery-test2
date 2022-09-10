from proj.tasks import add , multiply 

x = add.delay(10,2)
print(x)
print(x.get())

z = multiply.delay(3,10)
print(z)
print(z.get())