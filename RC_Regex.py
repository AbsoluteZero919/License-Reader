import re
# import json	#Not necessary since  we only need the pattern matched strings and no particular field

fop = open('RCjson.json')	#open JSON file
jdata = str(fop.readlines())	#.replace('}', "'''").replace('{', "'''")

regn_pat = '([A-Z]{2}[0-9]{1,2}[A-Z]{1,3}[\s]{0,1}[0-9]{4}|[A-Z]{2}[0-9]{2}-[A-Z]{1}-[0-9]{4})'						#RC Reg no. pattern

VIN_pat = '\w{11}[0-9]{6}'																							#VIN or Chassis no. pattern

name_pat = ': "[A-Z]{1,20}[\s.]{1,2}[A-Z]{0,20}[\s.]{0,2}[A-Z]{1,20}"'												#Name pattern

# eng_pat = ''	#Engine no. pattern is highly unique and there is no particular pattern

regdate_pat = '(0[1-9]|[12][0-9]|3[01])[/](0[1-9]|1[012])[/](19\d\d|20\d\d)'										#Registration date pattern or date of issue (dd/mm/yyyy)
mfgdate_pat = ': "(0[1-9]|1[012])[/](19\d\d|20\d\d)"'																#Mfg. date pattern

regn = re.findall(regn_pat, jdata)
print('Registration Number:', regn)

VIN = re.findall(VIN_pat, jdata)
print('VIN:', VIN)

name = re.findall(name_pat, jdata)
print('Name:', name)

regdate = re.findall(regdate_pat, jdata)
print('Registration Date:', regdate)

mfgdate = re.findall(mfgdate_pat, jdata)
print('Mfg Date:', mfgdate)

# print(str(jdata))