# Firebarrage's ChemiCompilerCompiler (C3)

# The ChemiCompiler ++ (CC++) language:
# add X Y 		- Adds Y to the contents of cell X
# sub X Y		- Subtracts Y from the contents of cell X
# move X bY bZ  - Moves X units from bY to bZ
# temp bX Y 	- sets the temperature of beaker X to Y degrees Kelvin
# end			- The end. 

def move_pointer(current_location, new_location):
	if(current_location < new_location):
		ch = '+'
	else:
		ch = '-'
	return ch*abs(current_location - new_location)

		

# Adds Y to cell X. Y may be a negative integer.
def process_add(state, command):
	# Is this a valid add command?
	try:
		assert(len(command) == 3)
		X = int(command[1])
		if(X < 0):
			print("Negative memory cell!")
			print("[" + str(i) + "]: " + " ".join(command))
			return [state,""]
		Y = int(command[2])
	except:
		print("Compile error: malformatted set command.")
		print("[" + str(i) + "]: " + " ".join(command))
		return [state,""]
		
	res = "" # Compiled ChemiFuck commands
	
	#Move the pointer to X
	res += move_pointer(state[pointer], X)
	state[pointer] = X
	
	# Determine direction
	if(Y >= 0):
		ch = '+'
	else:
		ch = '-'
	res += ch*Y
	return [state,res]
	

def compile(infile, outfile):
	#Keeps the current machine state
	state = {ax:0, tx: 0, sx: 0, pointer: 0} #Holds the registers

	#Read in a command
	line = infile.readline()
	command = line.split()
	i = 1 # Keeps line number for debugging purposes
	while(command[0] != "end"):
		if(line[0] == "#"): # comments are important!
			continue
		if(command[0] == ""): # Oi wheres the dang command 
			print("Compile error: expected a token at the start of a line")
			print("[" + str(i) + "]: " + " ".join(command))
			return
		if(command[0] == "add" or command[0] = "sub"): # add X Y or sub X Y
			res = process_add(state, command)
			if(res[1] == ""):
				return
			state = res[0]
			outfile.write(res[1])
			
			
				
		
		# next command
		command = infile.readline()
		i += 1
	return
	

def run():
	infile = input("Input file name: ")
	try:
		infile = open(infile,"r")
	except:
		print("Unable to open input file.")
		exit()
		
		
	outfile = input("Output file name: ")
	try:
		outfile = open(outfile,"w")
	except:
		print("Unable to open output file")
		exit()
		
	compile(infile, outfile)
	infile.close()
	outfile.close()
	
run()
