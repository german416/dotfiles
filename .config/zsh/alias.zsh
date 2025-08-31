# POWER LEVEL 10K
alias p10kc="p10k configure"

# BAT
alias cat="bat"

# CLS
alias cls="clear"

# FASTFETCH
alias ff="fastfetch"

# EZA
# alias ls="eza --icons=always --hyperlink --group-directories-first"
alias lsx="eza --long --header --all --group-directories-first --icons --git --changed --created --accessed --modified --time-style=iso"
alias ls="eza --icons=always --hyperlink --group-directories-first --all"

# NEOVIM
alias nv="nvim"

# ZOXIDE
alias zoxide="cd"

# TOUCH
alias tch="touch"

# EXIT
alias qq="exit"

# ZYPPER
alias zyp="sudo zypper"
alias zypin="sudo zypper install"
alias zypse="zypper search"
alias zypre="sudo zypper remove"

# LAZY GIT
alias lg="lazygit"
alias lgh="lazygit -p $HOME"
alias lgn="lazygit -p $HOME/.config/nvim"

# RUTAS
alias cdh="zoxide $HOME"
alias cdc="cd $HOME/.config"
alias cdz="cd $HOME/.config/zsh"
alias cd.="cd .."
alias cdn="cd $HOME/.config/nvim"
alias cdr="zoxide $HOME/Repos"

# ARCHIVOS RO
alias _alias="bat --language zsh $HOME/.config/zsh/alias"

# ARCHIVOS RW
alias __alias="nvim $HOME/.config/zsh/alias.zsh"
alias __zrc="nvim $HOME/.config/zsh/.zshrc"
alias __znv="nvim $HOME/.zshenv"
alias __p10="nvim $HOME/p10k.zsh"
alias __nvm="nvim $HOME/.config/nvim"
alias __wez="nvim $HOME/.config/wezterm/wezterm.lua"
alias __qtl="nvim $HOME/.config/qtile/"
