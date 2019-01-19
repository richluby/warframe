#!/usr/bin/env python3

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

	def __init__(self, healthModifer=1, armorModifier=1, shieldModifier=1):
		"""
		initializes the warframe
		"""
		# list containing the warframe abilities. 1-4 correlate with the
		# in-game abilities. Passive(s) are appended at the end of the list
		self.abilities = ()

		# warframe stats are a 1:1 mapping of the values shown in game
		self.armor  = base_armor
		self.shield = base_shield
		self.health = base_health
		self.energy = base_energy

		# all modifiers are stored as floats representing the non-percentage based
		# value, i.e. 110% power is stored 1.1
		self.sprint_speed_modifier = 1
		self.strength_modifier = 1
		self.efficiency_modifier = 1
		self.duration_modifier = 1
		self.range_modifier = 1

		self.health_modifier
		self.armor_modifier
		self.shield_modifier
		self.energy_modifier

		self.arcanes = ()

