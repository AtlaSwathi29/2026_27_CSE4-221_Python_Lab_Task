# string
text = "jeevitha"
print(f"'ee' in '{text}' is {'ee' in text}")
print(f"'ws' not in '{text}' is {'ws' not in text}")

# list (int, float, bool, str values)
number_list = [33, 88, 22]
float_list = [6.4, 3.2, 9.0]
bool_list = [True, False]
string_list = ["heylo", "prana"]
print(f"88 in {number_list} is {88 in number_list}")
print(f"9.0 in {float_list} is {9.0 in float_list}")
print(f"True in {bool_list} is {True in bool_list}")
print(f"'ra' in {string_list} is {'ra' in string_list}")

# tuple
number_tuple = (7, 9, 3)
print(f"7 in {number_tuple} is {7 in number_tuple}")

# set
number_set = {81, 34, 71}
print(f"34 in {number_set} is {34 in number_set}")

# dictionary
student = {"name": "Aira", "age": 19}
print(f"'name' in {student} is {'name' in student}")
print(f"'Aira' not in {student} is {'Aira' not in student}")