# Using PrettyTable for formating data inside a table.
from prettytable import PrettyTable
table = PrettyTable()
table.field_names = ["Pokemon Name", "Type"]
table.add_row(["Pikachu", "Electric"])
table.add_row(["Squirtle", "Water"])
table.add_row(["Charmander", "Fire"])
table.add_row(["Bulbasaur", "Grass"])
table.align = "l"
print(table)