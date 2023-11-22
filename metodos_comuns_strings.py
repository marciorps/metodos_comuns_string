nome_curso = "Edição de video"
print(nome_curso.upper())
print(nome_curso.lower())
print(nome_curso.strip())
print(nome_curso.lstrip())
print(nome_curso.rstrip())
print(nome_curso.find('ção'))
print(nome_curso.replace('Video', 'Música'))
print('https://sc.olx.com.br/?o=90&q=relogio'.replace('relogio', 'carro'))


# Desafio
##  Através da criação de strings dinâmicos e os métodos de um string qua acabou de aprender, use com base as variáveis a seguir para criar as seguintes frases

a ='é'
b = 'MELHOR'
c = 'QUE'
d = 'feito'
e = 'perfeito'

print('É melhor FEITO que PERFEITO')
print(f'{a.upper()} {b.lower()} {d.upper()} {c.lower()} {e.upper()}')