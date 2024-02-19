import folium 
import pandas

## loading data with pandas
data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elev):
    if elev < 1000:
        return 'green'
    elif 1000<= elev < 3000:
        return 'orange'
    else:
        return 'red'


map = folium.Map(location=[6.6764693847403125, -1.5408876721323577])


## adding a marker multiple markers

fg = folium.FeatureGroup(name='My group')

## we iterate through 2 lists simultaneously we use the "zip" method
for lat,lon,el in zip(lat, lon, elev):
    map.add_child(folium.Marker(location=[lat, lon], popup=str(el), icon=folium.Icon(color=color_producer(el))))
map.add_child(fg)




map.save("Map3.html")

