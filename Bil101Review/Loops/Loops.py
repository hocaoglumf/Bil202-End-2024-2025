person = {"Dhushi": 6, "Lee": 32, "Marc": 30}

for key, value in person.items():
    print(f'Name: {key}, Age: {value}.')

languages = ['Python', 'C', 'Java', 'JavaScript']

for index, value in enumerate(languages):
    print(f'Index:{index}, Value:{value}')

names = ['Dhushi', 'Praj', 'Lee']
languages = ['Python', 'JavaScript', 'Java']
for name, language in zip(names, languages):
    print('My name is {0}. My favourite language is {1}.'.format(name, language))