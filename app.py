import quickfix
from datetime import datetime
import re

def print_with_time(content):
	print(f'{datetime.now()} >> {content}')

def format_message(message):
	return re.sub('[\x01]', '|', message)

def inv_format_message(message):
	return re.sub('[|]', '\x01', message)

class TestApp(quickfix.Application):
	session_id = None
	logged_on = False

	def onCreate(self, sessionID):
		self.session_id = sessionID
		print_with_time(f'[{sessionID}] On Create')
	def onLogon(self, sessionID):
		self.logged_on = True
		print_with_time(f'[{sessionID}] On Logon')
	def onLogout(self, sessionID):
		print_with_time(f'[{sessionID}] On Logout\n\n')
	def toAdmin(self, message, sessionID):
		print_with_time(f'[{sessionID}] To Admin: {format_message(message.toString())}')
	def toApp(self, message, sessionID):
		print_with_time(f'[{sessionID}] To App: {format_message(message.toString())}')
	def fromAdmin(self, message, sessionID):
		print_with_time(f'[{sessionID}] From Admin: {format_message(message.toString())}')
	def fromApp(self, message, sessionID):
		print_with_time(f'[{sessionID}] From App: {format_message(message.toString())}')