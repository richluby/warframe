#!/usr/bin/env python3
from warframe import *
import warframe

class Chroma(Warframe):
	
	base_armor = 350
	base_health = 300
	base_shield = 300
	base_energy = 225
	
	def __init__(self, health_modifier=0, armor_modifier=0, shield_modifier=0):
		super().__init__(health_modifier, armor_modifier, shield_modifier)
		self.base_attributes["armor"] = Chroma.base_armor
		self.base_attributes["shield"] = Chroma.base_shield
		self.base_attributes["health"] = Chroma.base_health
		self.base_attributes["energy"] = Chroma.base_energy

	def _calcVexArmor(self, scorn_multiplier=3.5):
		"""
		returns the calculated armor amount for activating vex armor
		"""
		return self.base_attributes["armor"] * (1 + self.modifiers["armor"] + scorn_multiplier * (self.modifiers["strength"]))

if __name__ == "__main__":
	level = os.getenv("LOGGER_LEVEL")
	# should be DEBUG, INFO, WARN, ERROR
	if level == "" or level == None:
		level = "WARN"
	warframe._init_warframe_logger(level=level)
	test()

