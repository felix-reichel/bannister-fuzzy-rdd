import pandas as pd

# See: https://en.wikipedia.org/wiki/5000_metres_world_record_progression
data = [
    {"date": "1912-07-10", "time": 14*60 + 36.6, "athlete": "Hannes Kolehmainen", "country": "FIN", "location": "Stockholm, Sweden"},
    {"date": "1922-09-12", "time": 14*60 + 35.4, "athlete": "Paavo Nurmi", "country": "FIN", "location": "Stockholm, Sweden"},
    {"date": "1924-06-19", "time": 14*60 + 28.2, "athlete": "Paavo Nurmi", "country": "FIN", "location": "Helsinki, Finland"},
    {"date": "1932-06-19", "time": 14*60 + 17.0, "athlete": "Lauri Lehtinen", "country": "FIN", "location": "Helsinki, Finland"},
    {"date": "1939-06-16", "time": 14*60 + 8.8, "athlete": "Taisto Mäki", "country": "FIN", "location": "Helsinki, Finland"},
    {"date": "1942-09-20", "time": 13*60 + 58.2, "athlete": "Gunder Hägg", "country": "SWE", "location": "Gothenburg, Sweden"},
    {"date": "1954-05-30", "time": 13*60 + 57.2, "athlete": "Emil Zátopek", "country": "TCH", "location": "Paris, France"},
    {"date": "1954-08-29", "time": 13*60 + 56.6, "athlete": "Vladimir Kuts", "country": "URS", "location": "Bern, Switzerland"},
    {"date": "1954-10-13", "time": 13*60 + 51.6, "athlete": "Chris Chataway", "country": "GBR", "location": "London, United Kingdom"},
    {"date": "1954-10-23", "time": 13*60 + 51.2, "athlete": "Vladimir Kuts", "country": "URS", "location": "Prague, Czechoslovakia"},
    {"date": "1955-09-10", "time": 13*60 + 50.8, "athlete": "Sandor Iharos", "country": "HUN", "location": "Budapest, Hungary"},
    {"date": "1955-09-18", "time": 13*60 + 46.8, "athlete": "Vladimir Kuts", "country": "URS", "location": "Belgrad, Yugoslavia"},
    {"date": "1955-10-23", "time": 13*60 + 40.6, "athlete": "Sandor Iharos", "country": "HUN", "location": "Budapest, Hungary"},
    {"date": "1956-06-19", "time": 13*60 + 36.8, "athlete": "Gordon Pirie", "country": "GBR", "location": "Bergen, Norway"},
    {"date": "1957-10-13", "time": 13*60 + 35.0, "athlete": "Vladimir Kuts", "country": "URS", "location": "Rome, Italy"},
    {"date": "1965-01-16", "time": 13*60 + 34.8, "athlete": "Ron Clarke", "country": "AUS", "location": "Hobart, Australia"},
    {"date": "1965-02-01", "time": 13*60 + 33.6, "athlete": "Ron Clarke", "country": "AUS", "location": "Auckland, New Zealand"},
    {"date": "1965-06-04", "time": 13*60 + 25.8, "athlete": "Ron Clarke", "country": "AUS", "location": "Compton, USA"},
    {"date": "1965-11-30", "time": 13*60 + 24.2, "athlete": "Kipchoge Keino", "country": "KEN", "location": "Auckland, New Zealand"},
    {"date": "1966-07-05", "time": 13*60 + 16.6, "athlete": "Ron Clarke", "country": "AUS", "location": "Stockholm, Sweden"},
    {"date": "1972-09-14", "time": 13*60 + 16.4, "athlete": "Lasse Virén", "country": "FIN", "location": "Helsinki, Finland"},
    {"date": "1972-09-20", "time": 13*60 + 13.0, "athlete": "Emiel Puttemans", "country": "BEL", "location": "Brussels, Belgium"},
    {"date": "1977-07-05", "time": 13*60 + 12.9, "athlete": "Dick Quax", "country": "NZL", "location": "Stockholm, Sweden"},
    {"date": "1978-04-08", "time": 13*60 + 8.4, "athlete": "Henry Rono", "country": "KEN", "location": "Berkeley, California, USA"},
    {"date": "1981-09-13", "time": 13*60 + 6.20, "athlete": "Henry Rono", "country": "KEN", "location": "Knarvik, Norway"},
    {"date": "1982-07-07", "time": 13*60 + 0.41, "athlete": "David Moorcroft", "country": "GBR", "location": "Oslo, Norway"},
    {"date": "1985-07-22", "time": 13*60 + 0.40, "athlete": "Saïd Aouita", "country": "MAR", "location": "Oslo, Norway"},
    {"date": "1987-07-27", "time": 12*60 + 58.39, "athlete": "Saïd Aouita", "country": "MAR", "location": "Rome, Italy"},
    {"date": "1994-06-04", "time": 12*60 + 56.96, "athlete": "Haile Gebrselassie", "country": "ETH", "location": "Hengelo, Netherlands"},
    {"date": "1995-06-08", "time": 12*60 + 55.30, "athlete": "Moses Kiptanui", "country": "KEN", "location": "Rome, Italy"},
    {"date": "1995-08-16", "time": 12*60 + 44.39, "athlete": "Haile Gebrselassie", "country": "ETH", "location": "Zürich, Switzerland"},
    {"date": "1997-08-13", "time": 12*60 + 41.86, "athlete": "Haile Gebrselassie", "country": "ETH", "location": "Zürich, Switzerland"},
    {"date": "1997-08-22", "time": 12*60 + 39.74, "athlete": "Daniel Komen", "country": "KEN", "location": "Brussels, Belgium"},
    {"date": "1998-06-13", "time": 12*60 + 39.36, "athlete": "Haile Gebrselassie", "country": "ETH", "location": "Helsinki, Finland"},
    {"date": "2004-05-31", "time": 12*60 + 37.35, "athlete": "Kenenisa Bekele", "country": "ETH", "location": "Hengelo, Netherlands"},
    {"date": "2020-08-14", "time": 12*60 + 35.36, "athlete": "Joshua Cheptegei", "country": "UGA", "location": "Monaco"},
]

df = pd.DataFrame(data)
df.to_csv('5000m_world_records.csv', index=False, sep=";")
