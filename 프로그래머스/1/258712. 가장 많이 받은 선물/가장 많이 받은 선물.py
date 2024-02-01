def solution(friends, gifts):
    answer = 0
    
    graph = [[0 for i in range(len(friends))] for i in range(len(friends))]
    graph2 = [[0 for i in range(3)] for i in range(len(friends))]
    
    for x in gifts:
        give, take = x.split(" ")
        graph[friends.index(give)][friends.index(take)] += 1
        
        graph2[friends.index(give)][0] += 1
        graph2[friends.index(take)][1] += 1
    
    for y,x in enumerate(graph2):
        graph2[y][2] = x[0] - x[1]

    graph3 = [0 for i in range(len(friends))]
    for x in range(len(friends)):
        a = graph[x]
        b = [row[x] for row in graph]
        print(a)
        print(b)
        for y in range(len(a)):
            if a[y] > b[y]:
                graph3[x] += 1
            elif a[y] == b[y] and x!=y:
                if graph2[x][2] > graph2[y][2]:
                    graph3[x] += 1
    print(graph3)
    return max(graph3)