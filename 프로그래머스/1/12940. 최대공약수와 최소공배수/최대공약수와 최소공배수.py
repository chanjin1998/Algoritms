def solution(n, m):
    answer = []
    def gcd(n,m):
        while m:
            n, m = m , n%m
        return n
    res = gcd(n,m)
    res1 = n*m / res
    return res, res1