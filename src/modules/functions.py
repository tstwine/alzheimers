def menuDementiaOptions():
	print("Menu Options")
	print("1. Dementia Description")
	print("2. Dementia Symptons")
	print("3. Cognitive Symptons")
	print("4. Dementia Diagnosis")
	print("5. Types of Dementia")


def menuAlzheimersOptions():
	print("Menu Options")
	print("1. Alzheimers Definition")
	print("2. Alzheimers Description")
	print("3. Alzheimers Symptons")
	print("4. Alzheimers Causes")
	print("5. Alzheimers Treatment")
	print("6. Parkinson's Disease")
	print("7. Normal Pressure Hydrocephalus")
	print("8. Creutzfeldt Jakob Disease-CJD")
	print("9. Dementia with Lewy Body")
	print("10. Fronttempomporal Lobar Degeneration-FTLD")
	print("11. Vascular Dementia")
	print("12. Mixed Dementia")


	#checks if user knows zipcode
zipVerify = raw_input("Please enter your zip code? ").lower()
# if User knows zip, the user is asked for the rest of their address 
# through the getAddressWithZip function
if zipVerify == "yes" or zipVerify == "y":
    addressLine1, addressLine2, city, state, zipCode = getAddressWithZip()
#if user doesn't know their zip code, the user is asked for city and state 
# through the getAddressNoZip function
elif zipVerify == "no" or zipVerify == "n":
    addressLine1, addressLine2, city, state, zipCode = getAddressNoZip()
else:
    print("You have entered an invalid response. ")
# this runs if user enters something other than "yes" or "no" 

print("address")


