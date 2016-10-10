from testdementia import *
#form onset import *

def testdementiaSearch():
	while True:
		try:
			dementia = testdementia[input("Please enter the type of Alzheimers: ").capitalize()]
			break 

		except KeyError:
			print("Invalid Entry. Please try again")

		return testdementia
		
print(testdementiaSearch()['diagnosis'])			
			