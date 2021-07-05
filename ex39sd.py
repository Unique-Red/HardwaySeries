states = {
    'Lagos': 'LA',
    'Ondo': 'ON',
    'Calabar': 'CA',
    'Ogun': 'OG',
    'Benin': 'BE'
}

cities = {
    'LA': 'Island',
    'ON': 'Ondo town',
    'OG': 'Ota'
}

cities['CA'] = 'Awka'
cities['BE'] = 'Edo'

print('-' * 5)
print("OG State has: ", cities['OG'])
print("LA State has: ", cities['LA'])
