#!/bin/bash

# Automated Ubuntu installation script

GIT_NAME="Carlos Wei"
GIT_EMAIL="carlos.wei.hk@gmail.com"
LOG_FILE="${HOME}/install_script.log"
STATUS_SUCCESS=0

# Function to check the result of the last executed command
check_command() {
  if [ $1 -ne $STATUS_SUCCESS ]; then
    echo "[ERROR] $2 failed with status $1" | tee -a $LOG_FILE
    exit $1
  else
    echo "[INFO] $2 succeeded" | tee -a $LOG_FILE
    echo $2 >> $LOG_FILE
  fi
}

# Function to check if a command has already been executed
is_command_executed() {
  grep -Fxq "$1" $LOG_FILE
}

# Initialize log file
touch $LOG_FILE

# Backup the existing sources.list file
is_command_executed "backup_sources_list" || {
  sudo cp /etc/apt/sources.list /etc/apt/sources.list.bak
  check_command $? "backup_sources_list"
}

# Replace sources.list with Tsinghua University mirror
is_command_executed "update_sources_list" || {
  sudo tee /etc/apt/sources.list > /dev/null <<EOF
# Default commented out source mirrors to speed up apt update, uncomment if needed
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ noble main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ noble main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ noble-updates main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ noble-updates main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ noble-backports main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ noble-backports main restricted universe multiverse

# Security updates, includes official sources and mirror configurations, modify as needed
deb http://security.ubuntu.com/ubuntu/ noble-security main restricted universe multiverse
# deb-src http://security.ubuntu.com/ubuntu/ noble-security main restricted universe multiverse

# Proposed updates, not recommended to enable
# deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ noble-proposed main restricted universe multiverse
# # deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ noble-proposed main restricted universe multiverse
EOF
  check_command $? "update_sources_list"
  sudo apt update && sudo apt upgrade -y
  check_command $? "apt_update_upgrade"
}

# Install packages
is_command_executed "install_packages" || {
  sudo apt install tofrodos iproute2 gawk xvfb gcc git make net-tools libncurses5-dev zsh \
    tftpd zlib1g-dev libssl-dev flex bison libselinux1 gnupg wget diffstat chrpath socat xterm \
    autoconf libtool tar unzip texinfo gcc-multilib build-essential libsdl1.2-dev libglib2.0-dev \
    libssl-dev screen pax gzip vim net-tools cmake adb fastboot lzop \
    autoconf automake bc bison build-essential ccache codespell cscope curl device-tree-compiler \
    expect flex ftp-upload gdisk libattr1-dev libcap-dev libfdt-dev libftdi-dev libglib2.0-dev \
    libgmp-dev libhidapi-dev libmpc-dev libpixman-1-dev libssl-dev libtool make mtools \
    netcat ninja-build python3-pycryptodome samba ntpdate \
    python3-pyelftools python3-serial rsync unzip uuid-dev xdg-utils xterm xz-utils vlc \
    zlib1g-dev proxychains libqt5qml5 libqt5quick5 libqt5quickwidgets5 qml-module-qtquick2 \
    libgsettings-qt1 xinetd tftp-hpa xclip aria2 minicom guake openssh-client openssh-server libncursesw5 -y
  check_command $? "install_packages"
}

# Install Oh My Zsh
is_command_executed "install_oh_my_zsh" || {
  sh -c "$(curl -fsSL https://gitee.com/mirrors/oh-my-zsh/raw/master/tools/install.sh \
    | sed 's|^REPO=.*|REPO=${REPO:-mirrors/oh-my-zsh}|g' \
    | sed 's|^REMOTE=.*|REMOTE=${REMOTE:-https://gitee.com/${REPO}.git}|g')"
  check_command $? "install_oh_my_zsh"
}

# Backup and modify ~/.zshrc
is_command_executed "modify_zshrc" || {
  cp ~/.zshrc ~/.zshrc.bak
  sed -i 's/^THEME=".*"/THEME="ys"/' ~/.zshrc
  check_command $? "modify_zshrc_theme"
  cat <<EOF >> ~/.zshrc

# Custom aliases and functions
alias ks="proxychains"

proxy_on () {
  export http_proxy="http://127.0.0.1:7891"
  export https_proxy="http://127.0.0.1:7891"
  echo "[INFO] zsh HTTP Proxy on"
}

proxy_off () {
  unset http_proxy
  unset https_proxy
  echo "[INFO] zsh HTTP Proxy off"
}

proxy_off
EOF
  check_command $? "append_zshrc_custom_aliases"
}

# Append proxy configuration to /etc/proxychains.conf
is_command_executed "update_proxychains_conf" || {
  echo "socks5 127.0.0.1 7891" | sudo tee -a /etc/proxychains.conf > /dev/null
  check_command $? "update_proxychains_conf"
}

# Sync time with NTP server
is_command_executed "sync_time" || {
  sudo ntpdate cn.pool.ntp.org
  check_command $? "ntpdate"
  sudo timedatectl set-local-rtc 1 --adjust-system-clock
  check_command $? "timedatectl"
}

# Generate SSH keys
is_command_executed "generate_ssh_keys" || {
  ssh-keygen -t rsa -N '' -f ${HOME}/.ssh/id_rsa && cat ~/.ssh/id_rsa.pub
  check_command $? "generate_ssh_keys"
}

# Configure git
is_command_executed "configure_git" || {
  git config --global core.editor "vim"
  check_command $? "configure_git_editor"
  git config --global user.name "${GIT_NAME}"
  check_command $? "configure_git_username"
  git config --global user.email "${GIT_EMAIL}"
  check_command $? "configure_git_email"
}

# Install flameshot
is_command_executed "install_flameshot" || {
  sudo apt install flameshot -y
  check_command $? "install_flameshot"
}

# Download and run toolchain script
is_command_executed "download_toolchain_script" || {
  curl -fsSL "https://raw.githubusercontent.com/carloscn/script/master/down_tool_chains/down_toolchain.sh" | bash
  check_command $? "download_toolchain_script"
}

echo "[INFO] Script execution completed."