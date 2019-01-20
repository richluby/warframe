#!/usr/bin/env python3

import os
import unittest
from warframe import *
from chroma import *

class TestWarframe(unittest.TestCase):
	def __init__(self, test):
		super().__init__(test)
		self.warframe = Warframe()

	def test_applying_modifiers(self):
			with self.assertRaises(AttributeError, msg="Modifiers incorrectly allowed to apply to non-existant attributes."):
				self.warframe.apply_modifier("new", 1.5)
			self.warframe.apply_modifier("health", 1)
			self.assertEqual(self.warframe.health, 2, msg="Modifier not correctly applied. Recieved: {}\tExpected: {}".format(
				self.warframe.health, 2))
			self.warframe.apply_modifier("health", 0)
			self.assertEqual(self.warframe.health, 1, msg="Modifier not correctly removed. Recieved: {}\tExpected: {}".format(
				self.warframe.health, 1))

	def test_assign_properties(self):
		with self.assertRaises(AttributeError, msg="Properties incorrectly allowed to be directly assigned."):
			self.warframe.armor = 100
	
	def test_request_property(self):
		try:
			self.assertIsNotNone(self.warframe.energy, msg="Failed to access property using dot notation.")
		except AttributeError as e:
			self.assertTrue(False, "Failed to access property with dot notation: {}".format(e))

	def test_attribute_initialization(self):
		for att in Warframe.inherent_attributes:
			if self.warframe[att] != 1:
				self.assertEqual(self.warframe[att], 1, "Unexpected modified attribute: {} \tval: {}\tExpected: {}".format(att, self.warframe[att], 1))

class TestChroma(unittest.TestCase):
	def __init__(self, test):
		super().__init__(test)
		self.chroma = Chroma()
	
	def test_vex_armor(self):
		chroma = Chroma(armor_modifier=1.1)
		chroma.apply_modifier("strength", 1.3)
		calcArmor = chroma._calcVexArmor()
		self.assertEqual(calcArmor, 2327.5, "Chroma Vex armor: {}\tExpected: {}".format(calcArmor, 2327.5))

if __name__ == "__main__":
	global logger
	level = os.getenv("LOGGER_LEVEL")
	# should be DEBUG, INFO, WARN, ERROR
	if level == "" or level == None:
		level = "WARN"
	init_warframe_logger(level)
	logger = warframe.warframe_logger
	unittest.main()

