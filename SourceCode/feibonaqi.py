x = 0
y = 0
for i in range(0,102):
    if i == 0:
        y = 1
    elif i == 1:
        x = 1
        y = 1
    else:
        tmp = y
        y = x + y
        x = tmp      
print(y)
