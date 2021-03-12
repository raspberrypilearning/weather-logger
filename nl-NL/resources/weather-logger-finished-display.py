import pygal

temp = []

bestand = open('weather.txt', 'r')

for regel in bestand.read().splitlines():
  if regel:
    temp.append( float(regel) )
bestand.close()

weergrafiek = pygal.Line()
weergrafiek.title = 'Weer'
weergrafiek.x_labels = range(1, len(temp) + 1)
weergrafiek.add('temp', temp)
weergrafiek.render()

