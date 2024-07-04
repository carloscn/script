# !/bin/bash

# Automated Ubuntu installation script

GIT_NAME="Carlos Wei"
GIT_EMAIL="carlos.wei.hk@gmail.com"

# Backup the existing sources.list file
sudo cp /etc/apt/sources.list /etc/apt/sources.list.bak

# Replace sources.list with Tsinghua University mirror
sudo cat <<EOF > /etc/apt/sources.list
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

echo "[INFO] sources.list has been updated and the package list has been refreshed."

sudo apt update && apt upgrade -y
echo "[INFO] apt update and upgrade done!"

sudo apt install tofrodos iproute2 gawk xvfb gcc git make net-tools libncurses5-dev zsh       \
tftpd zlib1g-dev libssl-dev flex bison libselinux1 gnupg wget diffstat chrpath socat xterm    \
autoconf libtool tar unzip texinfo gcc-multilib build-essential libsdl1.2-dev libglib2.0-dev  \
libssl-dev screen pax gzip vim net-tools cmake adb fastboot lzop    \
autoconf  automake bc bison build-essential ccache codespell cscope curl device-tree-compiler \
 expect flex ftp-upload gdisk libattr1-dev libcap-dev libfdt-dev libftdi-dev libglib2.0-dev   \
libgmp-dev libhidapi-dev libmpc-dev libpixman-1-dev libssl-dev libtool make mtools            \
netcat ninja-build python3-pycryptodome samba ntpdate  \
python3-pyelftools python3-serial rsync unzip uuid-dev xdg-utils xterm xz-utils vlc           \
zlib1g-dev proxychains libqt5qml5 libqt5quick5 libqt5quickwidgets5 qml-module-qtquick2        \
libgsettings-qt1 xinetd tftp-hpa xclip aria2 minicom guake openssh-client openssh-server libncursesw5 -y


sh -c "$(curl -fsSL https://gitee.com/mirrors/oh-my-zsh/raw/master/tools/install.sh \
    | sed 's|^REPO=.*|REPO=${REPO:-mirrors/oh-my-zsh}|g' \
    | sed 's|^REMOTE=.*|REMOTE=${REMOTE:-https://gitee.com/${REPO}.git}|g')"

cp ~/.zshrc ~/.zshrc.bak

# Use sed to replace the theme value
sed -i 's/^THEME=".*"/THEME="ys"/' ~/.zshrc

echo "[INFO] The theme in ~/.zshrc has been changed to 'ys'. A backup of the original file is saved as ~/.zshrc.bak."

# Append the specified text to the end of the .zshrc file
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

echo "The theme in ~/.zshrc has been changed to 'ys' and the new configurations have been appended. A backup of the original file is saved as ~/.zshrc.bak."

sudo echo "socks5 127.0.0.1 7891" >> /etc/proxychains.conf

echo "socks5 proxy configuration has been appended to /etc/proxychains.conf. A backup of the original file is saved as /etc/proxychains.conf.bak."

sudo ntpdate cn.pool.ntp.org
sudo timedatectl set-local-rtc 1 --adjust-system-clock

ssh-keygen -t rsa -N '' -f ${HOME}/.ssh/id_rsa && cat ~/.ssh/id_rsa.pub

git config --global core.editor "vim" && git config --global user.name ${GIT_NAME} && git config --global user.email ${GIT_EMAIL}

sudo apt install flameshot

curl -fsSL "https://raw.githubusercontent.com/carloscn/script/master/down_tool_chains/down_toolchain.sh " | bash
