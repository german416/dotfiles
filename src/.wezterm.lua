local wezterm = require("wezterm")

return {
	font = wezterm.font("JetBrains Mono Nerd Font"),
	font_size = 12.0,
	enable_tab_bar = false,

	window_padding = {
		left = 5,
		right = 5,
		top = 0,
		bottom = 0,
	},

	-- color_scheme = "Tokyo Night Day",
	-- color_scheme = "BlulocoLight",
	color_scheme = "BlulocoDark",

	-- Opcionalmente podés setear un esquema de color acá (te explico más abajo)
	-- color_scheme = "Gruvbox Dark",
}
