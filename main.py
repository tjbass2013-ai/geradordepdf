# INFORMACOES DO JOGADOR

from reportlab.lib.units import cm
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    PageBreak
)
from reportlab.lib.pagesizes import A4

# imports modulos de calculos
import modcalc
import raca
import escolhaclasse

# DADOS

nomeJogador = ""
classe = None
antecedente = ""
nomePersonagem = ""
rac = None
tendencia = ""
pontosXP = ""

# CARACTERISTICAS

nomeJogador = input("insira o seu nome: ")
nomePersonagem = input("insira o nome do seu personagem: ")


while rac == None:
    print("""
                  
                  Selecione um numero de 1 a 6 para
                  as respectivas racas: 
                  
                  1. Humano
                  2. Elfo
                  3. Anao
                  4. Halfling
                  5. Tiefling
                  6. Draconato
                  
                  """)
    rac = raca.raca()
    if rac == None:
        print("""
              
              Escolha uma opcao valida!
              
              """)


forca = int(input("insira um valor para forca: "))
destreza = int(input("insira um valor para destreza: "))
constituicao = int(input("insira um valor para constituicao: "))
inteligencia = int(input("insira um valor para inteligencia: "))
sabedoria = int(input("insira um valor para sabedoria: "))
carisma = int(input("insira um valor para carisma: "))

# MODIFICADORES
modForca = modcalc.modCalc(forca)
modDest = modcalc.modCalc(destreza)
modConst = modcalc.modCalc(constituicao)
modInt = modcalc.modCalc(inteligencia)
modSabe = modcalc.modCalc(sabedoria)
modCar = modcalc.modCalc(carisma)

# INSERCAO DE DADOS






classeArm = 0
iniciativa = 0
deslocamento = 0

while classe == None:
    print("""
                  
                  Selecione um numero de 1 a 6 para
                  as respectivas classes: 
                  
                  1. Barbaro
                  2. Bardo
                  3. Clerigo
                  4. Guerreiro
                  5. Ladino
                  6. Mago
                  
                  """)
    classe = escolhaclasse.cla()
    if classe == None:
        print("""
              
              Escolha uma opcao valida!
              
              """)
# --------------------------
# CONFIGURACAO DO DOCUMENTO
# --------------------------

arquivo = f"{nomeJogador} - {nomePersonagem}.pdf"

doc = SimpleDocTemplate(
    arquivo,
    pagesize=A4,
    rightMargin=2 * cm,
    leftMargin=2*cm,
    topMargin=2*cm,
    bottomMargin=2*cm
)

# -------------------------
# ESTILOS
# -------------------------

styles = getSampleStyleSheet()

titulo = ParagraphStyle(
    "Titulo",
    parent=styles["Title"],
    fontSize=22,
    leading=26,
    alignment=TA_CENTER,
    spaceAfter=20
)

subtitulo = ParagraphStyle(
    "Subtitulo",
    parent=styles["Heading2"],
    fontSize=14,
    leading=18,
    spaceBefore=10,
    spaceAfter=10
)

texto = ParagraphStyle(
    "Texto",
    parent=styles["BodyText"],
    fontSize=10,
    leading=15,
    alignment=TA_LEFT,
    spaceAfter=10
)

# -----------------------------------
# CONTEÚDO
# -----------------------------------

story = []


# Título
story.append(
    Paragraph(
        "FICHA DE PERSONAGEM D&D",
        titulo
    )
)


# Subtítulo
story.append(
    Paragraph(
        f"Nome do Personagem: <i>{nomePersonagem}</i><br/>"
        f"Jogador: <i>{nomeJogador}</i><br/>",
        subtitulo
    )
)


# Texto
story.append(
    Paragraph(
        f"""
        <b>FORÇA:</b> {forca} <b>({modForca})</b><br/>
        <b>CONSTITUIÇAO:</b> {constituicao} <b>({modConst})</b><br/>
        <b>DESTREZA:</b> {destreza} <b>({modDest})</b><br/>
        <b>INTELIGENCIA:</b> {inteligencia} <b>({modInt})</b><br/>
        <b>SABEDORIA:</b> {sabedoria} <b>({modSabe})</b><br/>
        <b>CARISMA:</b> {carisma} <b>({modCar})</b><br/>
        """,
        texto
    )
)


# Outro parágrafo
story.append(
    Paragraph(
        """
    
        """,
        texto
    )
)


# Espaçamento
story.append(Spacer(1, 20))

# -----------------------------------
# GERAR PDF
# -----------------------------------

# doc.build(story)
print(f"""
      
      forca {forca} mod {modForca}\n 
      destreza {destreza} mod {modDest}
      constituicao {constituicao} mod {modConst}
      inteligencia {inteligencia} mod {modInt}
      sabedoria {sabedoria} mod {modSabe}
      carisma {carisma} mod {modCar}
      
      Raca {rac}
      Classe {classe}
      
      """)


print(f"PDF criado: {arquivo}")
