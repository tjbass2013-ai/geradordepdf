# selecionando a raca do personagem

def raca():
    rac = ""
    op = input()
    if op.isdigit():
        op = int(op)

        racas = {
            1: "Humaano",
            2: "Elfo",
            3: "Anao",
            4: "Halfiling",
            5: "Tiefling",
            6: "Meio-Orc"
        }

        rac = racas.get(op)
        
    else:
        rac = None
        
                
    return rac
            
