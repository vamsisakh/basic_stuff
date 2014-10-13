
#This program detects whether a string is a palindrome or not

def har_compare(String):
   length =len(String)
   if(length == 2):
      if(String[0] == String[1]):
	      return True
      else:
         return False
   elif(length == 1):
	   return True
   elif(String[0] == String[length-1]):
      String = String[1:length-1]
      return har_compare(String)
   else:
	   return False

String = raw_input ("Enter a string: ")
result =har_compare(String)

if(result == True):
	print("Entered string is a palindrome")
elif (result == False):
	print("Entered string is not a palidrome")

