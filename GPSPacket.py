	# Copyright Harold Clark 2021
#
#from menu import Menu
#from login import Login
#from database import database

class GPSPacket(object):
	"""GPS packet decoder for motobro radios"""
	def __init__(self, 
	             asciistring=None):
	    self._asciistring = asciistring
	    self._hexstring = None
	    self._binarystring = None
	    self.extractHex()
	    self.extractBinary()
	    self.extractLatLong()	
	    self.startbit = 0    	
	 
	def __str__(self):
		return "GPSPacket - Message: %s Lat: %s Long: %s" % (self._asciistring, self._latDec, self._longDec)

	def __repr(self):
		return "GPSPacket - Message: %s Lat: %s Long: %s pythonID: %s" % (self._asciistring, self._latDec, self._longDec, id(self))

	def extractHex(self):
		if self._asciistring:
			self._hexstring = self._asciistring.encode()
		else:
			self._hexstring = None

	def extractBinary(self):
		if self._hexstring:
			self._binarystring = bin(int(self._hexstring,16))[2:]
		else:
			self._binarystring = None

	def extractLatLong(self):
		if self._binarystring:
			self._lat = int(self._binarystring[11:18], 2)
			self._latMinutes = int(self._binarystring[18:24], 2)
			self._latMinutesDec = float("." + str(int(self._binarystring[24:38],2)))
			self._latDec = self._lat + (self._latMinutes + self._latMinutesDec)/60
			self._long = int(self._binarystring[38:46],2)
			self._longMinutes = int(self._binarystring[46:52], 2)
			self._longMinutesDec = float("." + str(int(self._binarystring[52:66], 2)))
			self._longDec = self._long + (self._longMinutes + self._longMinutesDec)/60
			
		else:
			self._lat = None
			self._latMinutes = None
			self._latMinutesDec =  None
			self._latDec = None
			self._long = None
			self._longMinutes = None
			self._longMinutesDec = None
			self._longDec = None

	def stripeOneBit(self):
		if self._binarystring!=None:
			self.startbit += 1
			#print("stripeOneBit startbit: %s" % (self.startbit))
			self._binarystring = self._binarystring[1:]
			if len(self._binarystring) > 53:
				self.extractLatLong()
			else:
				self._binarystring = None


	def printgps(self):
		pass

if __name__ == "__main__":
	print("Starting Run ...")
	packets = []
	packets.append("0d09663d5986a9c8da9a7b")
	packets.append("0d09663d598771c8da9b4c")
	for P in packets:
		print("Running scan with %s" % (P))
		gps = GPSPacket(P)
		print("gps initalized")
		#print(gps)
		while gps._binarystring!=None:
			if gps._lat==43:
				print("Found lat: %s index: %s" % (gps._lat, gps.startbit))
				print("Lat minutes: %s" % (gps._latMinutes))
				print("Lat dec: %s" %(gps._latMinutesDec))
				print("Long: %s" % (gps._long))
				print("Long minutes: %s" % (gps._longMinutes))
				print("Long dec: %s" % (gps._longMinutesDec))
				#print(gps)
			gps.stripeOneBit()
	print("Run Complete!")
	

