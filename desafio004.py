from time import sleep
print("\033[1;35;40mCHARACTER READER\033[m")
n = input('\033[35mType any character: \033[m')
sleep(3)
print('Is the typed character alphabet? ',(n.isalpha()))
print('Is the typed character numeric? ',(n.isnumeric()))
print('Is the typed character alphanumeric?',(n.isalnum()))
print('Is the typed character decimal? ',(n.isdecimal()))
print('Is the typed character in upper case?',(n.isupper()))
print('Is the typed character in lower case?',(n.islower()))
print('Is the typed character printable?',(n.isprintable()))
print('Is the typed character a digit?',(n.isdigit()))
print('Is the typed character ASCII?',(n.isascii()))
print('Is the typed character a Python Identifier?',(n.isidentifier()))
print('Is the typed character a white space?',(n.isspace()))
print('Is the typed character in title case?',(n.istitle()))
print("\033[35m----------READING COMPLETE-----------\033[m")











