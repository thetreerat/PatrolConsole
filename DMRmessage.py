# Copyright Harold Clark 2021
#
#from login import Login
#from database import database
from Radio import Radio
import datetime

class Message(object):
	""" """
	def __init__(self, raw=None):
		self.raw=raw
		self.sourceIP = raw[1][0]
		self.sourceport = raw[1][1]
		self.decoded = raw[0].decode()
		self.encoded = raw[0]
		self._command = None
		self._RadioID = None
		if self.raw!=None:
			self.extractRadioID()
			self.extractCommand()

	def __str__(self):
		return "Message: " % ()

	def __repr(self):
		return "Message pythonID: %s" % (id(self))


	def command(self):
		return self._command

	def encode_msg(self):
		"""Need to create msg from Parts """
		self.encoded = self.decoded.encode()

	def extractCommand(self):
		self._command = self.decoded[0:7]

	def extractRadioID(self):
		self._RadioID = self.decoded[8:23]

	def RadioID(self):
		return self._RadioID

	def set_RadioID(self, RadioID):
		self._RadioID = RadioID
		self.encode_msg()

	def set_command(self, command):
		self._command = command
		self.encode_msg()

if __name__ == "__main__":
	msg = "DoSomeThBill T -HILL.  Hello to you".encode()
	inet = ("12.12.0.23", 34653)
	msgandAddress = (msg,inet)
	m = Message(msgandAddress)
	print(m.command())
	print(m.RadioID())
