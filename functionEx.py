# Write a function that loops through a list of first_names and a list of last_names, combines the two and return a list of full_names
def fullName(first_names, last_names):
    return [f'{first_names[i].title()} {last_names[i].title()}' for i in range(min(len(first_names), len(last_names)))]
    
    

first_name = ['John', 'Evan', 'Jordan', 'Max']
last_name = ['Smith', 'Smith', 'Williams', 'Bell']

print(fullName(first_name, last_name))