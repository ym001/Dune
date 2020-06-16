#file_='amazon_review_full.zip'
#file_='yelp_review_polarity.zip'
file_='eRisk_dep.zip'
dir_='../datasets/'
outfile = dir_+file_

name=file_.split('.')[0]
ext=file_.split('.')[1]
packet_size = int(74 * 1000**2)   # bytes

#write
with open(outfile, "rb") as output:
	filecount = 0
	while True:
		data = output.read(packet_size)
		if not data:
			break   # we're done
		with open("{}{}{:02}.{}".format(dir_,name, filecount,ext), "wb") as packet:
			packet.write(data)
		filecount += 1
'''
#read
file_list=['amazon_review_full_00.zip','amazon_review_full.zip01','amazon_review_full.zip02','amazon_review_full.zip03',
'amazon_review_full.zip04','amazon_review_full.zip05','amazon_review_full.zip06','amazon_review_full.zip07','amazon_review_full.zip08']
data = None
for file_ in file_list:
	with open('../datasets/'+file_, "rb") as output:
		if data is None:data = output.read(packet_size)
		else:data += output.read(packet_size)

outfile='../datasets/'+'test.zip'
with open(outfile, "wb") as packet:
			packet.write(data)
'''
