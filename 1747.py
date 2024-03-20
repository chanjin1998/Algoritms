import sys
n,k = map(int,sys.stdin.readline().split())
num = list(map(int,sys.stdin.readline().split()))
tmp = list(set(num))
dic = dict.fromkeys(tmp,0)

start = 0
end = 0
dic[num[start]] = 1
res = []
while end< n-1:
  if start <= end:
    end += 1
    # print('end:',end)
    dic[num[end]] += 1
  while max(dic.values()) > k:
    res.append(sum(dic.values())-1)
    dic[num[start]] -= 1
    # print(dic)
    start += 1
res.append(sum(dic.values()))
print(max(res))

# import sys
# input=sys.stdin.readline

# N,K=map(int,input().split())

# L=list(map(int,input().split()))

# start=0 ; end=1

# A=[0]*100001

# A[L[start]]+=1 ; count=1 ; answer=0
# while end<N:
#     if A[L[end]]<K:
#         A[L[end]]+=1
#         count+=1
#         end+=1

#     elif A[L[end]]>=K:
#         A[L[start]]-=1
#         start+=1
#         count-=1
#     answer=max(answer,count)

# print(answer)