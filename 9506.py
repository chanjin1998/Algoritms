while(1):
    val = []
    sum = 0
    word = ''
    n = int(input())
    if n == -1:
        break
    for i in range(1,n):
        if n % i ==0:
            val.append(i)
    for j in range(len(val)):
        sum +=val[j]
    if sum == n:
        for k in range(len(val)):
            if k == 0:
                word += str(val[k])
            else:
                word += " + %s"%str(val[k])
        print("%d = %s"%(n,word))
    else:
        print(n,"is NOT perfect.")