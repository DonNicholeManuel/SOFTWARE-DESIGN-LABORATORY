def maxmin(data,n):
    if n == 1:
        return data[0],data[0]
    else:
        x ,y= maxmin(data, n - 1)
        return data[n - 1] if (data[n - 1] > x) else x, data[n - 1] if (data[n - 1] <y) else y
data=[2,4,6,7,8,10,15,20,21,22]
m,n=maxmin(data,10)
print(m,n)