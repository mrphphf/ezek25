from selenium import webdriver
import keyboard
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import pygame
class Hats:
	def __init__(self):
		self.ownedHats = {}
		self.unbindableKeys = ["w", "a", "s", "d", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "e", "`", "enter"]
		self.boundKeys = []
		self.goldCount = 0
		self.driver = webdriver.Firefox()
	def getHatState(self, id):
		handle = self.driver.find_element_by_id(id)
		stateDiv = handle.find_elements_by_tag_name("div")
		if stateDiv.text == "Equip":
			state = "inactive"
			if id not in self.ownedHats:
				self.hatBind(id)
		elif stateDiv.text == "Unequip":
			state = "active"
			if id not in self.ownedHats:
				self.hatBind(id)
		return state
	def hatScan(self):
		self.storeClick()
		for storeItem in self.driver.find_elements_by_class_name("storeItem"):
			state = getHatState(storeItem.get_attribute("id"))
		if self.activeHat == None:
			nohat = "gooo aiseu!"
		self.storeClick()
	def grabHatNameById(self, id):
		handle = self.driver.find_element_by_id(id)
		hatNameSpan = handle.find_elements_by_tag_name("span")
		hatName = span.text
		return hatName
	def playHat(self, id, key):
		self.storeClick()
		handle = self.driver.find_element_by_id(id)
		hatId = handle.find_elements_by_tag_name("id")
		hatId.click()
		self.storeClick()
	def getActiveHat(self):
		return true

	def removeHat(self):
		self.storeClick()
		for storeItem in self.driver.find_element_by_class_name("storeItem"):
			state = self.getHatState(storeItem.get_attribute("id"))
			if state == "Unequip":
				handle = storeItem.find_elements_by_tag_name("div")
				div.click
				break
		self.storeClick()
	def hvhStyle(self):
		self.driver.title = "LamboWare"
	def hatBind(self, id):
		self.driver.execute_script("var hatBind = prompt('What key would you like to bind to " + self.grabHatNameById(id) + " ? Enter an empty space character to keep unbound.')")
		bindKey = self.driver.execute_script("return hatBind;")
		if bind == " ":
			print self.grabHatNameById(id) + " will not be bound."
			return true
		else:
			if bindKey in self.boundKeys:
				self.driver.execute_script("alert('Key already bound')")
				return "Key Already Bound"
			if bindKey not in self.unbindableKeys:
				if(self.ownedHats.update({bindKey: id})):
					self.boundKeys.append(bindKey)
					return true
				else:
					return false
			else:
				self.driver.execute_script("alert('Illegal Key')")
				return "Key Cannot be bound"
	def storeClick(self):
		handle = self.driver.find_element_by_id("storeButton")
		handle.click()
hats = Hats()
while(True):
	if keyboard.is_pressed("`"):
		hats.hatScan()
		time.sleep(0.2)
	for key in hats.ownedHats:
		if keyboard.is_pressed(key):
			hats.playHat(hats.ownedHats[key], key)
	time.sleep(0.1)
