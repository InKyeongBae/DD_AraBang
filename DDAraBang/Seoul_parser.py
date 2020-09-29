import requests
import sys
import os
import json 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
import django
django.setup()
from review.models import SeoulLatLngMark, Gu

# def FindLatLng(Keyword):
    # URL 로 가져오기 


# def FindLatLng(Keyword):
#     #249 전국 지역 
#     #각 지역 검색

#     for i in range(len(data["features"])):
#         if data["features"][i]["properties"]["SIG_KOR_NM"] == Keyword :
#             LatLng_datas = data["features"][i]["geometry"]["coordinates"][0]

#             for i in range(len(LatLng_datas)):
#                 SeoulLatLngMark.objects.update_or_create(
#                     name=Keyword,
#                     lat = LatLng_datas[i][1],
#                     lng = LatLng_datas[i][0], 
#                     )


# FindLatLng("강서구")

# def FindLatLng():
#     with open('DDAraBang/seoul_line.json', 'rt', encoding="UTF8") as json_file:
#         data = json.load(json_file)
#         # print(data['features'][1]['properties']['name'])
#         for i in range(len(data['features'])):
#             LatLngDatas = data['features'][i]['geometry']['coordinates'][0]
#             gu_names = data['features'][i]['properties']['name']

#             for i in range(len(LatLngDatas)):
#                 SeoulLatLngMark.objects.update_or_create(
#                     gu_name = Gu.objects.get(gu=gu_names),
#                     lat = LatLngDatas[i][1],
#                     lng = LatLngDatas[i][0],            
#                 )

# FindLatLng()