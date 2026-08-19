import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, KeepTogether
)
from reportlab.lib.units import mm

import personagem


RACAS = [
    "Anão", "Elfo", "Humano", "Halfling", "Meio-Elfo", "Meio-Orc"
]

CLASSES = [
    "Bárbaro", "Bardo", "Clérigo", "Guerreiro", "Ladino", "Mago"
]

ATRIBUTOS = [
    "Força", "Destreza", "Constituição",
    "Inteligência", "Sabedoria", "Carisma"
]


def gerar_pdf(dados, caminho):
    doc = SimpleDocTemplate(
        caminho,
        pagesize=A4,
        rightMargin=12 * mm,
        leftMargin=12 * mm,
        topMargin=12 * mm,
        bottomMargin=12 * mm
    )

    estilos = getSampleStyleSheet()

    titulo = ParagraphStyle(
        "Titulo",
        parent=estilos["Title"],
        fontSize=18,
        leading=22,
        alignment=TA_CENTER,
        spaceAfter=8 * mm
    )

    subtitulo = ParagraphStyle(
        "Subtitulo",
        parent=estilos["Heading2"],
        fontSize=11,
        leading=14,
        spaceBefore=3 * mm,
        spaceAfter=2 * mm
    )

    texto = ParagraphStyle(
        "Texto",
        parent=estilos["BodyText"],
        fontSize=9,
        leading=11
    )

    story = [
        Paragraph("FICHA DE PERSONAGEM — D&D 5.0", titulo)
    ]

    # Dados básicos
    dados_basicos = [
        [
            Paragraph("<b>Nome do personagem</b><br/>" + dados["personagem"], texto),
            Paragraph("<b>Nome do jogador</b><br/>" + dados["jogador"], texto)
        ],
        [
            Paragraph("<b>Raça</b><br/>" + dados["raca"], texto),
            Paragraph("<b>Classe</b><br/>" + dados["classe"], texto)
        ],
        [
            Paragraph("<b>Nível</b><br/>" + dados["nivel"], texto),
            Paragraph("<b>Alinhamento</b><br/>" + dados["alinhamento"], texto)
        ],
        [
            Paragraph("<b>Pontos de Vida</b><br/>" + str(dados["atributos"].get("Pontos de Vida", "")), texto),
            Paragraph("<b>Dados de Vida</b><br/>" + str(dados["atributos"].get("Dados de Vida", "")), texto),
            
        ],
        [
            Paragraph("<b>Classe de Armadura</b><br/>" + str(dados["atributos"].get("Classe de Armadura", "")), texto)
        ],
        [
            Paragraph("<b>Iniciativa</b><br/>" + str(dados["atributos"].get("Iniciativa", "")), texto)
        ]
    ]

    tabela = Table(dados_basicos, colWidths=[92 * mm, 92 * mm], rowHeights=[14 * mm] * 6)
    tabela.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.7, colors.black),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 3),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
    ]))

    story += [tabela, Spacer(1, 4 * mm)]

    # Background
    story += [Paragraph("BACKGROUND", subtitulo)]

    background = Table(
        [[Paragraph(dados["background"].replace("\n", "<br/>"), texto)]],
        colWidths=[184 * mm],
        rowHeights=[42 * mm]
    )
    background.setStyle(TableStyle([
        ("BOX", (0, 0), (-1, -1), 0.7, colors.black),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
    ]))
    story += [background, Spacer(1, 4 * mm)]

    # Atributos
    story += [Paragraph("ATRIBUTOS", subtitulo)]

    atributos_linha = []
    for atributo in ATRIBUTOS:
        valor = dados["atributos"].get(atributo, "")
        modficador = dados["modificador_atributos"].get(atributo, 0)
        if modficador >= 0:
            valor += f" (+{modficador})"
        else:
            valor += f" ({modficador})"
        atributos_linha.append(
            Paragraph(f"<b>{atributo.upper()}</b><br/><br/>{valor} ({modficador})", texto)
        )

    atributos = Table(
        [atributos_linha],
        colWidths=[30.6 * mm] * 6,
        rowHeights=[24 * mm]
    )
    atributos.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.7, colors.black),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))
    story += [atributos, Spacer(1, 5 * mm)]

    # Espaços adicionais para preenchimento manual
    story += [Paragraph("INFORMAÇÕES ADICIONAIS", subtitulo)]

    campos = [
        ("Classe de Armadura (CA)", 18),
        ("Iniciativa", 18),
        ("Deslocamento", 18),
        ("Pontos de Vida", 18),
        ("Dados de Vida", 18),
        ("Percepção Passiva", 18),
        ("Proficiências e Idiomas", 35),
        ("Perícias", 45),
        ("Equipamentos e Inventário", 50),
        ("Magias / Habilidades", 60),
        ("Características e Anotações", 65),
    ]

    for nome, altura in campos:
        bloco = Table(
            [[Paragraph(f"<b>{nome}</b>", texto)], [""]],
            colWidths=[184 * mm],
            rowHeights=[7 * mm, altura * mm]
        )
        bloco.setStyle(TableStyle([
            ("BOX", (0, 0), (-1, -1), 0.7, colors.black),
            ("LINEBELOW", (0, 0), (-1, 0), 0.7, colors.black),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 4),
            ("TOPPADDING", (0, 0), (-1, -1), 3),
        ]))
        story += [bloco, Spacer(1, 3 * mm)]

    doc.build(story)


def obter_dados():
    atributos = {
        atributo: entradas_atributos[atributo].get().strip()
        for atributo in ATRIBUTOS
    }

    p = personagem.Personagem(
        nome=entrada_personagem.get().strip(),
        raca=combo_raca.get(),
        classe=combo_classe.get(),
        nivel=entrada_nivel.get().strip(),
        background=texto_background.get("1.0", tk.END).strip(),
        alinhamento=entrada_alinhamento.get().strip(),
        forca=int(atributos["Força"]) if atributos["Força"].isdigit() else 0,
        destreza=int(atributos["Destreza"]) if atributos["Destreza"].isdigit() else 0,
        constituicao=int(atributos["Constituição"]) if atributos["Constituição"].isdigit() else 0,
        inteligencia=int(atributos["Inteligência"]) if atributos["Inteligência"].isdigit() else 0,
        sabedoria=int(atributos["Sabedoria"]) if atributos["Sabedoria"].isdigit() else 0,
        carisma=int(atributos["Carisma"]) if atributos["Carisma"].isdigit() else 0
    )

    return {
        "jogador": entrada_jogador.get().strip(),
        "personagem": p.nome,
        "raca": p.raca,
        "classe": p.classe,
        "nivel": p.nivel,
        "background": p.background,
        "alinhamento": p.alinhamento,
        "atributos": atributos,
        "Pontos de Vida": p.vida,
        "Dados de Vida": p.dado_de_vida,
        "Classe de Armadura": p.classe_armadura,
        "modificador_atributos": {
            "Força": p.modificador_forca,
            "Destreza": p.modificador_destreza,
            "Constituição": p.modificador_constituicao,
            "Inteligência": p.modificador_inteligencia,
            "Sabedoria": p.modificador_sabedoria,
            "Carisma": p.modificador_carisma
        }
    }


def gerar_ficha():
    dados = obter_dados()

    if not dados["personagem"]:
        messagebox.showwarning(
            "Campo obrigatório",
            "Informe pelo menos o nome do personagem."
        )
        return

    caminho = filedialog.asksaveasfilename(
        title="Salvar ficha de personagem",
        defaultextension=".pdf",
        filetypes=[("Arquivo PDF", "*.pdf")]
    )

    if not caminho:
        return

    try:
        gerar_pdf(dados, caminho)
        messagebox.showinfo(
            "Sucesso",
            f"Ficha criada com sucesso!\n\n{caminho}"
        )
    except Exception as erro:
        messagebox.showerror(
            "Erro",
            f"Não foi possível gerar o PDF:\n\n{erro}"
        )


# ---------------- INTERFACE ----------------

janela = tk.Tk()
janela.title("Gerador de Ficha D&D 5.0")
janela.geometry("650x720")
janela.minsize(600, 650)

frame = ttk.Frame(janela, padding=15)
frame.pack(fill="both", expand=True)

ttk.Label(
    frame,
    text="GERADOR DE FICHA — D&D 5.0",
    font=("TkDefaultFont", 16, "bold")
).grid(row=0, column=0, columnspan=4, pady=(0, 15))


def adicionar_campo(rotulo, linha, coluna, largura=25):
    ttk.Label(frame, text=rotulo).grid(
        row=linha, column=coluna, sticky="w", padx=5, pady=5
    )

    entrada = ttk.Entry(frame, width=largura)
    entrada.grid(
        row=linha, column=coluna + 1, sticky="ew", padx=5, pady=5
    )
    return entrada


frame.columnconfigure(1, weight=1)
frame.columnconfigure(3, weight=1)

entrada_jogador = adicionar_campo("Nome do jogador:", 1, 0)
entrada_personagem = adicionar_campo("Nome do personagem:", 1, 2)

ttk.Label(frame, text="Raça:").grid(
    row=2, column=0, sticky="w", padx=5, pady=5
)
combo_raca = ttk.Combobox(
    frame, values=RACAS, state="readonly", width=22
)
combo_raca.grid(row=2, column=1, sticky="ew", padx=5, pady=5)
combo_raca.set(RACAS[0])

ttk.Label(frame, text="Classe:").grid(
    row=2, column=2, sticky="w", padx=5, pady=5
)
combo_classe = ttk.Combobox(
    frame, values=CLASSES, state="readonly", width=22
)
combo_classe.grid(row=2, column=3, sticky="ew", padx=5, pady=5)
combo_classe.set(CLASSES[0])

entrada_nivel = adicionar_campo("Nível:", 3, 0)
entrada_alinhamento = adicionar_campo("Alinhamento:", 3, 2)

ttk.Label(
    frame,
    text="Background:"
).grid(row=4, column=0, columnspan=4, sticky="w", padx=5, pady=(10, 3))

texto_background = tk.Text(frame, height=7, wrap="word")
texto_background.grid(
    row=5, column=0, columnspan=4,
    sticky="nsew", padx=5, pady=(0, 10)
)

frame.rowconfigure(5, weight=1)

ttk.Label(
    frame,
    text="ATRIBUTOS",
    font=("TkDefaultFont", 11, "bold")
).grid(row=6, column=0, columnspan=4, pady=(5, 5))

frame_atributos = ttk.Frame(frame)
frame_atributos.grid(
    row=7, column=0, columnspan=4, sticky="ew", padx=5
)

entradas_atributos = {}

for indice, atributo in enumerate(ATRIBUTOS):
    coluna = indice % 3
    linha = indice // 3

    ttk.Label(
        frame_atributos,
        text=f"{atributo}:"
    ).grid(row=linha, column=coluna * 2, sticky="w", padx=(5, 2), pady=5)

    entrada = ttk.Entry(frame_atributos, width=10)
    entrada.grid(
        row=linha, column=coluna * 2 + 1,
        sticky="ew", padx=(2, 10), pady=5
    )

    entradas_atributos[atributo] = entrada

for coluna in range(6):
    frame_atributos.columnconfigure(coluna, weight=1)

ttk.Button(
    frame,
    text="GERAR FICHA EM PDF",
    command=gerar_ficha
).grid(
    row=8, column=0, columnspan=4,
    pady=20, ipadx=20, ipady=8
)

janela.mainloop()
