# De un tablero de 3 en raya verifica quien gano. Devolciendo: "x" , "o" , ""


def checking_table(table):
    # Verificacion horizontal
    for line in table:
        if len(set(line)) == 1:
            return line[0]
        
    # Verificacion vertical
    for line in (list(zip(*table))):
        if len(set(line)) == 1:
            return line[0]
        
    # Verificacion diagonal
    diagonal_01 = [table[unit][unit] for unit in range(3)]  
    if len(set(diagonal_01)) == 1:
            return diagonal_01[0]
    
    diagonal_02 = [table[-unit][-unit] for unit in range(1,4)] 
    if len(set(diagonal_02)) == 1:
            return diagonal_02[0]
    
    # Verificacion cruz
    cruz_01 = [table[unit][1] for unit in range(3)]
    if len(set(cruz_01)) == 1:
            return cruz_01[0]
    
    cruz_02 = [table[1][unit] for unit in range(3)]
    if len(set(cruz_02)) == 1:
            return cruz_02[0]
    
    return ""

user_table = [
    ["x","o","x"],
    ["o","o","x"],
    ["o","x","o"],
]


print(checking_table(user_table))