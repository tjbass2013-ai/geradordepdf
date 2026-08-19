import racas_especify, modcalc

class Personagem(object):
    def __init__(self, nome, raca, classe, nivel, background, alinhamento, forca, destreza, constituicao, inteligencia, sabedoria, carisma):
        self.nome = nome
        self.raca = raca
        self.classe = classe
        self.nivel = nivel
        self.vida = 0
        self.dado_de_vida = ""
        self.background = background
        self.alinhamento = alinhamento
        self.forca = forca
        self.destreza = destreza
        self.constituicao = constituicao
        self.inteligencia = inteligencia
        self.sabedoria = sabedoria
        self.carisma = carisma
        self.modificador_forca = 0
        self.modificador_destreza = 0
        self.modificador_constituicao = 0
        self.modificador_inteligencia = 0
        self.modificador_sabedoria = 0
        self.modificador_carisma = 0
        self.classe_armadura = 0
        self.deslocamento = ""
        self.vantagem = ""
        self.visao = ""

        if self.raca == "Anão":
            self.constituicao += racas_especify.calcraca(self.raca)["aumento_habilidade"]
        elif self.raca == "Elfo":
            self.destreza += racas_especify.calcraca(self.raca)["aumento_habilidade"]
        elif self.raca == "Humano":
            self.forca += racas_especify.calcraca(self.raca)["aumento_habilidade"]
            self.destreza += racas_especify.calcraca(self.raca)["aumento_habilidade"]
            self.constituicao += racas_especify.calcraca(self.raca)["aumento_habilidade"]
            self.inteligencia += racas_especify.calcraca(self.raca)["aumento_habilidade"]
            self.sabedoria += racas_especify.calcraca(self.raca)["aumento_habilidade"]
            self.carisma += racas_especify.calcraca(self.raca)["aumento_habilidade"]
        elif self.raca == "Halfling":
            self.destreza += racas_especify.calcraca(self.raca)["aumento_habilidade"]
        elif self.raca == "Meio-Elfo":
            self.carisma += racas_especify.calcraca(self.raca)["aumento_habilidade"]
            self.destreza += racas_especify.calcraca(self.raca)["aumento_habilidade"]
        elif self.raca == "Meio-Orc":
            self.forca += racas_especify.calcraca(self.raca)["aumento_forca"]
            self.constituicao += racas_especify.calcraca(self.raca)["aumento_constituicao"]

        # Calculo dos modificadores de atributos    
        self.modificador_forca = modcalc.modCalc(self.forca)
        self.modificador_destreza = modcalc.modCalc(self.destreza)
        self.modificador_constituicao = modcalc.modCalc(self.constituicao)
        self.modificador_inteligencia = modcalc.modCalc(self.inteligencia)
        self.modificador_sabedoria = modcalc.modCalc(self.sabedoria)
        self.modificador_carisma = modcalc.modCalc(self.carisma)

        vida_e_dado = self.atributos_de_classe(self.classe)
        self.vida = vida_e_dado["vida"]
        self.dado_de_vida = vida_e_dado["dado-de-vida"]

        self.classe_armadura = self.ca()
        self.deslocamento = racas_especify.calcraca(self.raca)["deslocamento"]
        self.vantagem = racas_especify.calcraca(self.raca)["vantagem"]
        self.visao = racas_especify.calcraca(self.raca)["visao"]
        self.proficiencia_combate = racas_especify.calcraca(self.raca)["proficiencia_combate"]
        self.proficiencia_ferramenta = racas_especify.calcraca(self.raca)["proficiencia_ferramentas"]
        self.especializacao = racas_especify.calcraca(self.raca)["especializacao"]
        self.idiomas = racas_especify.calcraca(self.raca)["idiomas"]

    def atributos_de_classe(self, classe):
        atributos = {
            "vida": 0,
            "dado-de-vida": ""
        }

        if classe == "Barbaro":
            atributos["vida"] = 12 + modcalc.modCalc(self.constituicao)
            atributos["dado-de-vida"] = "1d12"
        elif classe == "Bardo":
            atributos["vida"] = 8 + modcalc.modCalc(self.constituicao)
            atributos["dado-de-vida"] = "1d8"
        elif classe == "Clérigo":
            atributos["vida"] = 8 + modcalc.modCalc(self.constituicao)
            atributos["dado-de-vida"] = "1d8"
        elif classe == "Guerreiro":
            atributos["vida"] = 10 + modcalc.modCalc(self.constituicao)
            atributos["dado-de-vida"] = "1d10"
        elif classe == "Ladino":
            atributos["vida"] = 8 + modcalc.modCalc(self.constituicao)
            atributos["dado-de-vida"] = "1d8"
        elif classe == "Mago":
            atributos["vida"] = 6 + modcalc.modCalc(self.constituicao)
            atributos["dado-de-vida"] = "1d6"
        return atributos

    def atributos_raca(self, rac):
        atributos = {
            "deslocamento": "",
            "vantagem": "",
            "visao": "",
            "proficiencia_combate": "",
            "proficiencia_ferramenta": "",
            "especializacao": "",
            "idiomas": ""
        }
        if rac == "Anão":
            atributos["deslocamento"] = racas_especify.calcraca(self.raca)["deslocamento"]
            atributos["vantagem"] = racas_especify.calcraca(self.raca)["vantagem"]
            atributos["visao"] = racas_especify.calcraca(self.raca)["visao"]
            atributos["proficiencia_combate"] = racas_especify.calcraca(self.raca)["proficiencia_combate"]
            atributos["proficiencia_ferramenta"] = racas_especify.calcraca(self.raca)["proficiencia_ferramentas"]
            atributos["especializacao"] = racas_especify.calcraca(self.raca)["especializacao"]
            atributos["idiomas"] = racas_especify.calcraca(self.raca)["idiomas"]
        elif rac == "Elfo":
            atributos["deslocamento"] = racas_especify.calcraca(self.raca)["deslocamento"]
            atributos["vantagem"] = racas_especify.calcraca(self.raca)["vantagem"]
            atributos["visao"] = racas_especify.calcraca(self.raca)["visao"]
            atributos["proficiencia_combate"] = racas_especify.calcraca(self.raca)["proficiencia_combate"]
            atributos["proficiencia_ferramenta"] = racas_especify.calcraca(self.raca)["proficiencia_ferramentas"]
            atributos["especializacao"] = racas_especify.calcraca(self.raca)["especializacao"]
            atributos["idiomas"] = racas_especify.calcraca(self.raca)["idiomas"]
        elif rac == "Humano":
            atributos["deslocamento"] = racas_especify.calcraca(self.raca)["deslocamento"]
            atributos["vantagem"] = racas_especify.calcraca(self.raca)["vantagem"]
            atributos["visao"] = racas_especify.calcraca(self.raca)["visao"]
            atributos["proficiencia_combate"] = racas_especify.calcraca(self.raca)["proficiencia_combate"]
            atributos["proficiencia_ferramenta"] = racas_especify.calcraca(self.raca)["proficiencia_ferramentas"]
            atributos["especializacao"] = racas_especify.calcraca(self.raca)["especializacao"]
            atributos["idiomas"] = racas_especify.calcraca(self.raca)["idiomas"]
        elif rac == "Halfling":
            atributos["deslocamento"] = racas_especify.calcraca(self.raca)["deslocamento"]
            atributos["vantagem"] = racas_especify.calcraca(self.raca)["vantagem"]
            atributos["visao"] = racas_especify.calcraca(self.raca)["visao"]
            atributos["proficiencia_combate"] = racas_especify.calcraca(self.raca)["proficiencia_combate"]
            atributos["proficiencia_ferramenta"] = racas_especify.calcraca(self.raca)["proficiencia_ferramentas"]
            atributos["especializacao"] = racas_especify.calcraca(self.raca)["especializacao"]
            atributos["idiomas"] = racas_especify.calcraca(self.raca)["idiomas"]
        elif rac == "Meio-Elfo":
            atributos["deslocamento"] = racas_especify.calcraca(self.raca)["deslocamento"]
            atributos["vantagem"] = racas_especify.calcraca(self.raca)["vantagem"]
            atributos["visao"] = racas_especify.calcraca(self.raca)["visao"]
            atributos["proficiencia_combate"] = racas_especify.calcraca(self.raca)["proficiencia_combate"]
            atributos["proficiencia_ferramenta"] = racas_especify.calcraca(self.raca)["proficiencia_ferramentas"]
            atributos["especializacao"] = racas_especify.calcraca(self.raca)["especializacao"]
            atributos["idiomas"] = racas_especify.calcraca(self.raca)["idiomas"]
        elif rac == "Meio-Orc":
            atributos["deslocamento"] = racas_especify.calcraca(self.raca)["deslocamento"]
            atributos["vantagem"] = racas_especify.calcraca(self.raca)["vantagem"]
            atributos["visao"] = racas_especify.calcraca(self.raca)["visao"]
            atributos["proficiencia_combate"] = racas_especify.calcraca(self.raca)["proficiencia_combate"]
            atributos["proficiencia_ferramenta"] = racas_especify.calcraca(self.raca)["proficiencia_ferramentas"]
            atributos["especializacao"] = racas_especify.calcraca(self.raca)["especializacao"]
            atributos["idiomas"] = racas_especify.calcraca(self.raca)["idiomas"]
        return atributos

    def ca(self):
        classe_armadura = 10 + modcalc.modCalc(self.destreza)
        return classe_armadura

