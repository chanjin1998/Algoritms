T = int(input())

for _ in range(T):
    clothes_dict = {}

    n = int(input())
    for _ in range(n):
        clothes_name, clothes_type = input().split() # 옷의 이름, 옷의 종류
        if (clothes_type not in clothes_dict): # 딕셔너리에 없던 옷 종류면
            clothes_dict[clothes_type] = [clothes_name] # 옷의 이름을 담은 리스트를 키(옷 종류)에 추가한다.
        else: # 딕셔너리에 이미 존재하는 옷 종류면 값 리스트에 추가한다.
            new_clothes = clothes_dict.get(clothes_type)
            new_clothes.append(clothes_name)
            clothes_dict[clothes_type] = new_clothes
    
    count = 1
    for key in clothes_dict:
        count *= len(clothes_dict[key]) + 1
    print(count - 1)