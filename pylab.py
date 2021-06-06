import json

#text: a,b:'20';c,d:True
def dict(text):
	keys_and_values = ""
	subjects = text.split(';')
	for each_sub in subjects:
		# remove whitespace
		each_sub = (each_sub.rstrip()).lstrip()

		# ignores if each_sub is empty
		if each_sub == "":
			continue

		# when = is used instead of :
		if "=" in each_sub:
			print("Error: Please use ':' for seperating key from value")
			exit(0)

		keys = each_sub.split(':')[0]

		# remove whitespace
		keys = keys.rstrip(" '").lstrip(" '")

		keys_value = each_sub.split(':')[1]

		# remove whitespace
		keys_value = (keys_value.rstrip()).lstrip()

		# converts string to json format
		if "True" in keys_value:
			keys_value = keys_value.replace("True", "true")	# json recognizes 'true' not 'True'
		if "False" in keys_value:
			keys_value = keys_value.replace("False", "false")
		if "'" in keys_value:
			keys_value = keys_value.replace("'", "\"")	# json uses '' to get the string

		if ", " in keys:
			for index, key in enumerate(keys.split(', ')):
				if index == 0:
					if len(keys_and_values) == 0:
						keys_and_values = f'"{key}":{keys_value}'
					else:
						keys_and_values += f', "{key}":{keys_value}'
				else:
					keys_and_values += f', "{key}":{keys_value}'
		elif "," in keys:
			for index, key in enumerate(keys.split(',')):
				if index == 0:
					if len(keys_and_values) == 0:
						keys_and_values = f'"{key}":{keys_value}'
					else:
						keys_and_values += f', "{key}":{keys_value}'
				else:
					keys_and_values += f', "{key}":{keys_value}'
		else:
			if len(keys_and_values) == 0:
				keys_and_values = f'"{keys}":{keys_value}'
			else:
				keys_and_values += f', "{keys}":{keys_value}'
	string_dict = '{' + keys_and_values + '}'
	# converts string to dict
	try:
		dictionary = json.loads(string_dict)
	except:
		print("Error! Check the syntax again.")
		exit(0)
	return dictionary