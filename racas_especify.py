def calcraca(rac):
    raca = rac
    deslocamento = 0
    vantagem = ""
    visao = ""
    proficiencia_combate = ""
    proficiencia_ferramentas = ""
    especializacao = ""
    idiomas = ""
    aumento_habilidade = 0

    # ver uma forma melhor de organizar estes dados para retornar. o melhor talvez seja reunir como um dicionario.

    if raca == "Anão":
        deslocamento = "7,5m"
        vantagem = "Veneno e danos de veneno"
        visao = "Penumbra: 18m luz plena Escuro: como se fosse penumbra"
        proficiencia_combate = "Machados de batalha, machadinhas, martelos leves e martelos de guerra"
        proficiencia_ferramentas = "Ferramentas de artesão: ferramentas de ferreiro, suprimento de cervejeiro ou ferramentas de pedreiro"
        aumento_habilidade = 2
    # elif raca == "Elfo":
        

    return (deslocamento, vantagem, visao, proficiencia_combate, proficiencia_ferramentas, aumento_habilidade)



