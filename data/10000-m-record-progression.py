# See: https://en.wikipedia.org/wiki/10,000_metres_world_record_progression

import pandas as pd

data_10k = [
    {"date": "1911-11-16", "time": 30*60 + 58.8, "athlete": "Jean Bouin", "country": "FRA", "location": "Paris, France"},
    {"date": "1921-06-22", "time": 30*60 + 40.2, "athlete": "Paavo Nurmi", "country": "FIN", "location": "Stockholm, Sweden"},
    {"date": "1924-05-25", "time": 30*60 + 35.4, "athlete": "Ville Ritola", "country": "FIN", "location": "Helsinki, Finland"},
    {"date": "1924-07-06", "time": 30*60 + 23.2, "athlete": "Ville Ritola", "country": "FIN", "location": "Paris, France"},
    {"date": "1924-08-31", "time": 30*60 + 6.2, "athlete": "Paavo Nurmi", "country": "FIN", "location": "Kuopio, Finland"},
    {"date": "1937-07-18", "time": 30*60 + 5.6, "athlete": "Ilmari Salminen", "country": "FIN", "location": "Kouvola, Finland"},
    {"date": "1938-09-29", "time": 30*60 + 2.0, "athlete": "Taisto Mäki", "country": "FIN", "location": "Tampere, Finland"},
    {"date": "1939-09-17", "time": 29*60 + 52.6, "athlete": "Taisto Mäki", "country": "FIN", "location": "Helsinki, Finland"},
    {"date": "1944-08-25", "time": 29*60 + 35.4, "athlete": "Viljo Heino", "country": "FIN", "location": "Helsinki, Finland"},
    {"date": "1949-06-11", "time": 29*60 + 28.2, "athlete": "Emil Zátopek", "country": "TCH", "location": "Ostrava, Czech Republic"},
    {"date": "1949-09-01", "time": 29*60 + 27.2, "athlete": "Viljo Heino", "country": "FIN", "location": "Kouvola, Finland"},
    {"date": "1949-10-22", "time": 29*60 + 21.2, "athlete": "Emil Zátopek", "country": "TCH", "location": "Ostrava, Czech Republic"},
    {"date": "1950-08-04", "time": 29*60 + 2.6, "athlete": "Emil Zátopek", "country": "TCH", "location": "Turku, Finland"},
    {"date": "1953-11-01", "time": 29*60 + 1.6, "athlete": "Emil Zátopek", "country": "TCH", "location": "Stara Boleslav, Czech Republic"},
    {"date": "1954-06-01", "time": 28*60 + 54.2, "athlete": "Emil Zátopek", "country": "TCH", "location": "Brussels, Belgium"},
    {"date": "1956-07-15", "time": 28*60 + 42.8, "athlete": "Sandor Iharos", "country": "HUN", "location": "Budapest, Hungary"},
    {"date": "1956-09-11", "time": 28*60 + 30.4, "athlete": "Vladimir Kuts", "country": "URS", "location": "Moscow, Soviet Union"},
    {"date": "1960-10-15", "time": 28*60 + 18.8, "athlete": "Pyotr Bolotnikov", "country": "URS", "location": "Kiev, Soviet Union"},
    {"date": "1962-08-11", "time": 28*60 + 18.2, "athlete": "Pyotr Bolotnikov", "country": "URS", "location": "Moscow, Soviet Union"},
    {"date": "1963-12-18", "time": 28*60 + 15.6, "athlete": "Ron Clarke", "country": "AUS", "location": "Melbourne, Australia"},
    {"date": "1965-07-14", "time": 27*60 + 39.89, "athlete": "Ron Clarke", "country": "AUS", "location": "Oslo, Norway"},
    {"date": "1972-09-03", "time": 27*60 + 38.35, "athlete": "Lasse Virén", "country": "FIN", "location": "Munich, Germany"},
    {"date": "1973-07-13", "time": 27*60 + 30.80, "athlete": "David Bedford", "country": "GBR", "location": "London, United Kingdom"},
    {"date": "1977-06-30", "time": 27*60 + 30.47, "athlete": "Samson Kimobwa", "country": "KEN", "location": "Helsinki, Finland"},
    {"date": "1978-06-11", "time": 27*60 + 22.47, "athlete": "Henry Rono", "country": "KEN", "location": "Vienna, Austria"},
    {"date": "1984-07-02", "time": 27*60 + 13.81, "athlete": "Fernando Mamede", "country": "POR", "location": "Stockholm, Sweden"},
    {"date": "1989-08-18", "time": 27*60 + 8.23, "athlete": "Arturo Barrios", "country": "MEX", "location": "Berlin, Germany"},
    {"date": "1993-07-05", "time": 27*60 + 7.91, "athlete": "Richard Chelimo", "country": "KEN", "location": "Stockholm, Sweden"},
    {"date": "1993-07-10", "time": 26*60 + 58.38, "athlete": "Yobes Ondieki", "country": "KEN", "location": "Oslo, Norway"},
    {"date": "1994-07-22", "time": 26*60 + 52.23, "athlete": "William Sigei", "country": "KEN", "location": "Oslo, Norway"},
    {"date": "1995-06-05", "time": 26*60 + 43.53, "athlete": "Haile Gebrselassie", "country": "ETH", "location": "Hengelo, Netherlands"},
    {"date": "1996-08-23", "time": 26*60 + 38.08, "athlete": "Salah Hissou", "country": "MAR", "location": "Brussels, Belgium"},
    {"date": "1997-07-04", "time": 26*60 + 31.32, "athlete": "Haile Gebrselassie", "country": "ETH", "location": "Oslo, Norway"},
    {"date": "1997-08-22", "time": 26*60 + 27.85, "athlete": "Paul Tergat", "country": "KEN", "location": "Brussels, Belgium"},
    {"date": "1998-06-01", "time": 26*60 + 22.75, "athlete": "Haile Gebrselassie", "country": "ETH", "location": "Hengelo, Netherlands"},
    {"date": "2004-06-08", "time": 26*60 + 20.31, "athlete": "Kenenisa Bekele", "country": "ETH", "location": "Ostrava, Czech Republic"},
    {"date": "2005-08-26", "time": 26*60 + 17.53, "athlete": "Kenenisa Bekele", "country": "ETH", "location": "Brussels, Belgium"},
    {"date": "2020-10-07", "time": 26*60 + 11.00, "athlete": "Joshua Cheptegei", "country": "UGA", "location": "Valencia, Spain"}
]

df_10k = pd.DataFrame(data_10k)
df_10k.to_csv('10k_records.csv', index=False, sep=";")