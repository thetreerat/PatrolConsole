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
		self.sourceIP=None
		self.sourcePort=None
		self._decodedmsg=None
		self.encoded=None
		self._command = None
		self._RadioID = None
		self._extra = None
		if self.raw!=None:
			self.sourceIP = raw[1][0]
			self.sourcePort = raw[1][1]
			self._decodedmsg = raw[0].decode()
			self.encoded = raw[0]
			self.extractRadioID()
			self.extractCommand()
			self.extractExtra()

	def __str__(self):
		return "Message: " % ()

	def __repr(self):
		return "Message pythonID: %s" % (id(self))


	def command(self, pad=None):
		if pad==None:
			return self._command
		else:
			if self._command==None:
				return "".ljust(pad, " ")
			else:
				return self._command.ljust(pad, " ")

	def decodedmsg(self, pad=None):
		if pad==None:
			return self._decodedmsg
		else:
			if self._decodedmsg==None:
				return "".ljust(pad, " ")
			else:
				return self._decodedmsg.ljust(pad, " ")

	def encode_msg(self):
		"""Make message parts one encoded block"""
		self._decodedmsg = self.command(8) + self.RadioID(15) + self.extra(0)
		self.encoded = self._decodedmsg.encode()

	def extra(self, pad=None):
		if pad==None:
			return self._extra
		else:
			if self._extra==None:
				return "".ljust(pad, " ")
			else:
				return self._extra.ljust(pad, " ")

	def extractCommand(self):
		self._command = self._decodedmsg[0:7]

	def extractExtra(self):
		self._extra = self._decodedmsg[24:]

	def extractRadioID(self):
		self._RadioID = self._decodedmsg[8:23]

	def RadioID(self, pad=None):
		if pad==None:
			return self._RadioID
		else:
			if self._RadioID==None:
				return "".ljust(pad)
			else:
				self._RadioID.ljust(pad)

	def set_RadioID(self, RadioID):
		self._RadioID = RadioID
		self.encode_msg()

	def set_command(self, command):
		self._command = command
		self.encode_msg()

	def set_extra(self, data):
		self._extra = data
		self.encode_msg()

if __name__ == "__main__":
	msg = "DoSomeThBill T -HILL.  Hello to you".encode()
	inet = ("12.12.0.23", 34653)
	msgandAddress = (msg,inet)
	m = Message(msgandAddress)
	print(m.command())
	print(m.RadioID())
