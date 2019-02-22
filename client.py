import sys

def vote():
	#vote for a party
	print("You voted!")

def add_party():
	#adding a party
	print("You added a party!")

def view_results():
	#viewring results
	print("results not out yet dawg")

def main():
	#Main function
	#3 functionalities -> vote, add, view results

	if(len(sys.argv)==2 or len(sys.argv)==3):
		
		if(sys.argv[1]=="add"):
			#add party
			add_party()

		elif(sys.argv[1]=="vote"):
			vote()

		elif(sys.argv[1]=="view"):
			view_results()

		else:
			print("Invalid format!")
			exit()
	
	else:
		print("Invalid format!")
		exit()

#calling main
main()
