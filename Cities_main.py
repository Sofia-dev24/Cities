from opencage.geocoder import OpenCageGeocode


def get_coordinates(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city, language="ru")
        if results:
            lat = round(results[0]['geometry']['lat'], 3)
            lng = round(results[0]['geometry']['lng'], 3)
            return lat, lng
        else:
            print("Город не найден")
    except Exception as e:
        return f"Возникла ошибка: {e}"


key = 'ded53afb91d247f0b95e30693ec37983'
city = "Екатеринбург"
coordinates = get_coordinates(city, key)

print(f"Координаты города {city}: {coordinates}.")
