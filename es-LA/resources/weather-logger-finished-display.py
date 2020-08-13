import pygal

temp = []

archivo = open ('weather.txt', 'r')

for linea in archivo.read().splitlines():
  if linea:
    temp.append( float(linea) )
archivo.close()

weatherchart = pygal.Line ()
weatherchart.title = 'Temperatura'
weatherchart.x_labels = range (1, len (temp) + 1)
weatherchart.add ('temp', temp)
weatherchart.render ()

