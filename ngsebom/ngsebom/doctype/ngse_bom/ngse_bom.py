# -*- coding: utf-8 -*-
# Copyright (c) 2020, FirstERP and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class NGSEBOM(Document):
	def get_stock_and_rate(self):
		from erpnext.stock.dashboard.item_dashboard import get_data
		from erpnext.stock.get_item_details import get_price_list_rate
		stock_data = get_data(self.itemid)
		data = []
		total_stock = 0
		for d in stock_data:
			total_stock += d.actual_qty
			data.append({
				'warehouse':d.warehouse,
				'actual_qty':d.actual_qty,
				'uom':self.stock_uom
			})
		args = frappe._dict({
								"doctype": self.doctype,
								"price_list": frappe.db.get_single_value("NGSE BOM Setting","buying_price_list"),
								"qty":1,
								"uom": self.uom or "Nos",
								"stock_uom": self.stock_uom,
								"transaction_type": "buying",
								"company": frappe.defaults.get_defaults("Company")["company"],
								"currency": frappe.defaults.get_defaults("Company")["currency"],
								"conversion_rate": 1, # Passed conversion rate as 1 purposefully, as conversion rate is applied at the end of the function
								"conversion_factor":  1,
								"plc_conversion_rate": 1,
								"ignore_party": True
							})
		item_doc = frappe.get_doc("Item", self.itemid)
		out = frappe._dict()
		get_price_list_rate(args, item_doc, out)
		rate = out.price_list_rate
		data.append({
			'warehouse':"Total Stock",
			'actual_qty':total_stock,
			'uom':self.stock_uom
		})
		data.append({
			'warehouse':"Rate",
			'actual_qty':rate,
			'uom':frappe.defaults.get_defaults("Company")["currency"]
		})
		return data, total_stock, rate
