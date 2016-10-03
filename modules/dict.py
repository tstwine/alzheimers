class DementiaClass:

	import urllib2
	import json

	def __init__(self):
		pass


	def getDemCharactByOnset(self, onset):
		api_call = DementiaClass.urllib2.urlopen('https://www.nia.nih.gov/alzheimers/topics/other-dementias')
		json_string = api_call.read()
		dementia_object = DementiaClass.json.loads(json_string)
		api_call.close

		return dementia_object

	def getDemCharactByFamilyHistory(self, family_history):
		api_call = DementiaClass.urllib2.urlopen('https://www.nia.nih.gov/alzheimers/topics/other-dementias')
		json_string = api_call.read()
		dementia_object = DementiaClass.json.loads(json_string)
		api_call.close

		return dementia_object
			
	def getDemCharactByActiveManagement(self, active_management):
		api_call = DementiaClass.urllib2.urlopen('https://www.nia.nih.gov/alzheimers/topics/other-dementias')
		json_string = api_call.read()
		dementia_object = DementiaClass.json.loads(json_string)
		api_call.close

		return dementia_object
	
	def getDemCharactByGender(self, gender):
		api_call = DementiaClass.urllib2.urlopen('https://www.nia.nih.gov/alzheimers/topics/other-dementias')
		json_string = api_call.read()
		dementia_object = DementiaClass.json.loads(json_string)
		api_call.close

		return dementia_object

	def getDemCharactByEducation(self, education):
		api_call = DementiaClass.urllib2.urlopen('https://www.nia.nih.gov/alzheimers/topics/other-dementias')
		json_string = api_call.read()
		dementia_object = DementiaClass.json.loads(json_string)
		api_call.close

		return dementia_object
					

	def getDemCharactByRace(self, race):
		api_call = DementiaClass.urllib2.urlopen('https://www.nia.nih.gov/alzheimers/topics/other-dementias')
		json_string = api_call.read()
		dementia_object = DementiaClass.json.loads(json_string)
		api_call.close

		return dementia_object
													

	def getDementiaByDefinition(self, definition):
		api_call = DementiaClass.urllib2.urlopen('https://www.who.int/mediacentre/factsheets/fs362/en/')
		json_string = api_call.read()
		dementia_object = DementiaClass.json.loads(json_string)
		api_call.close()

		return dementia_object

	def getDementiaBySymptons(self, symptons):
		api_call = DementiaClass.urllib2.urlopen('https://www.who.int/mediacentre/factsheets/fs362/en/')
		json_string = api_call.read()
		dementia_object = DementiaClass.json.loads(json_string)
		api_call.close

		return dementia_object

	def getDementiaByCognitive(self, cognitive):
		api_call = DementiaClass.urllib2.urlopen('https://www.who.int/mediacentre/factsheets/fs362/en/')
		json_string = api_call.read()
		dementia_object = DementiaClass.json.loads(json_string)
		api_call.close

		return dementia_object

	def getDementiaByTypesofDementia(self, TypesofDementia):
		api_call = DementiaClass.urllib2.urlopen('https://www.who.int/mediacentre/factsheets/fs362/en/')
		json_string = api_call.read()
		dementia_object = DementiaClass.json.loads(json_string)
		api_call.close

		return dementia_object

	def getAlzheimersByDefinition(self, definition):
		api_call = DementiaClass.urllib2.urlopen('https://www.nia.nih.gov/alzheimers/')
		json_string = api_call.read()
		dementia_object = DementiaClass.json.loads(json_string)
		api_call.close

		return dementia_object

	def getAlzheimersByDiagnosis(self, diagnosis):
		api_call = DementiaClass.urllib2.urlopen('https://www.nia.nih.gov/alzheimers')
		json_string = api_call.read()
		dementia_object = DementiaClass.json.loads(json_string)
		api_call.close

		return dementia_object

	def getAlzheimersBySymptons(self, symptons):
		api_call = DementiaClass.urllib2.urlopen('https://www.nia.nih.gov/alzheimers')
		json_string = api_call.read()
		dementia_object = DementiaClass.json.loads(json_string)
		api_call.close

		return dementia_object

	def getAlzheimersByTypesofAlzheimers(self, TypesofAlzheimers):
		api_call = DementiaClass.urllib2.urlopen('https://www.nia.nih.gov/alzheimers')
		json_string = api_call.read()
		dementia_object = DementiaClass.json.loads(json_string)
		api_call.close
			
		return dementia_object
		
	def getAlzheimersByTreatments(self, treatments):
		api_call = DementiaClass.urllib2.urlopen('https://www.nia.nih.gov/alzheimers')
		json_string = api_call.read()
		dementia_object = DementiaClass.json.loads(json_string)
		api_call.close
				
		return dementia_object
	
	def getVascularDementiabyDefinition(self, definition):
		api_call = DementiaClass.urllib2.urlopen('https://www.nia.nih.gov/alzheimers/topics/other-dementias')
		json_string = api_call.read()
		dementia_object = DementiaClass.json.loads(json_string)
		api_call.close

		return dementia_object

	def getVascularDementiabyDiagnosis(self, diagnosis):
		api_call = DementiaClass.urllib2.urlopen('https://www.nia.nih.gov/alzheimers/topics/other-dementias')
		json_string = api_call.read()
		dementia_object = DementiaClass.json.loads(json_string)
		api_call.close

		return dementia_object
		
	
	def getVascularDementiabySymptons(self, symptons):
		api_call = DementiaClass.urllib2.urlopen('https://www.nia.nih.gov/alzheimers/topics/other-dementias')
		json_string = api_call.read()
		dementia_object = DementiaClass.json.loads(json_string)
		api_call.close

		return dementia_object

	def	getVascularDementiabyCauses(self, causes):
		api_call = DementiaClass.urllib2.urlopen('https://www.nia.nih.gov/alzheimers/topics/other-dementias')
		json_string = api_call.read()
		dementia_object = DementiaClass.json.loads(json_string)
		api_call.close

		return dementia_object

	def getVascularDementiabyTreatments(self, treatments):
		api_call = DementiaClass.urllib2.urlopen('https://www.nia.nih.gov/alzheimers/topics/other-dementias')
		json_string = api_call.read()
		dementia_object = DementiaClass.json.loads(json_string)
		api_call.close

		return dementia_object
	
	def getDementiaWithLewyBodiesByDefinition(self, definition):
		api_call = DementiaClass.urllib2.urlopen('https://www.nia.nih.gov/alzheimers/topics/other-dementias')
		json_string = api_call.read()
		dementia_object = DementiaClass.json.loads(json_string)
		api_call.close

		return dementia_object
			
	def getDementiaWithLewyBodiesByDiagnosis(self, diagnosis):
		api_call = DementiaClass.urllib2.urlopen('https://www.nia.nih.gov/alzheimers/topics/other-dementias')
		json_string = api_call.read()
		dementia_object = DementiaClass.json.loads(json_string)
		api_call.close

		return dementia_object

	def getDementiaWithLewyBodiesBySymptons(self, symptons):
		api_call = DementiaClass.urllib2.urlopen('https://www.nia.nih.gov/alzheimers/topics/other-dementias')
		json_string = api_call.read()
		dementia_object = DementiaClass.json.loads(json_string)
		api_call.close

		return dementia_object

	def getDementiaWithLewyBodiesByCauses(self, causes):
		api_call = DementiaClass.urllib2.urlopen('https://www.nia.nih.gov/alzheimers/topics/other-dementias')
		json_string = api_call.read()
		dementia_object = DementiaClass.json.loads(json_string)
		api_call.close

		return dementia_object

	def getDementiabyWithLewyBodiesbyMedications(self, medications):
		api_call = DementiaClass.urllib2.urlopen('https://www.nia.nih.gov/alzheimers/topics/other-dementias')
		json_string = api_call.read()
		dementia_object = DementiaClass.json.loads(json_string)
		api_call.close

		return dementia_object

	def getMixedDementiabyDefinition(self, definition):
		api_call = DementiaClass.urllib2.urlopen('https://www.nia.nih.gov/alzheimers/topics/other-dementias')
		json_string = api_call.read()
		dementia_object = DementiaClass.json.loads(json_string)
		api_call.close

		return dementia_object

	def	getMixedDementiabyDiagnosis(self, diagnosis):
		api_call = DementiaClass.urllib2.urlopen('https://www.nia.nih.gov/alzheimers/topics/other-dementias')
		json_string = api_call.read()
		dementia_object = DementiaClass.json.loads(json_string)
		api_call.close

		return dementia_object

	def getMixedDementiabySymptons(self, symptons):
		api_call = DementiaClass.urllib2.urlopen('https://www.nia.nih.gov/alzheimers/topics/other-dementias')
		json_string = api_call.read()
		dementia_object = DementiaClass.json.loads(json_string)
		api_call.close

		return dementia_object

	def getMixedDementiabyCauses(self, causes):
		api_call = DementiaClass.urllib2.urlopen('https://www.nia.nih.gov/alzheimers/topics/other-dementias')
		json_string = api_call.read()
		dementia_object = DementiaClass.json.loads(json_string)
		api_call.close

		return dementia_object

	def getMixedDementiabyTreatments(self, treatments):
		api_call = DementiaClass.urllib2.urlopen('https://www.nia.nih.gov/alzheimers/topics/other-dementias')
		json_string = api_call.read()
		dementia_object = DementiaClass.json.loads(json_string)
		api_call.close

		return dementia_object	
				

	def	getFrontotemporalDementiabyDefinition(self, definition):
		api_call = DementiaClass.urllib2.urlopen('https://www.nia.nih.gov/alzheimers/topics/other-dementias')
		json_string = api_call.read()
		dementia_object = DementiaClass.json.loads(json_string)
		api_call.close

		return dementia_object

	def getFrontotemporalDementiabyDiagnosis(self, diagnosis):
		api_call = DementiaClass.urllib2.urlopen('https://www.nia.nih.gov/alzheimers/topics/other-dementias')
		json_string = api_call.read()
		dementia_object = DementiaClass.json.loads(json_string)
		api_call.close

		return dementia_object
		
	def getFrontotemporalDementiabySymptons(self, symptons):
		api_call = DementiaClass.urllib2.urlopen('https://www.nia.nih.gov/alzheimers/topics/other-dementias')
		json_string = api_call.read()
		dementia_object = DementiaClass.json.loads(json_string)
		api_call.close

		return dementia_object
	
	def getFrontotemporalDementiabyCauses(self, causes):
		api_call = DementiaClass.urllib2.urlopen('https://www.nia.nih.gov/alzheimers/topics/other-dementias')
		json_string = api_call.read()
		dementia_object = DementiaClass.json.loads(json_string)
		api_call.close

		return dementia_object
											

	def	getFrontotemporalDementiabyTreatments(self, treatments):
		api_call = DementiaClass.urllib2.urlopen('https://www.nia.nih.gov/alzheimers/topics/other-dementias')
		json_string = api_call.read()
		dementia_object = DementiaClass.json.loads(json_string)
		api_call.close

		return dementia_object

	def getFrontotemporalDementiabyTypesofFTD(self, TypesofFTD):
		api_call = DementiaClass.urllib2.urlopen('https://www.nia.nih.gov/alzheimers/topics/other-dementias')
		json_string = api_call.read()
		dementia_object = DementiaClass.json.loads(json_string)
		api_call.close

		return dementia_object

	def getCreutzfeldt_Jakob_DiseaseCJDbyDefinition(self, definition):
		api_call = DementiaClass.urllib2.urlopen('https://www.nia.nih.gov/alzheimers/topics/other-dementias')
		json_string = api_call.read()
		dementia_object = DementiaClass.json.loads(json_string)
		api_call.close

		return dementia_object

	def getCreutzfeldt_Jakob_DiseaseCJDbyDiagnosis(self, diagnosis):
		api_call = DementiaClass.urllib2.urlopen('https://www.nia.nih.gov/alzheimers/topics/other-dementias')
		json_string = api_call.read()
		dementia_object = DementiaClass.json.loads(json_string)
		api_call.close

		return dementia_object
	
	def getCreutzfeldt_Jakob_DiseaseCJDbySymptons(self, symptons):
		api_call = DementiaClass.urllib2.urlopen('https://www.nia.nih.gov/alzheimers/topics/other-dementias')
		json_string = api_call.read()
		dementia_object = DementiaClass.json.loads(json_string)
		api_call.close

		return dementia_object

	def	getCreutzfeldt_Jakob_DiseaseCJDbyCauses(self, causes):
		api_call = DementiaClass.urllib2.urlopen('https://www.nia.nih.gov/alzheimers/topics/other-dementias')
		json_string = api_call.read()
		dementia_object = DementiaClass.json.loads(json_string)
		api_call.close

		return dementia_object

	def getCreutzfeldt_Jakob_DiseaseCJDbyTreatments(self, treatments):
		api_call = DementiaClass.urllib2.urlopen('https://www.nia.nih.gov/alzheimers/topics/other-dementias')
		json_string = api_call.read()
		dementia_object = DementiaClass.json.loads(json_string)
		api_call.close

		return dementia_object

	def getNormalPressureHydrocephalusNPHbyDefinition(self, definition):
		api_call = DementiaClass.urllib2.urlopen('https://www.nia.nih.gov/alzheimers/topics/other-dementias')
		json_string = api_call.read()
		dementia_object = DementiaClass.json.loads(json_string)
		api_call.close

		return dementia_object
		
	def getNormalPressureHydrocephalusNPHbyDiagnosis(self, diagnosis):
		api_call = DementiaClass.urllib2.urlopen('https://www.nia.nih.gov/alzheimers/topics/other-dementias')
		json_string = api_call.read()
		dementia_object = DementiaClass.json.loads(json_string)
		api_call.close

		return dementia_object
	
	def getNormalPressureHydrocephalusNPHbySymptons(self, symptons):
		api_call = DementiaClass.urllib2.urlopen('https://www.nia.nih.gov/alzheimers/topics/other-dementias')
		json_string = api_call.read()
		dementia_object = DementiaClass.json.loads(json_string)
		api_call.close

		return dementia_object

	def getNormalPressureHydrocephalusNPHbyCauses(self, causes):
		api_call = DementiaClass.urllib2.urlopen('https://www.nia.nih.gov/alzheimers/topics/other-dementias')
		json_string = api_call.read()
		dementia_object = DementiaClass.json.loads(json_string)
		api_call.close

		return dementia_object

	def getNormalPressureHydrocephalusNPHbyTreatments(self, treatments):
		api_call = DementiaClass.urllib2.urlopen('https://www.nia.nih.gov/alzheimers/topics/other-dementias')
		json_string = api_call.read()
		dementia_object = DementiaClass.json.loads(json_string)
		api_call.close

		return dementia_object
	







			
	
			

		



