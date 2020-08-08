import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
#print(data)

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_prod(elev):
	if(elev<2000):
			return "green"
	elif(elev>2000 and el<4000):
			return "orange"
	elif(elev>4000):
			return "red"


map = folium.Map(location=[48,-121], zoom_start = 6, tiles = "Stamen Terrain")

fgp = folium.FeatureGroup(name = 'Population')

fgp.add_child(folium.GeoJson(data = open("world.json", 'r', encoding="utf-8-sig").read(), 
style_function =lambda x:{'fill_color':"blue" if x["properties"]["POP2005"]<10000000
else "yellow" if 10000000 <= x["properties"]["POP2005"]<20000000
else "red" }))

fgv = folium.FeatureGroup(name = 'Volcanoes')

for lt,ln,el in zip(lat, lon, elev):
		fgv.add_child(folium.CircleMarker(location=[lt, ln], popup = str(el)+ " m",radius=10,  fill_color=color_prod(el), color="grey", fill_opacity=0.7))


map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")


