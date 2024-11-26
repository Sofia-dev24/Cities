from opencage.geocoder import OpenCageGeocode


def get_coordinates(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city, language="ru")
        if results:
            return results[0]['geometry']['lat'], results[0]['geometry']['lng']
        else:
            print("Город не найден")
    except Exception as e:
        return f"Возникла ошибка: {e}"


key = 'ded53afb91d247f0b95e30693ec37983'
city = "London"
coordinates = get_coordinates(city, key)

print(f"Координаты города {city}: {coordinates}.")

