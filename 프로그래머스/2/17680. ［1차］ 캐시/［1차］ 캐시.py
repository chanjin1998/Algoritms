from collections import deque
def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    if cacheSize == 0:
        return 5*len(cities)
    
    for i in range(len(cities)):
        cities[i] = cities[i].upper()
    for city in cities:
        if len(cache) < cacheSize:
            if city in cache:
                answer += 1
                cache.remove(city)
                cache.append(city)
            else:
                cache.append(city)
                answer += 5
        else:
            if city in cache:
                answer += 1
                cache.remove(city)
                cache.append(city)
            else:
                answer += 5
                cache.append(city)
                cache.popleft()
    return answer