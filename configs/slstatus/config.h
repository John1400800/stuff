static const struct arg args[] = {
	/* function        format          argument */
	{ cpu_perc,      "cpu: %s%% | ",  NULL	        },
	{ ram_used, 	   "ram: %s/", 	    NULL	        },
	{ ram_total, 	   "%s | ",  	      NULL 	        },
	{ datetime,  	   "%s | ",         "%a %d %b %T" },
	{ keymap,  	     "%s | ",  	      NULL  	      },
	{ wifi_perc,     "wifi: %s | ",   "wlp0s20f3"   },
	{ battery_state, "%s",            "BAT1" 	      },
	{ battery_perc,  "%s%%",          "BAT1" 	      },
};
