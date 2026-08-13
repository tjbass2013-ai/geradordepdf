# selecionando a raca do personagem

def raca():
    rac = ""
    op = input()
    if op.isdigit():
        op = int(op)
        
        if op == 1:
            rac = "Humano"
            
        elif op == 2:
                rac ="Elfo"
                
        elif op == 3:
                rac = "Anao"
                
        elif op == 4:
                rac = "Halfling"
                
        elif op == 5:
                rac = "Tiefling"
                
        elif op == 6:
                rac = "Draconato"
                
        elif op < 1 or op > 6:
            rac = None
    else:
        rac = None
        
                
    return rac
            