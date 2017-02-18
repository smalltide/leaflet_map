import folium
import pandas

df = pandas.read_csv('Volcanoes-USA.txt')

map = folium.Map(location = [df['LAT'].mean(), df['LON'].mean()], zoom_start = 4, tiles = 'Mapbox Bright' )

def color(elev):
    minimum = int(df['ELEV'].min())
    step = int((df['ELEV'].max() - df['ELEV'].min()) / 3)

    if elev in range(minimum, minimum + step):
        col = 'green'
    elif elev in range(minimum + step, minimum + step * 2):
        col = 'orange'
    else:
        col = 'red'
    return col

for lat, lon, name, elev in zip(df['LAT'], df['LON'], df['NAME'], df['ELEV']):
    map.add_child(folium.Marker(location = [lat, lon], popup = name, icon=folium.Icon(color(elev))))

map.add_child(folium.GeoJson(
    data = open('world.json'),
    name = 'World population',
    style_function = lambda x: { 'fillColor': 'green' if int(x['properties']['POP2005']) <= 10000000 else 'orange' if 10000000 < int(x['properties']['POP2005']) < 20000000 else 'red' }
))

map.save(outfile = 'test.html')
