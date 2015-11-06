import json
with open('taglist_final.json') as f:
    j = json.load(f)
    
dict2 = {item: [key for key in j if item in j[key]] for value in j.values() for item in value}

with open('taglist_by_mod.json','w') as f:
    json.dump(dict2,f)