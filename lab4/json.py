import json
o = open('sample_json.txt')

data = json.load(o)
print(data['imdata'][0]['l1PhysIf']['attributes']['autoNeg'])