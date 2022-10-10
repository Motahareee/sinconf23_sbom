import sys
def search(search_keyword):
	import requests
	request_string = "https://sbom.rkvst.io/archivist/v1/sboms/-/metadata?trusted=TRUSTEDSTATUS_UNSPECIFIED&lifecycle_status=LIFECYCLESTATUS_UNSPECIFIED&privacy=PRIVATESTATUS_UNSPECIFIED&search="+\
                    search_keyword+"&page_size=1"
	#think about page limit
	response_API = requests.get(request_string, verify=True)
	jsondata = response_API.json()
	sboms = []
	counter = 0
	return(jsondata['sboms'])

counter = 1
with open(sys.argv[1], 'r') as dockerSearchResults:
	with open(sys.argv[2], 'a') as rkvstSearchResult:
		for line in dockerSearchResults:
			index = str(counter)
			keyword = line.split(',')[0].replace("\n", "")
			searchResult = search(keyword)
			for result in searchResult:
				address = result['identity']
				dl_request_string = "https://sbom.rkvst.io/archivist/v1/"+address
				
				dockername = result['component']
				version = result['version']
				#print([index, keyword, dockername, version, dl_request_string ])
				rkvstSearchResult.write(",".join([index, keyword, dockername, version, dl_request_string ])+"\n")
			
			if not len(searchResult):
				print("Could not find ", counter, keyword, searchResult)			
			counter += 1
