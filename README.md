**Morning-CLI**

Command line interface to show the weather in your city.

**Install**
```bash
git clone git@github.com:Peskoo/morning-cli.git
cd morning-cli
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

**Config API**
Visit [OpenWeatherMAP](https://openweathermap.org/price) and sign up for free.
Then copy the api key you received in your inbox mail.

```bash
source .venv/bin/activate
export API_KEY='YOUR_API_KEY'
```

**Commands**
- Show now
  `morning.py --city/-c YOUR_CITY`
- Search a city
  `morning.py all`
