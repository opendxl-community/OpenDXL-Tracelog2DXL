import sys, getopt,socket,json,os
import pyinotify
from dxlclient.client import DxlClient
from dxlclient.client_config import DxlClientConfig
from dxlclient.message import Event

config = DxlClientConfig.create_dxl_config_from_file(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dxl.conf'))

def pushDXL(PAYLOAD, TYPE_PAYLOAD, TOPIC_DESTINATION):
	HOST = socket.gethostname()
	DXL_MESSAGE = {}
	DXL_MESSAGE['SRC_HOST'] = HOST
	DXL_MESSAGE['TYPE_PAYLOAD'] = TYPE_PAYLOAD
	DXL_MESSAGE['PAYLOAD'] = PAYLOAD

	with DxlClient(config) as client:
		client.connect()
	    	event = Event(TOPIC_DESTINATION)
	    	event.payload = str(json.dumps(DXL_MESSAGE)).encode()
		client.send_event(event)
		return "DXL message: " + event.payload

def main(argv):

	TOPIC_DESTINATION = ''
	TYPE_PAYLOAD = 'log'
	PAYLOAD = ''
	LOG = ''
	help = 'python ' + sys.argv[0] + ' -t <topic destination> -f <logfile>'
	try:
		opts, args = getopt.getopt(argv,"ht:f:",["topic=","logfile="])
	except getopt.GetoptError:
		print help
		sys.exit(1)

	for opt, arg in opts:
		if opt == '-h':
			print help
			sys.exit(1)
		elif opt in ("-t", "--topic"):
			TOPIC_DESTINATION = arg
		elif opt in ("-f", "--logfile"):
			LOG = arg
	
	if (TOPIC_DESTINATION != '' and os.path.isfile(LOG)):   

		wm = pyinotify.WatchManager()
		mask = pyinotify.IN_MODIFY

		class EventHandler(pyinotify.ProcessEvent):
			def process_IN_MODIFY(self, event):
				PAYLOAD = file(LOG, "r").readlines()[-1].strip('\n')
				try:
					print pushDXL(PAYLOAD, TYPE_PAYLOAD, TOPIC_DESTINATION)
				except:
					print "message not sent. Check dxl.conf / Certificates / Connection"
					
		handler = EventHandler()
		notifier = pyinotify.Notifier(wm, handler)
		wdd = wm.add_watch(LOG, mask, rec=True)
		notifier.loop()

	else:
		print help
		sys.exit(1)

if __name__ == "__main__":
	main(sys.argv[1:])









