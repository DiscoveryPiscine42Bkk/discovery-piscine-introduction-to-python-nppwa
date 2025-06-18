def cakewa(family):
    return list(filter(lambda name: family[name] == "cake", family.keys()))

dupont_family = {
    "wa": "wa",
    "cake": "cake",
    "mairu": "tem",
    "nipaporn": "wa",
    "chomphu": "wa"
}

print(cakewa(dupont_family))
                