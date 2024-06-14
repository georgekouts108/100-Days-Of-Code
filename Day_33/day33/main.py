import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
status = response.status_code
if status == 200:
    print("200 - Success")
    data = response.json()  # will be a dictionary
    lat, lng = (data['iss_position']['latitude'], data['iss_position']['longitude'])
    print(f"Lat: {lat}, Lng: {lng}")
else:
    print(f"{status} - Error")
    response.raise_for_status()
