# pintando parede
larg = float(input('Qual é a largura da parede que você deseja pintar?'))
alt = float(input('E qual é a altura desta mesma parede?'))
area = float((larg*alt))
tinta = float((area/2))
print('Você precisará pintar {} m² de área de parede\nE para isso precisará usar {} L de tinta'.format(area, tinta))
