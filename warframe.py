#!/usr/bin/env python3

class Warframe():
	"""
	stores stats specific to a warframe
	"""

	def __init__(self):
		"""
		initializes the warframe
		"""
		self.abilities = ()
		self.armor = 0
		self.shield = 0
		self.health = 0

		# all powers are stored as floats representing the non-percentage based
		# value, i.e. 110% power is stored 1.1
		self.strength = 1
		self.efficiency = 1
		self.duration = 1
		self.range = 1

def calcChromaVexArmor(baseArmor=425, armorModValue=0, mulitplier=3.5, strengthMods=0):
	"""
	returns the calculated armor amount for activating vex armor
	"""
	return baseArmor * (1 + armorModValue + mulitplier * (1 + strengthMods))
	
