#Python XploitWirter
# An ImOverlord Productions


#Dichiarare le variabili
lineN = 0 
line = "" 
buffer = ["#ImOverlord"] #Array to save all lines
Over = 0

#Functions because why not 
def Input( lineN ):
	inp = str(lineN)
	inp += ' : > '
	line = raw_input(inp)
	return line;

def Edit(line): #Edit Function get Line Number to Edit
	# **edit [line]
	line_len = len(line)
	Edito = line[7:line_len]
	#Debugging Stuff 
	#print Edito
	Edito = int(Edito)
	#modify array
	buffer[Edito] = raw_input('Edit > ')
	print "\n"
	for i in range(len(buffer)):
		print i,": >",buffer[i]
	return
	return

def Clear( line ): #Clear Function
	# **clear [line]
	line_len = len(line)
	Clearo = line[8:line_len]
	#Debugging Stuff
	#print Clearo
	Clearo = int(Clearo)
	#Remove item from array
	buffer.pop(Clearo)
	print "\n"
	for i in range(len(buffer)):
		print i,": > ",buffer[i]
	
	return


file= raw_input('File Name: ')
print "\n"
while line != "{END}":
	Over = 0 #reset
	lineN = lineN + 1
	inp = str(lineN)
	inp += ' : > '
	line = raw_input(inp)
	
	#Add clear line function and Edit Function
	if "**clear" in line:
		Clear(line)
		Over = 1
		lineN -= 2
	
	if "**edit" in line:
		Edit(line)
		Over = 1 
		lineN -= 2
		
	if line == "{END}":
		f = open(file,'w')
		buffer.pop(0)
		#Write Buffer to file
		for i in range(len(buffer)):
			f.write(buffer[i])
		f.close()

	if line != "{END}" and Over == 0:
		buffer.append(line + "\n")
