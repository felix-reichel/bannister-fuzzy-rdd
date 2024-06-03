# The data stems from: https://bringbackthemile.com/history/progressions
# Might contain errors
# For all current IAF data see:
# https://worldathletics.org/records/all-time-toplists/middlelong/one-mile/all/men/senior

import pandas as pd

data = [
    {"date": "1913-05-31", "time": 4*60 + 14.4, "athlete": "John Paul Jones", "country": "USA", "location": "Cambridge, MA USA"},
    {"date": "1915-07-16", "time": 4*60 + 12.6, "athlete": "Norman Taber", "country": "USA", "location": "Cambridge, MA USA"},
    {"date": "1923-08-23", "time": 4*60 + 10.4, "athlete": "Paavo Nurmi", "country": "FIN", "location": "Stockholm, SWE"},
    {"date": "1931-10-04", "time": 4*60 + 9.2, "athlete": "Jules Ladoumègue", "country": "FRA", "location": "Paris, FRA"},
    {"date": "1933-07-15", "time": 4*60 + 7.6, "athlete": "Jack Lovelock", "country": "NZL", "location": "Princeton, NJ USA"},
    {"date": "1934-06-16", "time": 4*60 + 6.8, "athlete": "Glenn Cunningham", "country": "USA", "location": "Princeton, NJ USA"},
    {"date": "1937-08-28", "time": 4*60 + 6.4, "athlete": "Sydney Wooderson", "country": "GBR", "location": "Motspur Park, GBR"},
    {"date": "1942-07-01", "time": 4*60 + 6.2, "athlete": "Gunder Hägg", "country": "SWE", "location": "Göteborg, SWE"},
    {"date": "1942-07-10", "time": 4*60 + 6.2, "athlete": "Arne Andersson", "country": "SWE", "location": "Stockholm, SWE"},
    {"date": "1942-09-04", "time": 4*60 + 4.6, "athlete": "Gunder Hägg", "country": "SWE", "location": "Stockholm, SWE"},
    {"date": "1943-07-01", "time": 4*60 + 2.6, "athlete": "Arne Andersson", "country": "SWE", "location": "Göteborg, SWE"},
    {"date": "1944-07-18", "time": 4*60 + 1.6, "athlete": "Arne Andersson", "country": "SWE", "location": "Malmö, SWE"},
    {"date": "1945-07-17", "time": 4*60 + 1.4, "athlete": "Gunder Hägg", "country": "SWE", "location": "Malmö, SWE"},
    {"date": "1954-05-06", "time": 3*60 + 59.4, "athlete": "Roger Bannister", "country": "GBR", "location": "Oxford, GBR"},
    {"date": "1954-06-21", "time": 3*60 + 58.0, "athlete": "John Landy", "country": "AUS", "location": "Turku, FIN"},
    {"date": "1957-07-19", "time": 3*60 + 57.2, "athlete": "Derek Ibbotson", "country": "GBR", "location": "London, GBR"},
    {"date": "1958-08-06", "time": 3*60 + 54.5, "athlete": "Herb Elliott", "country": "AUS", "location": "Dublin, IRL"},
    {"date": "1962-01-27", "time": 3*60 + 54.4, "athlete": "Peter Snell", "country": "NZL", "location": "Wanganui, NZL"},
    {"date": "1964-11-17", "time": 3*60 + 54.1, "athlete": "Peter Snell", "country": "NZL", "location": "Auckland, NZL"},
    {"date": "1965-06-09", "time": 3*60 + 53.6, "athlete": "Michel Jazy", "country": "FRA", "location": "Rennes, FRA"},
    {"date": "1966-07-17", "time": 3*60 + 51.3, "athlete": "Jim Ryun", "country": "USA", "location": "Berkeley, CA USA"},
    {"date": "1967-06-23", "time": 3*60 + 51.1, "athlete": "Jim Ryun", "country": "USA", "location": "Bakersfield, CA USA"},
    {"date": "1975-05-17", "time": 3*60 + 51.0, "athlete": "Filbert Bayi", "country": "TAN", "location": "Kingston, JAM"},
    {"date": "1975-08-12", "time": 3*60 + 49.4, "athlete": "John Walker", "country": "NZL", "location": "Göteborg, SWE"},
    {"date": "1979-07-17", "time": 3*60 + 49.0, "athlete": "Sebastian Coe", "country": "GBR", "location": "Oslo, NOR"},
    {"date": "1980-07-01", "time": 3*60 + 48.8, "athlete": "Steve Ovett", "country": "GBR", "location": "Oslo, NOR"},
    {"date": "1981-08-19", "time": 3*60 + 48.53, "athlete": "Sebastian Coe", "country": "GBR", "location": "Zürich, SUI"},
    {"date": "1981-08-26", "time": 3*60 + 48.40, "athlete": "Steve Ovett", "country": "GBR", "location": "Koblenz, GER"},
    {"date": "1981-08-28", "time": 3*60 + 47.33, "athlete": "Sebastian Coe", "country": "GBR", "location": "Brussels, BEL"},
    {"date": "1985-07-27", "time": 3*60 + 46.32, "athlete": "Steve Cram", "country": "GBR", "location": "Oslo, NOR"},
    {"date": "1993-09-05", "time": 3*60 + 44.39, "athlete": "Noureddine Morceli", "country": "ALG", "location": "Rieti, ITA"},
    {"date": "1999-07-07", "time": 3*60 + 43.13, "athlete": "Hicham El Guerrouj", "country": "MAR", "location": "Rome, ITA"}
]

df = pd.DataFrame(data)

df.to_csv('mile_records.csv',
          index=False,
          sep=";")