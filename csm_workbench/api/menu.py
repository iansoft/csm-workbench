# _*_ coding: utf-8 _*_
from django.db import connection
from manage_menu.models import Menu
from sqlhelper import dictfetchall

def init_menu(menu_config):
	'''start build the menu tree'''
	for m in menu_config:
		menu = Menu(name=m["name"], url=m["url"], icon=m["icon"], openable=m["openable"])
		menu.save()
		for sub_m in m["children"]:
			sub_menu = Menu(name=sub_m["name"], url=sub_m["url"], icon=sub_m["icon"], openable=sub_m["openable"], parentID=menu.id)
			sub_menu.save()

def set_menu(role_name, menu_name):
    #get the roles' name
	# role_name_list = []
	# for role in roles:
	# 	role_name_list.append("'"+role["name"]+"'")
	# str_role_name_list= ','.join(role_name_list)

	#generate the sql
	sql='''SELECT id, name, url, icon, openable, active, parentID, deleted 
		FROM t_menu
		WHERE id IN (
		SELECT DISTINCT(m.id)
		FROM t_role_menu rm
		INNER JOIN t_menu m ON m.id = rm.menu_id
		INNER JOIN t_role r ON r.id = rm.role_id
		WHERE r.name = '%s'
	)
	'''%(role_name)

	#fetch the data
	dataset = []
	with connection.cursor() as c:
		c.execute(sql)
		dataset = dictfetchall(c)

	# get all the menu item 
	menu_list = []
	selected_menu_parentID = 0
	for m in dataset:
		selected = False
		if m["name"] == menu_name:
			selected = True
			selected_menu_parentID = m["parentID"]
		menu = {
			"id":m["id"],
			"name":m["name"],
			"url":m["url"],
			"icon":m["icon"],
			"openable":m["openable"],
			"active":"",
			"parentID":m["parentID"],
			"selected":selected,
			"children":[]
		}
		menu_list.append(menu)
	# filter the parent menu 
	parent_menu = [m for m in menu_list if m["parentID"]==None]
	# get the menu tree
	for p in parent_menu:
		if p["selected"] == True or p["id"] == selected_menu_parentID:
			p["active"] = "active"
		for m in menu_list:
			# filter the sub_menu belong to some parent menu 
			if p["id"] == m["parentID"]:
				if m["selected"] == True:
					# set the current menu's active 
					m["active"] = "active"
				p["children"].append(m)
	return parent_menu
