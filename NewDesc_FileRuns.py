import sys
from com.optibrium.dms.common.database.mongodb_wrapper import MongoDbWrapper
MongoDbWrapper.initialise("127.0.0.1")
from com.optibrium.dms.worker.reactivity.barrier_calculation import get_barrier_values
from com.optibrium.dms.worker.reactivity.gst_descriptor_matrix import get_gst_descriptor_matrix

# Script to run the new dataset structures through the CP2K epoxidation routine in DMS
with open("NewDataSet_descs2.csv", "w") as outfile:
	with open(sys.argv[1], 'r') as infile:
		lines = infile.readlines()
		for li in lines:
			tmpline = li.strip()
			linearray = tmpline.split(' ')
			calc = get_gst_descriptor_matrix([linearray[0]], True, False)
			outfile.write(calc)
