def findAllPeople(n, meetings, firstPerson):
    result = [0, firstPerson]
    sorted_meetings = sorted(meetings, key=lambda x: x[2])
    for meet in sorted_meetings:
        if meet[0] in result or meet[1] in result:
            if meet[1] not in result:
                result.append(meet[1])
            if meet[0] not in result:
                result.append(meet[0])
        
    print(sorted(result))



findAllPeople(4, [[3,1,3],[1,2,2],[0,3,3]], 3)
# findAllPeople(5, [[3,4,2],[1,2,1],[2,3,1]], 1)