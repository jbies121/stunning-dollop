# Letter Frequency Analysis
# abruz & jbies121
def checkLetters(let):
        letters = let
        checked = []
        exists = False
        i=0
        j=0
        while i < len(letters):
            while j < len(checked):
                if letters[i] == checked[j]:
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
separated = list(userInput)
checkLetters(separated)
