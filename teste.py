import personagem

p = personagem.Personagem("John", "Halfling", "Barbaro", 1, "Nenhum", "Neutro", 15, 15, 15, 15, 15, 15)

print(f"Nome: {p.nome}")
print(f"Raça: {p.raca}")
print(f"Classe: {p.classe}")
print(f"Nível: {p.nivel}")
print(f"Vida: {p.vida}")
print(f"Classe de Armadura: {p.classe_armadura}")
print(f"Dado de Vida: {p.dado_de_vida}")
print(f"Atributos e modificadores: Força: {p.forca} mod: {p.modificador_forca}, Destreza: {p.destreza} mod: {p.modificador_destreza}, Constituição: {p.constituicao} mod: {p.modificador_constituicao}, Inteligência: {p.inteligencia} mod: {p.modificador_inteligencia}, Sabedoria: {p.sabedoria} mod: {p.modificador_sabedoria}, Carisma: {p.carisma} mod: {p.modificador_carisma}")

print(f"Deslocamento: {p.deslocamento}")
print(f"Vantagem: {p.vantagem}")
print(f"Visão: {p.visao}")
print(f"Proficiência em Combate: {p.proficiencia_combate}")
print(f"Proficiência em Ferramentas: {p.proficiencia_ferramenta}")
print(f"Especialização: {p.especializacao}")
print(f"Idiomas: {p.idiomas}")
