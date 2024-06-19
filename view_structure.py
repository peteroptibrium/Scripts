import sys
## The below commented out section was to help me find the archive hash associated with the name
## of a compound from the smiles file used as input to the epoxide calculation script
#with open('Epoxide_run.out', 'r') as infile:
#	lines = infile.readlines()
#	for li in lines:
#		tmpline = li.strip()
#		linearray = tmpline.split(' ')
#		if sys.argv[1] == linearray[0]:
#			dirhash = 'archive/'+linearray[4]+'/MINIMUM.xyz'
#			break
##	print(dirhash)

## The dirhash directory location is the location of the DMS archive directory created during an
## energy calculation
dirhash = '../OneDrive - Optibrium/Experimental_work/DMS_Archive/'+sys.argv[1]+'/MINIMUM.xyz'
with open('temp.xyz', "w") as outfile:
	with open(dirhash, 'r') as minimfile:
		lines2 = minimfile.readlines()
		numlines = len(lines2)
		atoms = int(lines2[0].strip())+1
		for newli in range(numlines-atoms,numlines):
#			print(lines2[newli].strip())
			outfile.write(lines2[newli])