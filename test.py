from tasks import add , multiply ,dev

x = add.delay(10,2)
z = multiply.delay(3,10)
y = dev.delay(10,5)

print(y)
print(y.get())
print(x)
print(x.get())
print(z)
print(z.get())
# add.apply_async([40,2])