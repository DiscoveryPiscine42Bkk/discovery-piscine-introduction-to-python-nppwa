def genopum(family):
    return list(filter(lambda name: family[name]== "pum", family.keys()))

dupont_family = { 
    "wa": "peter",
    "peter": "wa",
    "ice": "cake",
    "nipaporn": "wa",
    "chomphu": "wa"
}

print(peterwa(dupont_family))