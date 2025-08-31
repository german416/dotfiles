local wezterm = require("wezterm")

return {
	font = wezterm.font("JetBrains Mono Nerd Font"),
	font_size = 12.0,
	enable_tab_bar = false,

	window_padding = {
		left = 2,
		right = 2,
		top = 0,
		bottom = 0,
	},

	color_scheme_dirs = { "~/.config/wezterm/colors" },
	-- https://github.com/frdwin/everforest-for-wezterm
	color_scheme = "Everforest Dark (Hard)",
	-- color_scheme = "Everforest Dark (Medium)",
	-- color_scheme = "Everforest Dark (Soft)",
	-- color_scheme = "BlulocoDark",
	-- color_scheme = "Gruvbox Dark",
}
