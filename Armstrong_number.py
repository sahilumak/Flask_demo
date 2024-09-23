def armstrong(num):
    result = 0
    acc = num
    while num:
        a = num%10
        result = result * 10 + a
        num = num//10

    if result==acc:
        return 1
    else:
        return 0