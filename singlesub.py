def popArray(str):
	i=0
	lettors = []
	while i < len(str):
		letter = str[i]
		lettors.append(letter)
		i+=1
	return(lettors)
	
def outputArray(let):
	print(let)
	
def checkLetters(let):
	letters = let
	checked = []
	exists = False
	i=0
	j=0
	while i < len(letters):
		while j < len(checked):
			if(letters[i] == checked[j]):
				exists = True
			j+=1
		if exists == False:
			t = letters[i]
			checked.append(t)
			countLetters(letters, i)
		j=0
		i+=1
		exists = False

	
def countLetters(let, a):
	char = let[a]
	print(char,end="")
	print(" appears: ",end="")
	print(let.count(char))
		
		

userInput = input("What string should be used? ")
separated = popArray(userInput)
checkLetters(separated)
