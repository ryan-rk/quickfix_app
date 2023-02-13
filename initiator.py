import quickfix
import quickfix50sp2 as sp2
import app
import uuid
from app import print_with_time, inv_format_message
import time

try:
	settings = quickfix.SessionSettings('initiator.conf')
	application = app.TestApp()
	storeFactory = quickfix.FileStoreFactory(settings)
	initiator = quickfix.SocketInitiator(application, storeFactory, settings)
	initiator.start()
	print_with_time("Initiator started...\n")
	while (not application.logged_on):
		time.sleep(1)
	single_order_msg = sp2.NewOrderSingle()
	quickfix.Session.sendToTarget(single_order_msg, application.session_id)

	# logon_string = '8=FIXT.1.1|9=75|35=A|34=10|49=client|52=20230213-02:26:13.000|56=server|98=0|108=20|1137=9|10=195|'
	# formatted_logon_string = inv_format_message(logon_string)

	time.sleep(5)
	initiator.stop()
except quickfix.ConfigError as e:
	print(e)