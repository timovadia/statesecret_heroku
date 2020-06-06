# -*- coding: utf-8 -*-
from django.http import HttpResponse
import datetime
import folium


def main(request):
    nowTime = datetime.datetime.now()
    nowTime = nowTime.strftime("%m-%B-%Y %H:%M:%S")
    html = "<html><body>%s. Это главная страница {main_page}!</body></html>" % nowTime
    return HttpResponse(html)


def hello(request):
    return HttpResponse("Большой брат приветствует тебя!")


def map(request):
    my_map = folium.Map(location=[45.5236, -122.6750], zoom_start=2, tiles='Stamen Toner')
    # tooltip = 'Click me!'
    # folium.Marker([45.5806, -122.6015], popup='<i>Marker 1.</i>', tooltip=tooltip).add_to(my_map)
    # folium.Marker([45.5488, -122.9545], popup='<b>Marker 2.</b>', tooltip=tooltip).add_to(my_map)
    folium.TileLayer('stamentoner').add_to(my_map)
    folium.TileLayer('openstreetmap').add_to(my_map)
    folium.TileLayer('stamenterrain').add_to(my_map)
    # folium.TileLayer('cartodbdark_matter').add_to(my_map)
    # folium.TileLayer('stamenwatercolor').add_to(my_map)

    folium.LayerControl().add_to(my_map)
    html = my_map.get_root().render()
    return HttpResponse(html)
