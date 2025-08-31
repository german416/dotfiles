import subprocess
import os

from libqtile import bar, layout, qtile, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

mod = "mod4"
terminal = "wezterm"
browser_web = "firefox"
browser_file = "dolphin"
app_launcher = "rofi -show combi -sorting-method fzf"

keys = [
    # Move windows focus:
    # mod + key
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    # Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    # mod + shift + key
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    # mod + control + key
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod, "control"], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod, "control"], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen on the focused window",),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),

    # Custom binding
    # mod + key
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "b", lazy.spawn(browser_web), desc="Launch Firefox web browser"),
    Key([mod], "e", lazy.spawn(browser_file), desc="Launch file broser"),
    Key([mod], "space", lazy.spawn(app_launcher), desc="Launch rofi launcher"),
    Key([mod], "p", lazy.spawn("spectacle"), desc="Launch spectacle")
]

# Add key bindings to switch VTs in Wayland.
# We can't check qtile.core.name in default config as it is loaded before qtile is started
# We therefore defer the check until the key binding is run by using .when(func=...)
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc="Switch to VT{vt}",
        )
    )


groups = [Group(i) for i in "1234567890"]

for i in groups:
    keys.extend(
        [
            # mod + group number = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc=f"Switch to group {i.name}",
            ),
            # mod + shift + group number = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc=f"Switch to & move focused window to group {i.name}",
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod + shift + group number = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(
        border_focus_stack=["#00ff00", "#00ff00"],
        border_width=2,
        margin=0,
        split=False
    ),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="JetBrainsMono Nerd Font",
    fontsize=14,
    padding=0,
    foreground="#d3c6aa",     # Color del texto
    background="#2b3339",     # Fondo del widget
)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Spacer(),
                widget.CurrentLayoutIcon(
                    scale=0.8,
                    # padding=2,
                    # foreground="#d3c6aa",     # Color del texto
                    # background="#2b3339",     # Fondo del widget
                ),
                # widget.GroupBox(),
                widget.GroupBox(
                    # font="JetBrainsMono Nerd Font",
                    # fontsize=14,
                    # margin_y=0,
                    # margin_x=0,
                    # padding_y=50,
                    # padding_x=15,
                    # borderwidth=0,
                    # active="#a7c080",
                    # inactive="#83c092",
                    # rounded=False,
                    # highlight_method="block",
                    # this_current_screen_border="#83c092",
                    # this_screen_border="#00ff00",
                    # other_current_screen_border="#ffb86c",
                    # other_screen_border="#6272a4",
                    # urgent_border="#ff0000",
                    # disable_drag=True,
                    fmt=" {} ",
                    borderwidth=1,
                    active="#a7c080",         # Grupo activo (verde suave)
                    inactive="#83c092",       # Grupos inactivos (verde apagado)
                    rounded=False,
                    highlight_method="border", # o "line" si prefieres subrayado
                    this_current_screen_border="#dbbc7f",  # Resaltado dorado
                    this_screen_border="#2b3339",         # Fondo del tema
                    other_current_screen_border="#7fbbb3", # Azul verdoso (otro monitor)
                    other_screen_border="#3a515d",         # Fondo alternativo
                    urgent_border="#e67e80",  # Rojo para ventanas urgentes
                ),
                # widget.Prompt(),
                # widget.WindowName(),
                # widget.Chord(
                    # chords_colors={
                        # "launch": ("#00ff00", "#ffffff"),
                    # },
                    # name_transform=lambda name: name.upper(),
                #),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                widget.Spacer(),
                widget.Clock(format="%H:%M (%A, %B %d)"),
                widget.Systray(),
                # widget.QuickExit(),
            ],
            25,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# xcursor theme (string or None) and size (integer) for Wayland backend
wl_xcursor_theme = None
wl_xcursor_size = 24

# Nobody uses this string besides some java UI toolkits.
wmname = "LG3D"

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~")
    subprocess.Popen(["feh", "--bg-fill", f"{home}/Pictures/Wallpapers/landscape_07.jpg"])
    subprocess.Popen(["setxkbmap", "us", "-variant", "intl"])
    subprocess.Popen(["picom", "--config", f"{home}/.config/picom/picom.conf"])
