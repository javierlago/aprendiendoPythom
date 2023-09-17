# Variables #

my_variable = "My string variable"
print(my_variable)

my_int_variable = 5
print(my_int_variable)

my_bool_variable = True
print(my_bool_variable)

# Concatenacion de variables en un print. #
print(my_bool_variable, my_variable, my_int_variable)
print(len(my_variable))   # Te dice el largo de la cadena #
print("Este es el valor de:", my_bool_variable)

# Variable en una sola linea #
name, surname, alias, age = "Javier", "Lago", "Reibax", 38

print('Mi nombre es ', name, 'y me apellido', surname)

# Entrada de datos por teclado #
name = input('Como te llamas')
age = input('Cuantos años tienes')

print('Me llamo ', name, 'y mi edad es de ', age)
