# Criador de rotinas
# A rotina é nada mais nada menos que uma lista com 7 listas organizadas

days = ['segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado', 'domingo']
new_routine = []

for i in range(6):
    num = int(input(f'Digite o número de atividades na rotina para {days[i]}:\n'))
    for j in range (num):
        day = []
        activity = input(f'Digite a atividade número {j+1}:\n')
        day.append(activity)
    new_routine.append(day)

print(new_routine)