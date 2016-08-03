# _*_ coding: utf-8 _*_

role_config = ["admin", "operator", "user"]

menu_config = [
	{"name":"Dashboard", "url":"/home/", "icon":"fa-dashboard", "openable":False,"active":"","children":[]},
	{"name":"Server Management", "url":"/server/", "icon":"fa-cloud", "openable":True,"active":"","children":[
		{"name":"Server", "url":"/server/","icon":"fa-desktop", "openable":False,"active":"","children":[]},
		{"name":"Device", "url":"/device/","icon":"fa-plus", "openable":False,"active":"","children":[]},
	]},
	{"name":"Cluster Management", "url":"/cluster/", "icon":"fa-cloud", "openable":True,"active":"","children":[
		{"name":"Cluster", "url":"/cluster/","icon":"fa-star", "openable":False,"active":"","children":[]},
		{"name":"Pool", "url":"/pool/","icon":"fa-database", "openable":False,"active":"","children":[]},
		{"name":"EC Profile", "url":"/ec_profile/","icon":"fa-database", "openable":False,"active":"","children":[]},
		{"name":"RBD", "url":"/rbd/","icon":"fa-database", "openable":False,"active":"","children":[]},
		{"name":"Storage Group", "url":"/crushmap/","icon":"fa-users", "openable":False,"active":"","children":[]},
		{"name":"Zone", "url":"/zone/","icon":"fa-sitemap", "openable":False,"active":"","children":[]},
		{"name":"Ceph Upgrade", "url":"/upgrade/ceph/","icon":"fa-file-text-o", "openable":False,"active":"","children":[]},
	]},
	{"name":"Performance", "url":"", "icon":"fa-bar-chart-o", "openable":True,"active":"","children":[
		{"name":"Monitor", "url":"/performance/monitor/","icon":"fa-arrows", "openable":False,"active":"","children":[]},
	]},
	{"name":"Integrate", "url":"", "icon":"fa-external-link", "openable":True,"active":"","children":[
		{"name":"Openstack", "url":"/integrate/openstack/","icon":"fa-retweet", "openable":False,"active":"","children":[]},
		{"name":"Hadoop", "url":"/integrate/hadoop/","icon":"fa-database", "openable":False,"active":"","children":[]},
	]},
	{"name":"System Management", "url":"", "icon":"fa-cogs", "openable":True,"active":"","children":[
		{"name":"Settings", "url":"/settings/","icon":"fa-file-text-o", "openable":False,"active":"","children":[]},
		{"name":"Account", "url":"/account/","icon":"fa-file-text-o", "openable":False,"active":"","children":[]},
	]}
]

role_menu_config = [
    {
		"role":"admin", 
	 	"menu_list":[
			"Dashboard", 
			"Server Management", "Server", "Device",
			"Cluster Management", "Cluster", "EC Profile", "RBD", "Storage Group", "Zone", "Ceph Upgrade",
			"Performance", "Monitor", 
			"Integrate", "Openstack", "Hadoop",
			"System Management","Account",
	 	]
	},
	{
		"role":"operator", 
	 	"menu_list":[
			"Dashboard", 
			"Server Management", "Server", "Device",
			"Cluster Management", "Cluster", "EC Profile", "RBD", "Storage Group", "Zone", "Ceph Upgrade",
			"Performance", "Monitor", 
			"Integrate", "Openstack", "Hadoop"
	 	]
	},
	{
		"role":"user", 
	 	"menu_list":[
			"Dashboard", 
			"Performance", "Monitor", 
	 	]	
	}
]