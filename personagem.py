import racas_especify, modcalc

class Personagem(object):
    def __init__(self, nome, raca, classe, nivel, background, alinhamento, forca, destreza, constituicao, inteligencia, sabedoria, carisma, modificador_forca, modificador_destreza, modificador_constituicao, modificador_inteligencia, modificador_sabedoria, modificador_carisma):
        self.nome = nome
        self.raca = raca
        self.classe = classe
        self.nivel = nivel
        self.background = background
        self.alinhamento = alinhamento
        self.forca = forca
        self.destreza = destreza
        self.constituicao = constituicao
        self.inteligencia = inteligencia
        self.sabedoria = sabedoria
        self.carisma = carisma
        self.modificador_forca = modificador_forca
        self.modificador_destreza = modificador_destreza
        self.modificador_constituicao = modificador_constituicao
        self.modificador_inteligencia = modificador_inteligencia
        self.modificador_sabedoria = modificador_sabedoria
        self.modificador_carisma = modificador_carisma

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
        modificador_forca = modcalc.modCalc(self.forca)
        modificador_destreza = modcalc.modCalc(self.destreza)
        modificador_constituicao = modcalc.modCalc(self.constituicao)
        modificador_inteligencia = modcalc.modCalc(self.inteligencia)
        modificador_sabedoria = modcalc.modCalc(self.sabedoria)
        modificador_carisma = modcalc.modCalc(self.carisma)

