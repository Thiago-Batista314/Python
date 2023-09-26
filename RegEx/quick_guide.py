import re
# Match = Verificar;
# ^ Matches the beginning of a line; Ex: re.search('^From:', line);
# $ Matches the end of the line; Ex: ;
# . Matches any characther; Ex: ;
# \s Matches whitespace; Ex: ;
# \S Matches any non whitespace charachter; Ex: ;
# '*' Repeats any character zero or more times; Ex: ;
# '*?' Repeats any character zero or more times; Ex: ; (non-greedy)
# + Repeats a character one or more times; Ex: ;
# +? Repeats a character one or more times; Ex: ; (non-greedy)
# [aeiou] Matches a single character in the listed set; Ex: ;
# [^XYZ] Matches a single character not in the listed set; Ex: ;
# [a-z0-9] The set of the characters can include a range; Ex: ;
# ( Indicates where string extraction will start; Ex: ;
# ) Indicates where string extraction will end; Ex: ;
# re.search: string.find(), returns true or false;
# re.findall: string.find() + slice, returns the estracted value;

# <---- Matching and extracting Data ---->
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+', x) # returns a list if the string have the the characters;
z = re.search('[0-9]', x) # returns none if the string doesn't have;
print(y, z)

# <---- Greedy Matching Data ---->
x = 'From: Using the : character'
y = re.findall('^F.+:', x) # first chac: F, last chac: :, .+: 1 or more times;
print(y)

# <---- Non-Greedy Matching Data ---->
x = 'From: Using the : character'
y = re.findall('^F.+?:', x) # first chac: F, last chac: :, .+?: 1 or more times non-greedy;
print(y)

# <---- Fine-Tuning String Extraction ---->
# <~~~~ Mode 1 ~~~~>
x = 'From stephen.maquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('\S+@\S+', x) # ! Wrong!!!
print(y)
# <~~~~ Mode 2 ~~~~>
x = 'From stephen.maquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('^From (\S+@\S+)', x)# ? Correct!!!
print(y)

# <---- String Parsing Examples ---->
# ! <~~~~ Mode 1 ~~~~>
data = 'From stephen.maquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos = data.find('@')
appos = data.find(' ', atpos)
host = data[atpos+1 : appos]
print(host) # uct.ac.za
# ! <~~~~ Mode 1 ~~~~>
# ! <~~~~ Mode 2 ~~~~>
data = 'From stephen.maquard@uct.ac.za Sat Jan  5 09:14:16 2008'
email = data.split()[1]
pieces = email.split('@')
print(pieces[1])# uct.ac.za
# ! <~~~~ Mode 2 ~~~~>
# ? <~~~~ Mode 3 ~~~~>
data = 'From stephen.maquard@uct.ac.za Sat Jan  5 09:14:16 2008'
host = re.findall('@ (\S*)', data)
print(host)# ['uct.ac.za']
# ? <~~~~ Mode 3 ~~~~>
# ? <~~~~ Mode 3 ~~~~> Better
data = 'From stephen.maquard@uct.ac.za Sat Jan  5 09:14:16 2008'
host = re.findall('^From .*@(\S*)', data)
print(host)# ['uct.ac.za']
# ? <~~~~ Mode 3 ~~~~> Better