# Apollos Eastman
# Nov 18 2024
# Default Values for Parameters Practice

# 8-3 (T-Shirt)
def make_shirt(size, text):
    print(f'\nYour shirt is size {size.lower()} and says "{text}".')

make_shirt('Medium', 'There\'s no place like home!')
make_shirt(size = 'Medium', text = 'There\'s no place like home!')

# 8-4 (Large Shirts)
def large_shirt(text = 'I love python!', size = 'large'):
    print(f'\nYour shirt is size {size.lower()} and says "{text}".')
    
large_shirt()
large_shirt(size = 'Medium')
large_shirt(size = 'small', text = 'Florida')

# 8-5 (Cities)
def describe_city(city, country = 'the USA'):
    print(f'\n{city} is in {country}.')

describe_city(city = 'Chicago')
describe_city('Paris', 'France')
describe_city('New York')
