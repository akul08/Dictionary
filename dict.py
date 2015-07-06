import sys
from  bs4 import BeautifulSoup as bs
import requests as r

def main():

	"""

			Stage 1
	----------------------------------------------------------------------------
		Check if The User Has Input The Word Or Not
	"""

	if len(sys.argv)<2:
		print "Usage : python dict.py word_to_search"
		sys.exit()

	"""
			Stage 2
	----------------------------------------------------------------------------
		Open Dictionary.com And Parse it Using BeautifulSoup
	"""

	content = r.get('http://dictionary.reference.com/browse/'+str(sys.argv[1]))
	soup = bs(content.text)

	"""
			Stage 3
	----------------------------------------------------------------------------
		Check if The Word Is Misspelled or Spelled Correctly
	"""

	if soup.find(class_="closest-result"):
		print "\n\t\t\tMisspelled."
		print soup.find(class_="closest-result").get_text().replace("\n\n\n","")
		print soup.find(class_="more-suggestions").get_text().replace("\n\n\n","\t")
		
		"""
			Stage 4
	------------------------------------------------------------------------------
		If The Word is Correctly Spelled Then Search It On Dictionary.com And Print The Results

		"""
	
	else:
		i = 0
		for dictionary in soup.findAll("div",{'class':'def-list'}):
			if not i:
				print "\n\t\tWelcome To Dictionary.com\n"
			elif i == 1 : #For British Dictionary
				print "\t\tBritish Dictionary definitions for " + str(sys.argv[1])

			elif i == 2 :	#For History And Origin of Word
				print "\t\tWord Origin and History for " + str(sys.argv[1])

			if dictionary.find({'class':'luna-data-header'}):# if Dictionary Has A Title
				print dictionary.find({'class':'luna-data-header'})

			print dictionary.get_text() 
			i += 1

if __name__ == "__main__":
	main()