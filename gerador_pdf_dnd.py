from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.units import mm


ATRIBUTOS = [
    "Força",
    "Destreza",
    "Constituição",
    "Inteligência",
    "Sabedoria",
    "Carisma"
]


def gerar_ficha(dados, caminho_pdf):
    """
    Gera uma ficha de personagem de D&D 5.0 em PDF.

    Parâmetros:
        dados (dict):
            Dicionário contendo os dados preenchidos pelo usuário.

            Exemplo:
            {
                "jogador": "João",
                "personagem": "Thorin",
                "raca": "Anão",
                "classe": "Guerreiro",
                "nivel": "5",
                "background": "Soldado...",
                "alinhamento": "Leal e Bom",
                "atributos": {
                    "Força": "16",
                    "Destreza": "12",
                    "Constituição": "15",
                    "Inteligência": "10",
                    "Sabedoria": "11",
                    "Carisma": "13"
                }
            }

        caminho_pdf (str):
            Caminho onde o arquivo PDF será salvo.
    """

    doc = SimpleDocTemplate(
        caminho_pdf,
        pagesize=A4,
        rightMargin=12 * mm,
        leftMargin=12 * mm,
        topMargin=12 * mm,
        bottomMargin=12 * mm
    )

    estilos = getSampleStyleSheet()

    titulo = ParagraphStyle(
        "TituloFicha",
        parent=estilos["Title"],
        fontSize=18,
        leading=22,
        alignment=TA_CENTER,
        spaceAfter=8 * mm
    )

    subtitulo = ParagraphStyle(
        "SubtituloFicha",
        parent=estilos["Heading2"],
        fontSize=11,
        leading=14,
        spaceBefore=3 * mm,
        spaceAfter=2 * mm
    )

    texto = ParagraphStyle(
        "TextoFicha",
        parent=estilos["BodyText"],
        fontSize=9,
        leading=11
    )

    story = []

    # ---------------------------------------------------------
    # TÍTULO
    # ---------------------------------------------------------

    story.append(
        Paragraph("FICHA DE PERSONAGEM — D&D 5.0", titulo)
    )

    # ---------------------------------------------------------
    # DADOS BÁSICOS
    # ---------------------------------------------------------

    dados_basicos = [
        [
            Paragraph(
                "<b>Nome do personagem</b><br/>"
                + str(dados.get("personagem", "")),
                texto
            ),
            Paragraph(
                "<b>Nome do jogador</b><br/>"
                + str(dados.get("jogador", "")),
                texto
            )
        ],
        [
            Paragraph(
                "<b>Raça</b><br/>"
                + str(dados.get("raca", "")),
                texto
            ),
            Paragraph(
                "<b>Classe</b><br/>"
                + str(dados.get("classe", "")),
                texto
            )
        ],
        [
            Paragraph(
                "<b>Nível</b><br/>"
                + str(dados.get("nivel", "")),
                texto
            ),
            Paragraph(
                "<b>Alinhamento</b><br/>"
                + str(dados.get("alinhamento", "")),
                texto
            )
        ]
    ]

    tabela_dados = Table(
        dados_basicos,
        colWidths=[92 * mm, 92 * mm],
        rowHeights=[14 * mm] * 3
    )

    tabela_dados.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.7, colors.black),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 3),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
    ]))

    story.append(tabela_dados)
    story.append(Spacer(1, 4 * mm))

    # ---------------------------------------------------------
    # BACKGROUND
    # ---------------------------------------------------------

    story.append(
        Paragraph("BACKGROUND", subtitulo)
    )

    background = str(dados.get("background", ""))
    background = background.replace("\n", "<br/>")

    tabela_background = Table(
        [[Paragraph(background, texto)]],
        colWidths=[184 * mm],
        rowHeights=[42 * mm]
    )

    tabela_background.setStyle(TableStyle([
        ("BOX", (0, 0), (-1, -1), 0.7, colors.black),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
    ]))

    story.append(tabela_background)
    story.append(Spacer(1, 4 * mm))

    # ---------------------------------------------------------
    # ATRIBUTOS
    # ---------------------------------------------------------

    story.append(
        Paragraph("ATRIBUTOS", subtitulo)
    )

    valores_atributos = dados.get("atributos", {})

    atributos_linha = []

    for atributo in ATRIBUTOS:
        valor = valores_atributos.get(atributo, "")

        atributos_linha.append(
            Paragraph(
                f"<b>{atributo.upper()}</b><br/><br/>{valor}",
                texto
            )
        )

    tabela_atributos = Table(
        [atributos_linha],
        colWidths=[30.6 * mm] * 6,
        rowHeights=[24 * mm]
    )

    tabela_atributos.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.7, colors.black),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))

    story.append(tabela_atributos)
    story.append(Spacer(1, 5 * mm))

    # ---------------------------------------------------------
    # ESPAÇOS PARA PREENCHIMENTO MANUAL
    # ---------------------------------------------------------

    story.append(
        Paragraph("INFORMAÇÕES ADICIONAIS", subtitulo)
    )

    campos_manuais = [
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

    for nome, altura in campos_manuais:

        bloco = Table(
            [
                [Paragraph(f"<b>{nome}</b>", texto)],
                [""]
            ],
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

        story.append(bloco)
        story.append(Spacer(1, 3 * mm))

    # ---------------------------------------------------------
    # GERAÇÃO DO PDF
    # ---------------------------------------------------------

    doc.build(story)
