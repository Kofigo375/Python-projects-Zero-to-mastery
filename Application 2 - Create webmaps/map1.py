import folium 
map = folium.Map(location=[6.6764693847403125, -1.5408876721323577])


## adding a marker multiple markers

fg = folium.FeatureGroup(name='My group')
for coordinates in [[6.4, -1.4],[6.5, -1.5],[6.6, -1.7]]:
    map.add_child(folium.Marker(location=coordinates, popup='Hi I am a marker', icon=folium.Icon(color='green')))
map.add_child(fg)




map.save("Map3.html")

