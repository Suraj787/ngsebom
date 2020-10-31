# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "ngsebom"
app_title = "Ngsebom"
app_publisher = "FirstERP"
app_description = "Custom BOM For NGSE"
app_icon = "octicon octicon-file-directory"
app_color = "Red"
app_email = "support@firsterp.in"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = [
    "https://unpkg.com/frappe-datatable@0.0.5/dist/frappe-datatable.min.css"
]

app_include_js = [
    "https://unpkg.com/clusterize.js@0.18.0/clusterize.min.js",
    "https://unpkg.com/frappe-datatable@0.0.5/dist/frappe-datatable.min.js"
]
# include js, css files in header of desk.html
# app_include_css = "/assets/ngsebom/css/ngsebom.css"
# app_include_js = "/assets/ngsebom/js/ngsebom.js"

# include js, css files in header of web template
# web_include_css = "/assets/ngsebom/css/ngsebom.css"
# web_include_js = "/assets/ngsebom/js/ngsebom.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "ngsebom.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "ngsebom.install.before_install"
# after_install = "ngsebom.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "ngsebom.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"ngsebom.tasks.all"
# 	],
# 	"daily": [
# 		"ngsebom.tasks.daily"
# 	],
# 	"hourly": [
# 		"ngsebom.tasks.hourly"
# 	],
# 	"weekly": [
# 		"ngsebom.tasks.weekly"
# 	]
# 	"monthly": [
# 		"ngsebom.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "ngsebom.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "ngsebom.event.get_events"
# }
