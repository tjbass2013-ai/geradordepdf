def calcraca(rac):
    raca = rac
    racas ={ 
        "Anao": {
        "deslocamento": "7.5m",
        "vantagem": "Veneno e danos de veneno",
        "visao": "Penumbra: 18m luz plena Escuro: como se fosse penumbra",
        "proficiencia_combate": "Machados de batalha, machadinhas, martelos leves e martelos de guerra",
        "proficiencia_ferramentas": "Ferramentas de artesão: ferramentas de ferreiro, suprimento de cervejeiro ou ferramentas de pedreiro",
        "especializacao": "Sempre que você realizar um teste de Inteligência (História) relacionado à origem de um trabalho em pedra, você é considerado proficiente na perícia História e adiciona o dobro do seu bônus de proficiência ao teste, ao invés do seu bônus de proficiência normal",
        "idiomas": "Comum e Anão",
        "aumento_habilidade": 2 # constituicao

    },
    "Elfo": {
        "deslocamento": "9m",
        "vantagem": "",
        "visao": "18m como se fosse luz plena e a noite como se fosse penumbra",
        "proficiencia_combate": "",
        "proficiencia_ferramenta": "",
        "especializacao": "",
        "idiomas": "",
        "aumento_habilidade": 2 # destreza
    },
    "Humano": {
        "deslocamento": "",
        "vantagem": "",
        "visao": "",
        "proficiencia_combate": "",
        "proficiencia_ferramenta": "",
        "especializacao": "",
        "idiomas": "",
        "aumento_habilidade": 0
    },
    "Halfling": {
        "deslocamento": "",
        "vantagem": "",
        "visao": "",
        "proficiencia_combate": "",
        "proficiencia_ferramenta": "",
        "especializacao": "",
        "idiomas": "",
        "aumento_habilidade": 0
    },
    "Meio-Elfo": {
        "deslocamento": "",
        "vantagem": "",
        "visao": "",
        "proficiencia_combate": "",
        "proficiencia_ferramenta": "",
        "especializacao": "",
        "idiomas": "",
        "aumento_habilidade": 0
    },
    "Meio-Orc": {
        "deslocamento": "",
        "vantagem": "",
        "visao": "",
        "proficiencia_combate": "",
        "proficiencia_ferramenta": "",
        "especializacao": "",
        "idiomas": "",
        "aumento_habilidade": 0
    }

    }


    if raca == "Anão":
        return racas["Anao"]
    elif raca == "Elfo":
        return racas["Elfo"]
    elif raca == "Humano":
        return racas["Humano"]
    elif raca == "Halfling":
        return racas["Halfling"]
    elif raca == "Meio-Elfo":
        return racas["Meio-Elfo"]
    elif raca == "Meio-Orc":
        return racas["Meio-Orc"]
        