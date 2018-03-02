import requests

fh = open('trainslist.txt', 'a')
log = open('log.txt', 'a')

for i in range(89999,69999,-1):
	trainno = ('{0:05}'.format(i))
	print(trainno)
	url = 'https://enquiry.indianrail.gov.in/xyzabc/ShowTrainSchedule?trainNo=' + trainno + '&validOnDate=26/02/2018&scrnSize=&langFile=props.en-us'
	
	while True:
		try:
			data = requests.get(url).content.decode()
			# print(data)
			if not data.startswith('XYZABC'):
				# print('hey')
				fh.write(str(trainno) + "\n")
			log.write("success: " + str(trainno) + "\n")
			break
		except Exception:
			log.write("error: " + str(trainno) + "\n")
			print("error: " + str(trainno))
	