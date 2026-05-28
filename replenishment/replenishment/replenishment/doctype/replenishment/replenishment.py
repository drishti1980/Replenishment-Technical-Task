# Copyright (c) 2026, Drishti and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Replenishment(Document):

	def validate(self):
		frappe.msgprint("Validated")
		self.calculate_stock()

	def calculate_stock(self):
		
		self.current_stock = 20
		self.lockdays = self.lockdays or 90
		self.avg_daily_usage = self.current_stock/ self.lockdays
		self.lead_time_days = 7 if  self.lead_time_days ==0  else self.lead_time_days
		# if self.lead_time_days == 0:
		# 	self.lead_time_days = 7
		self.safety_stock_days = self.avg_daily_usage * self.safety_stock_days
		self.reorder_point = (
            self.avg_daily_usage
            * lead_time_days
        ) + safety_stock_qty
	# pass
