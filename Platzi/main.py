import utils

keys, values = utils. get_population()
print(keys, values)

print(utils.A)

data = [
    {
    'country': 'colombia',
    'population': 300
    },
    {
    'country': 'peru',
    'population': 120
    },

    {
    'country': 'brazil',
    'population': 450
    },
    
    {
    'country': 'Argentina',
    'population': 520
    },
]
country = input('Type country => ')
result = utils.population_by_country(data, country)
print(result)