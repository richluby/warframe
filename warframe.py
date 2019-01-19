#!/usr/bin/env python3

import logging
import os

_warframe_logger = None

class Warframe():
	"""
	stores stats specific to a warframe
	"""

	"""
	defines base values for all warframes. should be overriden by individual frames
	"""
	base_armor = 100
	base_health = 100
	base_shield = 100
	base_energy = 100
	base_sprint = 1

	"""
	defines the valid modifiers
	"""
	modifiers = ["health",
	"armor",
	"shield",
	"energy",
	"sprint_speed",
	"strength",
	"range",
	"duration",
	"efficiency",
	"energy"]

	def __init__(self, health_modifier=1, armor_modifier=1, shield_modifier=1):
		"""
		initializes the warframe
		"""
		# list containing the warframe abilities. 1-4 correlate with the
		# in-game abilities. Passive(s) are appended at the end of the list
		self.abilities = ()
		self.modifiers = dict()

		# warframe stats are a 1:1 mapping of the values shown in game
		self.base_armor  = Warframe.base_armor
		self.base_shield = Warframe.base_shield
		self.base_health = Warframe.base_health
		self.base_energy = Warframe.base_energy

		# all modifiers are stored as floats representing the non-percentage based
		# value, i.e. 110% power is stored 1.1
		for mod in Warframe.modifiers:
			self.modifiers[mod] = 1
		self.modifiers["health"] = health_modifier
		self.modifiers["armor"] = armor_modifier
		self.modifiers["shield"] = shield_modifier

		self.arcanes = ()
	
	def apply_modifier(self, modifier_name, value):
		"""
		applies the specified modifier with the value. `modifier_name` MUST be
		listed in Warframe.modifiers. `value` is the float value of the
		modifier (ie, 110% becomes 1.1)
		"""
		if not modifier_name in Warframe.modifiers:
			raise KeyError("modifier_name must be one of {}".format(Warframe.modifiers))
		self.modifiers[modifier_name] = value

def _test():
	warframe = Warframe()
	try:
		warframe.apply_modifier("new", 1.5)
	except KeyError as e:
		_warframe_logger.debug("apply_modifier correctly checks for non-existant keys.")

def _init_logger(level):
	global _warframe_logger
	formatter = logging.Formatter(datefmt="%Y-%m-%d %H:%M:%S", fmt=":%(name)s:%(levelname)s:%(message)s")
	handler = logging.StreamHandler()
	handler.setFormatter(formatter)
	_warframe_logger = logging.getLogger("libwarframe:"+__name__)
	_warframe_logger.addHandler(handler)
	_warframe_logger.setLevel(level)
	_warframe_logger.debug("Logger set to {}".format(level))

if __name__ == "__main__":
	level = os.getenv("LOGGER_LEVEL")
	# should be DEBUG, INFO, WARN, ERROR
	if level == "" or level == None:
		level = "WARN"
	_init_logger(level)
	_test()
	logging.shutdown()

