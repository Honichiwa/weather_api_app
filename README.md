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

### Configure Redis
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
