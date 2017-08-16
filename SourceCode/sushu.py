# 高手优化后的版本
for i in range(2,1):
    for j in range(2,int(i**0.5)+1):
        if i % j == 0:
            break
    else:
        print(i)
