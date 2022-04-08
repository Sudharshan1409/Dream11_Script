import pandas as pd
import json
scores = {
    'Darshan': 0,
    'Panee': 0,
    'Badri': 0,
    'Srinidhi': 0,
    'Nandan': 0,
    'PavanG': 0,
    'PavanK': 0,
    'Ananthu': 0
}

df = pd.read_csv('scoresheet.csv')

for i in range(len(df)):
    if len(df.iloc[i]['Second'].split('&')) > 1:
        scores[df.iloc[i]['Second'].split('&')[0]] += 20
        scores[df.iloc[i]['Second'].split('&')[1]] += 20
        scores[df.iloc[i]['First']] += 40
    else:
        scores[df.iloc[i]['First']] += 40
        scores[df.iloc[i]['Second']] += 25
        scores[df.iloc[i]['Third']] += 15

print('Total Winings:', json.dumps(scores, indent=4), sep='\n')

for key, value in scores.items():
    scores[key] = value - len(df) * 10

print('Total Profit:', json.dumps(scores, indent=4), sep='\n')


