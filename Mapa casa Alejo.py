import folium
import webbrowser

longitud = -74.106866
latitud = 4.820827

mapa = folium.Map(location=[latitud, longitud], zoom_start=17)


icon_rojo = folium.Icon(color='red')


folium.Marker([latitud, longitud], popup="Mi casa", icon=icon_rojo).add_to(mapa)

folium.raster_layers.TileLayer(
    tiles="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
    attr="Esri, DigitalGlobe, GeoEye, Earthstar Geographics, CNES/Airbus DS, USDA, USGS, AEX, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community",
    name="Satellite",
    overlay=True,
    control=True
).add_to(mapa)

mapa.save("mapa.html")

url = "mapa.html"
webbrowser.open(url)