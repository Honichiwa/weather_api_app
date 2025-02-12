# Weather API App 🌦️ with **Redis** caching

A simple weather forecasting web application built with **Django** and **Redis** The app fetches weather data from Open-Meteo and caches responses for better performance.

## Features 🚀
- Search weather data by city
- Fetches temperature, precipitation, and probability of precipitation
- Caches API responses using **Redis** for improved speed
- Displays results in a simple Django template

## Tech Stack 🛠️
- **Backend:** Django, Python
- **Caching:** Redis
- **API:** Open-Meteo and Nominatim
- **Frontend:** Django Templates

## Setup & Installation ⚙️

### Prerequisites
- Python 3.x
- Redis Server
- Virtual Environment (recommended)

### Clone the Repository
```sh
git clone https://github.com/Honichiwa/weather_api_app.git
cd weather_api_app
```

### Create & Activate Virtual Environment
```sh
python -m venv venv  # Create virtual environment
source venv/bin/activate  # Activate on Mac/Linux
venv\Scripts\activate  # Activate on Windows
```

### Install Dependencies
```sh
pip install -r requirements.txt
```


### Create and update local_settings.py file
Create `local_settings.py` file in `weather_app/weather_app` next to django `settings.py`

Make django secret key:
```sh
django-admin shell
```
```sh
from django.core.management.utils import get_random_secret_key  
get_random_secret_key()
```
Copy generated secret key to `local_settings.py`:
```python
SECRET_KEY = "(your_generated_random_secret_key)"
```
Add rest of needed constants such as Headers for api and redis_psw, redis_host, redis_port if you are using Redis cloud:
```python
HEADERS = {'User-Agent' : 'your_project_name (your_email@email.com)'}

REDIS_PSW = '*******'

REDIS_HOST = '*****'

REDIS_PORT = *****
```

### Configure Redis for local server

Make sure you have a running Redis server. -> https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/

Update `settings.py` with your Redis configuration:
```python
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}
```

### Configure Redis for Redis cloud

Update `settings.py` with your Redis configuration:
```python
CACHES = {
        'default': {
            'BACKEND': 'django_redis.cache.RedisCache',
            #location = your redis cloud url + port
            "LOCATION": f"redis://{local_settings.REDIS_HOST}:{local_settings.REDIS_PORT}/0",
            'OPTIONS': {
                #Your redis cloud database given username which is "default" by default
                #and redis cloud database password which u can find on the database dashoard
                #IMPORTNANT ! make sure to pass them both as str() even if they already are in str format
                'USERNAME': str("default"),
                'PASSWORD': str(local_settings.REDIS_PSW),
                'DB': 0,
        }
    }
}
```

### Run the Server
```sh
python manage.py migrate  # Apply migrations
python manage.py runserver  # Start the Django server
```

Visit **http://127.0.0.1:8000/** in your browser.

## Usage 📝
- Enter a city name in the search bar
- Get weather data including temperature and precipitation
- Cached results improve performance on repeated searches

## To-Do ✅
- [ ] Add unit tests
- [ ] Improve UI with better styling
- [ ] Add more weather parameters
- [ ] Deploy to a cloud server

## Contributing 🤝
Feel free to fork the repo and submit a pull request!
