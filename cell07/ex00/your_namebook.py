def array_of_names(name_dict):
    full_names = []
    for first, last in name_dict.items():
        full_names = f"{first.capitalize()} {last.capitalize()}"
        full_names.append(full_names)
    return full_names

persons + {
    "nipaporn": "chomphu",
    "warit": "watcharamaitithipat",
    'wa': "peter",
    "peter": "wa"
}

print(array_of_names(persons))