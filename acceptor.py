import quickfix
import app
from app import print_with_time

try:
	settings = quickfix.SessionSettings('acceptor.conf')
	application = app.TestApp()
	storeFactory = quickfix.FileStoreFactory(settings)
	acceptor = quickfix.SocketAcceptor(application, storeFactory, settings)
	acceptor.start()
	print_with_time("Acceptor started...\n\n")
	while True:
		pass
	acceptor.stop()
except quickfix.ConfigError as e:
	print(e)