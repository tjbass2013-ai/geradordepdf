# escolha a classe do personagem

def cla():
    classe = ""
    op = input()

    if op.isdigit():
        op = int(op)
        
        classes = {
            1: "Barbaro",
            2: "Bardo",
            3: "Clerigo",
            4: "Guerreiro",
            5: "Ladino",
            6: "Mago"
        }
        
        classe = classes.get(op)
    else:
        classe = None
    
    return classe
