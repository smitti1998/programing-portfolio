# today we are making cookies

def main():
	try: 
		cookie = open("zcookie.txt", "r")
		cookie.close()
		return True 
	except:
		return False

def set_cookie(name):
 	cookie = open("zcookie.txt", "w")
 	cookie.write(name+"\n")
 	cookie.write(email + "\n")
 	cookie.close()

def main():
	if has_cookie():
		greet()
	
def greet():
	try:
		cookie = open("zcookie.txt", "r")
		lines = cookie.readlines()
		name = lines [0]
		email = line [1]
		print "Welcome %s! Nice to see you again, is your email %s?" % (name, email)
		cookie.close()
	except:
		print "Welcome" 
		
print show_instructions():
	print "Hello, please enter your name: "
	name = raw_input()
	print "now enter your email:"
	email = raw_input
	return (name, email)
			
	name, email = show_instructions()
	set_cookie(name , email)
	
	
	print "thank you. Have a nice day %s!" % (name)

	

main()


why is jacson so gay!!!!              llllll
							