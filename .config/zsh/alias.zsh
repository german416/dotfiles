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

# APTITUDE
alias aptin="sudo apt install"
alias aptse="apt search"
alias aptsh="apt show"
alias aptls="apt list --installed"

# LAZY GIT
alias lg="lazygit"
alias lgh="lazygit -p $HOME"
alias lgn="lazygit -p $HOME/.config/nvim"

# RUTAS
alias cdh="zoxide $HOME"
alias cdc="cd $HOME/.config"
alias cdz="cd $HOME/.config/zsh"
alias cdd="cd .."
alias cdn="cd $HOME/.config/nvim"
alias cdr="zoxide $HOME/Repos"

# ARCHIVOS RO
alias _alias="bat --language zsh $HOME/.config/zsh/alias"

# ARCHIVOS RW
alias __ali="cd $HOME/.config/zsh/ && nvim alias.zsh"
alias __zrc="cd $HOME/.config/zsh/ && nvim .zshrc"
alias __znv="cd $HOME/ && nvim .zshenv"
alias __p10="cd $HOME/.config/zsh/ && nvim p10k.zsh"
alias __nvm="cd $HOME/.config/nvim/ && nvim ."
alias __wez="cd $HOME/.config/wezterm/ && nvim ."
alias __qtl="cd $HOME/.config/qtile/ && nvim ."
