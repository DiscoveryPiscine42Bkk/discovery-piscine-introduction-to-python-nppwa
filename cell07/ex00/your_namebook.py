def array_of_name(name_dict):
    full_names  = []
    for first, last in name_dict.items():
        full_name = f"{first.capitalize()} {last.capitalize()}"
        full_names.append(full_name)
    return full_names
persons = {
    "thanyaluk": "mungwicha",
    "nipaporn": "nhomphu",
    "cake": "wa",
    "wa": "cake"

}
    
print(array_of_name(persons))

