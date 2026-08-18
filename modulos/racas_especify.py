def calcraca(rac):

    racas ={ 
        "Anão": {
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
        "vantagem": "Vantagem em testes de resistência a feitiços. Magias não podem o colocar para dormir.",
        "visao": "18m como se fosse luz plena e a noite como se fosse penumbra",
        "proficiencia_combate": "",
        "proficiencia_ferramenta": "",
        "especializacao": "Proficiente em Percepção. Você pode se mover através do espaço de qualquer criatura que seja de tamanho maior que o seu.",
        "idiomas": "Comum e Élfico",
        "aumento_habilidade": 2 # destreza
    },
    "Humano": {
        "deslocamento": "9m",
        "vantagem": "",
        "visao": "",
        "proficiencia_combate": "",
        "proficiencia_ferramenta": "",
        "especializacao": "",
        "idiomas": "Comum e um idioma adicional de sua escolha",
        "aumento_habilidade": 1 # em todos os atributos
    },
    "Halfling": {
        "deslocamento": "7,5m",
        "vantagem": "Vantagem em testes de resistência a medo",
        "visao": "",
        "proficiencia_combate": "Pode mover-se através do espaço de qualquer criatura que seja de tamanho maior que o seu",
        "proficiencia_ferramenta": "",
        "especializacao": "Quando você rolar um 1 natural em um teste de ataque, teste de habilidade ou teste de resistência, você pode rerrolar o dado e deve usar o novo resultado",
        "idiomas": "Comum e Halfling",
        "aumento_habilidade": 2 # destreza
    },
    "Meio-Elfo": {
        "deslocamento": "9m",
        "vantagem": "Vantagem em testes de resistência a feitiços. Magias não podem o colocar para dormir.",
        "visao": "Visão no escuro: 18m como se fosse luz plena e a noite como se fosse penumbra",
        "proficiencia_combate": "",
        "proficiencia_ferramenta": "",
        "especializacao": "Proficiência em duas perícias de sua escolha",
        "idiomas": "Comum, Élfico e um idioma adicional de sua escolha",
        "aumento_habilidade": 2 # destreza e carisma
    },
    "Meio-Orc": {
        "deslocamento": "9m",
        "vantagem": "",
        "visao": "Visão no escuro: 18m como se fosse luz plena e a noite como se fosse penumbra. Não pode diferenciar cores na penumbra, apenas tons de cinza",
        "proficiencia_combate": "Quando atinge ataque crítico com uma arma de combate corpo a corpo, você pode rolar um dado de dano adicional da arma e adicionar o resultado ao dano extra do crítico",
        "proficiencia_ferramenta": "",
        "especializacao": "Proficiência em Intimidação. Quando você rolar um 1 natural em um teste de ataque, teste de habilidade ou teste de resistência, você pode rerrolar o dado e deve usar o novo resultado",
        "idiomas": "Comum e Orc",
        "aumento_forca": 2,
        "aumento_constituicao": 1
    }

    }


    raca = racas.get(rac)
    return raca