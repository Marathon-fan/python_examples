from tasks import add

add.delay(1, 2)

result = add.delay(1, 2)

print(result)
print(result.get())   # get the async result

