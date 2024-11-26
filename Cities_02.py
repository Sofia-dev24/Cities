from opencage.geocoder import OpenCageGeocode
from tkinter import *
import webbrowser


def get_coordinates(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city, language="ru")
        if results:
            lat = round(results[0]['geometry']['lat'], 3)
            lng = round(results[0]['geometry']['lng'], 3)
            country = results[0]['components']['country']
            currency = results[0]['annotations']['currency']['name']
            osm_url = f"https://openstreetmap.org/?mlat={lat}&mlng={lng}"
            if "state" in results[0]['components']:
                region = results[0]['components']['state']
                return {
                    "coordinates": f"Широта: {lat}, Долгота: {lng}\nСтрана: {country}, Регион: {region}\n"
                                   f"Валюта: {currency}", "map_url": osm_url
                }
            else:
                return {
                    "coordinates": f"Широта: {lat}, Долгота: {lng}\nСтрана: {country}\nВалюта: {currency}",
                    "map_url": osm_url
                }
        else:
            print("Город не найден")
    except Exception as e:
        return f"Возникла ошибка: {e}"


def show_coordinates(event=None):
    global map_url
    city = entry.get()
    result = get_coordinates(city, key)
    label.config(text=f"Координаты города {city}:\n\n{result['coordinates']}")
    map_url = result["map_url"]


def show_map():
    if map_url:
        webbrowser.open(map_url)


def clear():
    entry.delete(0, END)


key = 'ded53afb91d247f0b95e30693ec37983'
map_url = ""

window = Tk()
window.title("Координаты городов")
window.geometry("500x250")

entry = Entry(width=25)
entry.pack(pady=10)
entry.bind("<Return>", show_coordinates)

button = Button(width=12, text="Поиск координат", command=show_coordinates)
button.pack()

label = Label(text="Введите город и нажмите кнопку")
label.pack(pady=10)

map_button = Button(width=12, text="Показать карту", command=show_map)
map_button.pack()

clear_button = Button(width=12, text="Очистить", command=clear)
clear_button.pack()

window.mainloop()
