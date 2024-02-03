def solution(edges):
    answer = []
    
    # [1,2] -> out 1 in 2
    dict ={}
    for x in edges:
        if x[0] in dict:
            dict[x[0]][0] += 1
        if x[1] in dict:
            dict[x[1]][1] += 1
        if x[0] not in dict:
            dict[x[0]] = [1,0]
        if x[1] not in dict:
            dict[x[1]] = [0,1]
    stick, eight, start = 0, 0, 0

    for k,v in dict.items():
        if v[0]==0:
            stick += 1
        elif v[0]==2:
            if v[1] > 0:
                eight += 1
            else:
                start = k
        elif v[0] > 2:
            start = k

    ring = abs(dict.get(start)[0] - eight - stick)
    answer.append(start)
    answer.append(ring)
    answer.append(stick)
    answer.append(eight)

    return answer