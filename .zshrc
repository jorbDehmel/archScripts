# Created by newuser for 5.9
source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.plugin.zsh

git_branch() {
  OUT=$(git branch --show 2> /dev/null)
  if [ -n "$OUT" ]
  then
    echo " ($OUT)"
  fi
}

autoload -U colors && colors
autoload -U promptinit && promptinit
setopt PROMPT_SUBST
PROMPT='%{$fg[green]%}%n@%{$reset_color%}%{$fg[white]%}%m %{$reset_color%}%{$fg[green]%}%~%{$reset_color%}$(git_branch)> '

bindkey "^[[1;5C" forward-word
bindkey "^[[1;5D" backward-word
bindkey "^[[3~" delete-char
set -o sharehistory on
set -o extendedhistory on
set -o nohistbeep on
set -o histfindnodups on
set -o histignorealldups on
set -o histignoredups on
set -o histsavenodups on
set -o incappendhistory on
HISTSIZE=10000
SAVEHIST=10000
HISTFILE=~/.zsh_history
setopt SHARE_HISTORY
