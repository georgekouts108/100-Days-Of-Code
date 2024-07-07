from datetime import datetime
import requests
import os

NUTR_APP_ID = os.environ['NUTR_APP_ID']
NUTR_API_KEY = os.environ['NUTR_API_KEY']

ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'

HEADERS = {
    'x-app-id': NUTR_APP_ID,
    'x-app-key': NUTR_API_KEY
}

PARAMS = {
    'query': input("What exercise did you do today: "),
    'gender': 'male',
    'weight_kg': 75,
    'height_cm': 173,
    'age': 26
}

response = requests.post(url=ENDPOINT, json=PARAMS, headers=HEADERS)
result = response.json()

exercises = result['exercises'][0]
exercise_type = str(exercises['user_input'])
exercise_type = (exercise_type[:-2] + 'ing').title()
exercise_duration = int(exercises['duration_min'])
exercise_calories = float(exercises['nf_calories'])

SHEETY_API_KEY = os.environ['SHEETY_API_KEY']
SHEETY_API = f'https://api.sheety.co/{SHEETY_API_KEY}/myWorkouts2/workouts'
SHEETY_USERNAME = os.environ['SHEETY_USERNAME']
SHEETY_PWD = os.environ['SHEETY_PWD']

date = datetime.now().strftime('%d/%m/%Y')
time = str(datetime.now().time())
time = time[:time.index('.')]

data_entry = {
    'workout': {
        'date': date,
        'time': time,
        'exercise': exercise_type,
        'duration': exercise_duration,
        'calories': exercise_calories
    }
}

# response2 = requests.get(url=SHEETY_API)
response3 = requests.post(url=SHEETY_API, json=data_entry, auth=(SHEETY_USERNAME, SHEETY_PWD))
print(response3.text)
