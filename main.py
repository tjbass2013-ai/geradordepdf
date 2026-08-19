import tkinter as tk
from tkinter import ttk
import personagem


def gerar_ficha():
    jogador = entrada_jogador.get()
    pers = entrada_personagem.get()
    raca = combo_raca.get()
    classe = combo_classe.get()
    nivel = entrada_nivel.get()
    alinhamento = entrada_alinhamento.get()
    background = texto_background.get("1.0", tk.END)

    forca = int(entradas_atributos["Força"].get())
    destreza = int(entradas_atributos["Destreza"].get())
    constituicao = int(entradas_atributos["Constituição"].get())
    inteligencia = int(entradas_atributos["Inteligência"].get())
    sabedoria = int(entradas_atributos["Sabedoria"].get())
    carisma = int(entradas_atributos["Carisma"].get())

    p = personagem.Personagem(nome=pers, raca=raca, classe=classe, nivel=nivel, alinhamento=alinhamento, background=background, forca=forca, destreza=destreza, constituicao=constituicao, inteligencia=inteligencia, sabedoria=sabedoria, carisma=carisma)

    print(jogador)
    print(p.nome)
    print(p.raca)
    print(p.classe)
    print(p.nivel)
    print(p.alinhamento)
    print(p.background)

    print(p.forca, p.destreza, p.constituicao)
    print(p.inteligencia, p.sabedoria, p.carisma)
    print(p.modificador_forca, p.modificador_destreza, p.modificador_constituicao)
    print(p.modificador_inteligencia, p.modificador_sabedoria, p.modificador_carisma)

    





# Janela principal
janela = tk.Tk()
janela.title("Gerador de Ficha de RPG")
janela.geometry("600x700")


# -------------------------
# DADOS DO PERSONAGEM
# -------------------------

frame_dados = ttk.LabelFrame(
    janela,
    text="Dados do Personagem"
)

frame_dados.pack(
    padx=10,
    pady=10,
    fill="x"
)


# Nome do jogador
ttk.Label(
    frame_dados,
    text="Nome do jogador:"
).grid(row=0, column=0, padx=5, pady=5, sticky="w")

entrada_jogador = ttk.Entry(frame_dados, width=40)
entrada_jogador.grid(row=0, column=1, padx=5, pady=5)


# Nome do personagem
ttk.Label(
    frame_dados,
    text="Nome do personagem:"
).grid(row=1, column=0, padx=5, pady=5, sticky="w")

entrada_personagem = ttk.Entry(frame_dados, width=40)
entrada_personagem.grid(row=1, column=1, padx=5, pady=5)


# Raça
ttk.Label(
    frame_dados,
    text="Raça:"
).grid(row=2, column=0, padx=5, pady=5, sticky="w")

racas = [
    "Anão",
    "Elfo",
    "Humano",
    "Halfling",
    "Meio-Elfo",
    "Meio-Orc"
]

combo_raca = ttk.Combobox(
    frame_dados,
    values=racas,
    state="readonly",
    width=37
)

combo_raca.grid(row=2, column=1, padx=5, pady=5)


# Classe
ttk.Label(
    frame_dados,
    text="Classe:"
).grid(row=3, column=0, padx=5, pady=5, sticky="w")

classes = [
    "Bárbaro",
    "Bardo",
    "Clerigo",
    "Guerreiro",
    "Ladino",
    "Mago"
]

combo_classe = ttk.Combobox(
    frame_dados,
    values=classes,
    state="readonly",
    width=37
)

combo_classe.grid(row=3, column=1, padx=5, pady=5)


# Nível
ttk.Label(
    frame_dados,
    text="Nível:"
).grid(row=4, column=0, padx=5, pady=5, sticky="w")

entrada_nivel = ttk.Entry(frame_dados, width=10)
entrada_nivel.grid(row=4, column=1, padx=5, pady=5, sticky="w")


# Alinhamento
ttk.Label(
    frame_dados,
    text="Alinhamento:"
).grid(row=5, column=0, padx=5, pady=5, sticky="w")

entrada_alinhamento = ttk.Entry(frame_dados, width=40)
entrada_alinhamento.grid(row=5, column=1, padx=5, pady=5)


# Background
ttk.Label(
    frame_dados,
    text="Background:"
).grid(row=6, column=0, padx=5, pady=5, sticky="nw")

texto_background = tk.Text(
    frame_dados,
    width=40,
    height=6
)

texto_background.grid(row=6, column=1, padx=5, pady=5)


# -------------------------
# ATRIBUTOS
# -------------------------

frame_atributos = ttk.LabelFrame(
    janela,
    text="Atributos"
)

frame_atributos.pack(
    padx=10,
    pady=10,
    fill="x"
)


# Dicionário para armazenar os campos
entradas_atributos = {}


atributos = [
    "Força",
    "Destreza",
    "Constituição",
    "Inteligência",
    "Sabedoria",
    "Carisma"
]


for i, atributo in enumerate(atributos):

    ttk.Label(
        frame_atributos,
        text=f"{atributo}:"
    ).grid(
        row=i // 2,
        column=(i % 2) * 2,
        padx=10,
        pady=5,
        sticky="w"
    )

    entrada = ttk.Entry(
        frame_atributos,
        width=8
    )

    entrada.grid(
        row=i // 2,
        column=(i % 2) * 2 + 1,
        padx=5,
        pady=5
    )

    entradas_atributos[atributo] = entrada


# -------------------------
# BOTÃO
# -------------------------

botao = ttk.Button(
    janela,
    text="Gerar Ficha PDF",
    command=gerar_ficha
)

botao.pack(
    pady=15
)


janela.mainloop()