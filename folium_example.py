import folium
from folium import plugins
from folium.plugins import MarkerCluster
from folium.plugins import FastMarkerCluster


m = folium.Map([40.0690994, 45.0381889], zoom_start=8)

url = r'C:/Users/arturp/Downloads/mygeodata/gadm36_ARM_1.geojson'
stripes = plugins.pattern.StripePattern(angle=-45)
stripes.add_to(m)

circles = plugins.pattern.CirclePattern(width=20, height=20, radius=5, fill_opacity=0.5, opacity=1)
circles.add_to(m)

def style_function(feature):
    default_style = {
        'opacity':1.0,
        'fillColor': 'green',
        'color': 'black',
        'weight': 3
    }
        
    if feature['properties']['name']  == 'Colorado':
        default_style['fillPattern'] = stripes
        default_style['fillOpacity'] = 1.0
        
    if feature['properties']['name']  == 'Utah':
        default_style['fillPattern'] = circles
        default_style['fillOpacity'] = 1.0
        
    return default_style
	





folium.Marker([40.1655693, 44.2946205], popup='<i>Mt. Hood Meadows</i>').add_to(m)


# Adding remote GeoJSON as additional layer.
folium.GeoJson(url, smooth_factor=0.5, style_function=style_function).add_to(m)


m.save('index.html')


