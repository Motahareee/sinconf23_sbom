import os
import sys
import requests

def parse_xml(dl_request_string: str):
  from urllib.request import urlopen
  from xml.etree.ElementTree import parse
  var_url = urlopen(dl_request_string)
  return(var_url.read())

  from bs4 import BeautifulSoup
  bs_data = BeautifulSoup(var_url, "xml")
  components = bs_data.components.find_all('component')
  
  res = set()
  counter = 0
  for comp in components:
    current = (comp.find('name').string, comp.version.string)
    if current not in res:
      res.add(current)
  return res

# existing_files = set()
# for file in os.listdir("uniqueXmlFiles"):
# 	existing_files.add(file[:-4])
counter = 0
with open ( sys.argv[1], 'r') as xmlURLS:
	for line in xmlURLS:
		#print(counter)
		# if counter<5012:
		# 	counter += 1
		# 	continue
		counter += 1
		index, keyword, dockername, version, url = line.split(",")

		dockername, version = dockername.replace('-','_').replace('/','_'), version.replace('.', '_') 
		r = requests.get(url)
		filename = f"{index}_{dockername}_{version}"
		#if filename not in existing_files:
		try:
			with open(F"uniqueXmlFiles_Oct22/{filename}.xml",'ab') as xml:
				xml.write(parse_xml(url))
				#print("NEW !!")
		except:
			with open("uniqueDownloadFailure_Oct22", 'a') as failed:
				print("could not do ", url)
				failed.write(line)
		# else:
		# 	print("Already have it!")
				
