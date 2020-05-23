names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names = [first_name.split()[0].lower() for first_name in names]
print(first_names)