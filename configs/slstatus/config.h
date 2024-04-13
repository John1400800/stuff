static const struct arg args[] = {
	/* function        format          argument */
	{ cpu_perc,	 "CPU: %s%% | ",	NULL		},
	{ ram_perc,	 "RAM: %s%% | ",	NULL		},
	{ wifi_perc,     "NET: %s%% | ",	"wlp0s20f3"	},
	{ battery_state, "BAT: %s",		"BAT1"		},
	{ battery_perc,  "%s%% | ",		"BAT1"		},
	{ keymap,	 "%s | ",		NULL		},
	{ datetime,	 "%s",			"%a %d %b %R"	},
};
