animals = [{'type': 'cat', 'name': 'Stephanie', 'age': 8},
           {'type': 'dog', 'name': 'Devon', 'age': 3},
           {'type': 'rhino', 'name': 'Moe', 'age': 5}]
print(sorted(animals, key=lambda animal: animal['age']))
animals.sort(key=lambda animal:animal['age'])
print(animals)
