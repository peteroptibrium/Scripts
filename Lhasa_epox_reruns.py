import sys
from com.optibrium.dms.common.reactivity.barrier_calculation import BarrierCalculation

# Script to run the Lhasa parent structures through the CP2K epoxidation routine in DMS

with open(sys.argv[1], 'r') as infile:
	lines = infile.readlines()
	for li in lines:
		tmpline = li.strip()
		linearray = tmpline.split(' ')
		calc = BarrierCalculation(linearray[0], "GST", "HUMAN", "CP2K")
		subs_eng = calc.get_substrate_energy(True, False)
		print(linearray[1]+" is in directory "+str(calc.get_hash()))
		print("parent HoF is "+str(subs_eng))
		dict = calc.get_sites_of_metabolism()
		for key in dict.keys():
			if len(dict[key]) >0:
				for pair in dict[key] :
						epox_eng = calc.get_activation_energy(pair, True, False)
						print("energy and gap for "+str(pair)+" is "+str(epox_eng))
