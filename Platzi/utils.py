def get_population():
    keys = ['col', 'bol']
    values = [300, 40]
    return keys, values

A = 'Hola'

def population_by_country(data, country):
    result = list(filter(lambda item: item['country'] == country, data))
    return result





