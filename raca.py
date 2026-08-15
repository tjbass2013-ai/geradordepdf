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
        
    #     if op == 1:
    #         rac = "Humano"
    #
    #     elif op == 2:
    #             rac ="Elfo"
    #
    #     elif op == 3:
    #             rac = "Anao"
    #
    #     elif op == 4:
    #             rac = "Halfling"
    #
    #     elif op == 5:
    #             rac = "Tiefling"
    #
    #     elif op == 6:
    #             rac = "Draconato"
    #
    #     elif op < 1 or op > 6:
    #         rac = None
    else:
        rac = None
        
                
    return rac
            
