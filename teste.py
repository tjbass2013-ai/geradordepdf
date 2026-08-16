import racas_especify

raca = racas_especify.calcraca("Anão")
consti = 15 + raca["aumento_habilidade"]

print(f"""

   Deslocamento: {raca["deslocamento"]},
   Visão: {raca["visao"]},
   Combate: {raca["proficiencia_combate"]},
   Constituição: {consti}

""")
