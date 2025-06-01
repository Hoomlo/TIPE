def init(n):
    structure  = [[i] for  i in range(n)]
    return structure

def trouver(structure, x):
    n = len(structure)
    c = 0
    
    for i in range(n):
        m = len(structure[i])
        c += m
        
        if c > n :
            break
        if c == n :
            c += 1
            for j in range(m):
                if structure[i][j] == x:
                    return i
        if c < n :
            for j in range(m):
                if structure[i][j] ==x:
                    return i
    return -1


def unir(structure, x, y):
    # return True if the union is effective and False if the 2 elements where in the same class  
    
    rx = trouver(structure, x)
    ry = trouver(structure, y)
    
    if rx == ry:
        return False
    
    if rx < ry:
        for i in range(len(structure[ry])):
            
            trouver[rx].append(structure[ry][i])
            trouver[ry].remove(structure[ry][i])
        return True
    else:
        for i in range(len(structure[rx])):
            
            trouver[ry].append(structure[rx][i])
            trouver[rx].remove(structure[rx][i])
        return True
            
            

