from opencage.geocoder import OpenCageGeocode
from tkinter import *


def get_coordinates(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city, language="ru")
        if results:
            lat = round(results[0]['geometry']['lat'], 3)
            lng = round(results[0]['geometry']['lng'], 3)
            return f"Широта: {lat}, Долгота: {lng}"
        else:
            print("Город не найден")
    except Exception as e:
        return f"Возникла ошибка: {e}"


def show_coordinates(event=None):
    city = entry.get()
    coordinates = get_coordinates(city, key)
    label.config(text=f"Координаты города {city}:\n\n{coordinates}")



key = 'ded53afb91d247f0b95e30693ec37983'

window = Tk()
window.title("Координаты городов")
window.geometry("320x160")

entry = Entry()
entry.pack()
entry.bind("<Return>", show_coordinates)

button = Button(text="Поиск координат", command=show_coordinates)
button.pack()

label = Label(text="Введите город и нажмите кнопку")
label.pack()

window.mainloop()
