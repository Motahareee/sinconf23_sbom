import os
import sys
from bs4 import BeautifulSoup, NavigableString, Tag
# read the list of urls and create a dic based on dic
data_address = sys.argv[1]
dic = dict()
with open (data_address, 'r') as f:
	for line in f:
		index, keyword, dockername, version, url = line.split(",")
		if index not in dic.keys():	
			dic[int(index)] = [keyword, dockername, version, url]
		else:
			print("We got this one element twice:", index)

# now once I read the file I also have the info and can write it all
dir_address = sys.argv[2]
count = 0
total_rows = 0 #for test
unique_dockers = {}
with open("collected_unique_data_oct22", 'a') as data:
	for filename in os.listdir(dir_address):
		count += 1
		if  '.DS' in filename:	continue
		index = int(filename.split("_")[0])
		print(count, filename, index, len(unique_dockers))
		
		with open(f"{dir_address}/{filename}", 'rb') as f:
			file_content = f.read()
		bs_data = BeautifulSoup(file_content, "xml")
		components = bs_data.components.find_all('component')
		dependencies = set()
		
		counter = 0
		for comp in components:
			licenses = []
			if comp.licenses:
				for item in comp.licenses :
					if isinstance(item, NavigableString):	continue	
					for license in item.findAll('name'):
						licenses.append(''.join(license.findAll(text=True)))
			licenses = "|".join(licenses)
			purl = comp.purl.find_all(text=True)[0] if comp.purl else None
			current = (F"\"{comp.find('name').string}\"", F"\"{comp.version.string}\"", 
						F"\"{licenses}\"", F"\"{purl}\"")
			if current not in dependencies:
				if current[0]==None:	continue
				dependencies.add(current)
		total_rows += len(dependencies)
		
		for dependency in dependencies:
			dockername, version = dic[index][1:3]
			# if dockername in unique_dockers.keys():
			# 	if filename not in unique_dockers[dockername]:
			# 		unique_dockers[dockername].append(filename)
			# 		print("First time this happens:" ,unique_dockers[dockername])
			# 		exit()
			# else:
			# 	unique_dockers[dockername] = [filename]
			asstring = f"{dockername}, {version}, {dependency[0]}, {dependency[1] if dependency[1]!=None else '-'}, {dependency[2]}, {dependency[3]}\n"
			data.write(asstring)
for key in unique_dockers.keys():
	print(key, unique_dockers[key])
		