#!/usr/bin/env python3

import logging
import os

warframe_logger = None

class Warframe():
	"""
	stores stats specific to a warframe
	"""

	"""
	defines the valid warframe attributes
	"""
	inherent_attributes = ["health",
	"armor",
	"shield",
	"energy",
	"sprint_speed",
	"strength",
	"range",
	"duration",
	"efficiency"]

	def __init__(self, health_modifier=0, armor_modifier=0, shield_modifier=0):
		"""
		initializes the warframe
		"""
		# list containing the warframe abilities. 1-4 correlate with the
		# in-game abilities. Passive(s) are appended at the end of the list
		self.abilities = ()

		# dicts contain attribute information for each warframe. these are
		# intended as read-only values. use `apply_modifier` to add a modifier.
		self.base_attributes = dict()
		self.modifiers = dict()

		# all modifiers are stored as floats representing the non-percentage based
		# value, i.e. 110% power is stored 1.1
		for att in Warframe.inherent_attributes:
			self.base_attributes[att] = 1
			self.modifiers[att] = 0
		self.apply_modifier("health", health_modifier)
		self.apply_modifier("armor", armor_modifier)
		self.apply_modifier("shield", shield_modifier)

		self.arcanes = ()

	def __getattr__(self, att):
		"""returns a calculated attribute from a warframe"""
		self._check_attribute(att)
		return self.base_attributes[att] * (1 + self.modifiers[att])
	
	def __getitem__(self, att):
		"""allow subscripting for access"""
		return self.__getattr__(att)
	
	def __str__(self):
		"""returns a string representation of this frame"""
		return "\n".join("{}: {}".format(i, self.__getattr__(i)) for i in Warframe.inherent_attributes)

	def _check_attribute(self, att):
		"""raises an error if this attibute is not supported"""
		if not att in self.base_attributes:
			raise AttributeError("Attribute must be one of {}\tReceived: {}".format(self.base_attributes, att))

	
	def apply_modifier(self, modifier_name, value):
		"""
		applies the specified modifier with the value. `modifier_name` MUST be
		listed in Warframe.modifiers. `value` is the float value of the
		modifier (ie, 110% becomes 1.1). While the modifiers are directly
		settable, its recommended to use the apply_modifier function. the
		function allows individual warframes to modify behavior if necessary.
		directly setting the dict value may bypass this behavior.
		"""
		self._check_attribute(modifier_name)
		self.modifiers[modifier_name] = value

def init_warframe_logger(level="WARN"):
	global warframe_logger
	formatter = logging.Formatter(datefmt="%Y-%m-%d %H:%M:%S", fmt="%(asctime)s:%(name)s:%(levelname)s:%(message)s")
	handler = logging.StreamHandler()
	handler.setFormatter(formatter)
	warframe_logger = logging.getLogger("libwarframe:"+__name__)
	warframe_logger.addHandler(handler)
	warframe_logger.setLevel(level)
	warframe_logger.debug("Logger set to {}".format(level))

if __name__ == "__main__":
	level = os.getenv("LOGGER_LEVEL")
	# should be DEBUG, INFO, WARN, ERROR
	if level == "" or level == None:
		level = "WARN"
	init_warframe_logger(level)
	_test()
	logging.shutdown()

