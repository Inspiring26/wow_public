#! /bin/bash

export PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"

function shadowsocksconfig(){
    SSLOCAL="[\"[::0]\",\"0.0.0.0\"]"
    PORT="443"
    LOACL="127.0.0.1"
    LOCALPORT="1080"
    PASSWORD=""
    DNS="8.8.8.8"
    TIMEOUT="600"
    METHOD="aes-256-cfb"
    OBFS="http"
    OBFSHOST="www.icloud.com"
    WORKERS="1024"
    BBR="enable"
    FWS="enable"
    ABB="enable"
}

function systemconfig(){
    IPREGEX="^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"
    ETH=""
    PUBLICIP=""
    PUBLICIPv6=""
}

function install_twist(){
    clear
    twist
    notice
    rootness
    disableselinux
    shadowsocksconfig
    systemconfig
    detectsystem
    installlibs
    configbbr
    installsslibev
    configsslibev
    configiptables
    startservices
    twiststatus
}

function update_twist(){
    clear
    twist
    echo -e "#[\033[32;1m                Update Twist Shadowsocks-libev                   \033[0m]#"
    echo -e "#[\033[32;1m                Update will Start in 5 Seconds\033[0m                   ]#"
    echo "#####################################################################"
    echo ""
    sleep 5
    rootness
    systemconfig
    if [ -e /etc/init.d/shadowsocks ]; then
        /etc/init.d/shadowsocks stop
    else
        echo -e "#[\033[31;1m             Twist was Not Find on Your Server!\033[0m                  ]#"
        echo ""
        exit 1
    fi
    rm -f /usr/local/bin/ss-local
    rm -f /usr/local/bin/ss-tunnel
    rm -f /usr/local/bin/ss-server
    rm -f /usr/local/bin/ss-manager
    rm -f /usr/local/bin/ss-redir
    rm -f /usr/local/bin/ss-nat
    rm -f /usr/local/lib/libshadowsocks-libev.a
    rm -f /usr/local/lib/libshadowsocks-libev.la
    rm -f /usr/local/include/shadowsocks.h
    rm -f /usr/local/lib/pkgconfig/shadowsocks-libev.pc
    rm -f /usr/local/share/man/man1/ss-local.1
    rm -f /usr/local/share/man/man1/ss-tunnel.1
    rm -f /usr/local/share/man/man1/ss-server.1
    rm -f /usr/local/share/man/man1/ss-manager.1
    rm -f /usr/local/share/man/man1/ss-redir.1
    rm -f /usr/local/share/man/man1/ss-nat.1
    rm -f /usr/local/share/man/man8/shadowsocks-libev.8
    rm -fr /usr/local/share/doc/shadowsocks-libev
    disableselinux
    detectsystem
    installlibs
    installsslibev
    startservices
    clear
    twist
    echo -e "#[\033[32;1m                      Twist Update Finished\033[0m                       ]#"
    echo "######################################################################"
    echo ""
    exit 1
}

function uninstall_twist(){
    clear
    twist
    echo -e "#[\033[31;1m              Uninstall Twist Shadowsocks-libev                  \033[0m]#"
    echo -e "#[\033[31;1m              Uninstall will Start in 5 Seconds\033[0m                  ]#"
    echo "#####################################################################"
    echo ""
    sleep 5
    rootness
    sed -i "/# Twist/d" /etc/sysctl.conf
    if [ -e /etc/init.d/shadowsocks ]; then
        /etc/init.d/shadowsocks stop
    else
        echo -e "#[\033[31;1m             Twist was Not Find on Your Server!\033[0m                  ]#"
        echo ""
        exit 1
    fi
    if grep -Eqi "Ubuntu|Debian|Raspbian|Arch Linux" /etc/*-release || grep -Eqi "Ubuntu|Debian|Raspbian|Arch Linux" /proc/version; then
        update-rc.d -f shadowsocks remove
        iptables -I INPUT -m state --state NEW -m tcp -p tcp --dport $PORT -j DROP
        iptables -I INPUT -m state --state NEW -m udp -p udp --dport $PORT -j DROP
    fi
    if grep -Eqi "CentOS|Red Hat|Fedora" /etc/*-release || grep -Eqi "CentOS|Red Hat|Fedora" /proc/version; then
        chkconfig --del shadowsocks
        systemctl start firewalld
        firewall-cmd --permanent --zone=public --remove-port=${PORT}/tcp
        firewall-cmd --permanent --zone=public --remove-port=${PORT}/udp
        firewall-cmd --reload
    fi
    ps -ef | grep -v grep | grep -i "ss-server"
    update-rc.d -f shadowsocks remove
    rm -fr /etc/shadowsocks-libev
    rm -f /usr/local/bin/ss-local
    rm -f /usr/local/bin/ss-tunnel
    rm -f /usr/local/bin/ss-server
    rm -f /usr/local/bin/ss-manager
    rm -f /usr/local/bin/ss-redir
    rm -f /usr/local/bin/ss-nat
    rm -f /usr/local/lib/libshadowsocks-libev.a
    rm -f /usr/local/lib/libshadowsocks-libev.la
    rm -f /usr/local/include/shadowsocks.h
    rm -f /usr/local/lib/pkgconfig/shadowsocks-libev.pc
    rm -f /usr/local/share/man/man1/ss-local.1
    rm -f /usr/local/share/man/man1/ss-tunnel.1
    rm -f /usr/local/share/man/man1/ss-server.1
    rm -f /usr/local/share/man/man1/ss-manager.1
    rm -f /usr/local/share/man/man1/ss-redir.1
    rm -f /usr/local/share/man/man1/ss-nat.1
    rm -f /usr/local/share/man/man8/shadowsocks-libev.8
    rm -fr /usr/local/share/doc/shadowsocks-libev
    rm -f /etc/init.d/shadowsocks
    clear
    twist
    echo -e "#[\033[32;1m                Twist Uninstallation Finished\033[0m                     ]#"
    echo "######################################################################"
    echo ""
    exit 1
}

function twist(){
    echo "######################################################################"
    echo "#####################################################################"
    echo "       ###       ###         ###     ###      #########    #########"
    echo "       ###        ###    #  ###     ###      ##               ##"
    echo "       ###         ###  ## ###     ###      #########        ##"
    echo "       ###          ### ## ##     ###             ##        ##"
    echo "       ###           ### ###     ###      #########        ##"
    echo ""
}

function notice(){
    echo -e "#[\033[32;1m         Install Shadowsocks-libev Script By Unbinilium\033[0m           ]#"
    echo -e "#[\033[32;1m             Installation will Start in 5 Seconds\033[0m                 ]#"
    echo "######################################################################"
    echo ""
    sleep 5
}

function rootness(){
    if [ $EUID -ne 0 ]; then
        echo -e "# [\033[31;1mError:Twist must be run as root. Please Run Twist with root Access!\033[0m]" 1>&2
        echo ""
        exit 1
    fi
}

function disableselinux(){
    if [ -s /etc/selinux/config ] && grep 'SELINUX=enforcing' /etc/selinux/config; then
        sed -i 's/SELINUX=enforcing/SELINUX=disabled/g' /etc/selinux/config
        setenforce 0
    fi
}

function detectsystem(){
    if grep -Eqi "Ubuntu|Debian|Raspbian|Arch Linux" /etc/*-release || grep -Eqi "Ubuntu|Debian|Raspbian|Arch Linux" /proc/version; then
        systemtype="1"
    elif grep -Eqi "CentOS|Red Hat|Fedora" /etc/*-release || grep -Eqi "CentOS|Red Hat|Fedora" /proc/version; then
        systemtype="0"
    else
        echo -e "# [\033[31;1mThis Script Must be Run on CentOS, Red Hat, Fedora, Ubuntu, Debian or Arch Linux. Aborating!\033[0m]"
        echo ""
        exit 1
    fi
    if [ ! -z "$(which apt)" ]; then
        packagemanagertype="a"
    elif [ ! -z "$(which yum)" ]; then
        packagemanagertype="y"
    elif [ ! -z "$(which pacman)" ]; then
        packagemanagertype="p"
    else
        echo -e "# [\033[31;1mThis Script Must be Run on CentOS, Red Hat, Ubuntu, Debian or Arch Linux. Aborating!\033[0m]"
        echo ""
        exit 1
    fi
    if [ -f /proc/user_beancounters ]; then
        BBR="disable"
        if [ "$packagemanagertype" = "a" ]; then
            systemtype="1"
        elif [ "$packagemanagertype" = "y" ]; then
            systemtype="0"
        elif [ "$packagemanagertype" = "p" ]; then
            systemtype="1"
        fi
    fi
    kernelverheader="$(uname -r | grep -oE '[0-9]+\.[0-9]+')"
    if [ $(echo ${kernelverheader} | awk -v ver=4.10 '{print($1>ver)? "1":"0"}') -eq "0" ]; then
        [ "$BBR" = "enable" ] && serverrestart="true"
    fi
    if [ -z "$ETH" ]; then
        ETH="$(route 2>/dev/null | grep '^default' | grep -o '[^ ]*$')"
        [ -z "$ETH" ] && ETH="$(ip -4 route list 0/0 | grep -Po '(?<=dev )(\S+)')"
    fi
    ethstatus="$(cat /sys/class/net/${ETH}/operstate)"
    if [ -z "$ethstatus" ] || [ "$ethstatus" = "down" ]; then
        echo -e "# [\033[31;1mNetwork Interface '${ETH}' is Not Available. Please try Another Network Interface Listed Below!\033[0m]"
        echo ""
        ip link
        echo ""
        echo -e "Please Enter [\033[32;1mNetwork Interface Name\033[0m]:"
        read -p "Input Devices Name:" eth
     	if [ ! "$eth" = "" ]; then
            ethstatus="$(cat /sys/class/net/${eth}/operstate)"
            if [ -z "$ethstatus" ] || [ "$ethstatus" = "down" ]; then
                echo ""
                echo -e "# [\033[31;1mNetwork Interface Your Entered is Not Available. Aborting!\033[0m]"
                echo ""
                exit 1
            else
                ETH="$eth"
                echo ""
                echo -e "# [\033[33;1mNetwork Interface Check Passed and Using Interface\033[0m \033[32;1m${ETH}\033[0m]"
                echo ""
            fi
        fi
    fi
    [ -z "$PUBLICIP" ] && PUBLICIP="$(dig @resolver1.opendns.com -t A -4 myip.opendns.com +short)"
    if ! printf %s "$PUBLICIP" | grep -Eq "$IPREGEX"; then
        echo ""
        echo -e "# [\033[31;1mCannot Detect Valid Public IP. Please Fill Your IP Address Below!\033[0m]"
        read -p "Input Your Public IP:" publicip
        if ! printf %s "$publicip" | grep -Eq "$IPREGEX"; then
            echo ""
            echo -e "# [\033[31;1mThe IP:${publicip} The IP Address You Entered is Out of Range. You May Unable to Connect!\033[0m]"
            echo ""
            sleep 3
        else
            PUBLICIP="$publicip"
            echo ""
            echo -e "# [\033[32;1mYou are now using Public IP:${PUBLICIP}\033[0m]"
            echo ""
        fi
    fi
    [ -z "$(ip -6 addr show ${ETH})" ] && { SSLOCAL="\"0.0.0.0\""; AddrV6="false"; }
    [ -z "$PUBLICIPv6" ] && PUBLICIPv6="$(curl -s diagnostic.opendns.com/myip)"
    [ -z "$PUBLICIPv6" ] && AddrV6="false"
    [ "$PUBLICIPv6" = "$PUBLICIP" ] && AddrV6="false"
}

function installlibs(){
    if [ "$packagemanagertype" = "a" ]; then
        apt-get -yq update || { echo ""; echo -e "# [\033[31;1mCannot Update Source, Please Check Your Network or Errors Noticed!\033[0m]"; echo ""; exit 1; }
        apt-get -yq upgrade || { echo ""; echo -e "# [\033[31;1mCannot Upgrade Source, Please Check Your Network or Errors Noticed!\033[0m]"; echo ""; exit 1; }
        apt-get -yq install wget dnsutils git gawk grep sed net-tools rng-tools curl gcc swig make perl cpio libc-ares-dev || { echo ""; echo -e "# [\033[31;1mCannot Install Depends On, Please Check Your Network or Errors Noticed!\033[0m]"; echo ""; exit 1; }
        apt-get -yq install gettext autoconf automake libtool openssl libssl-dev zlib1g-dev xmlto asciidoc libpcre3-dev libudns-dev libev-dev || { echo ""; echo -e "# [\033[31;1mCannot Install Depends On, Please Check Your Network or Errors Noticed!\033[0m]"; echo ""; exit 1; }
        apt-get -yq install python-dev python-pip python-setuptools python-m2crypto build-essential libevent-dev fail2ban || { echo ""; echo -e "# [\033[31;1mCannot Install Depends On, Please Check Your Network or Errors Noticed!\033[0m]"; echo ""; exit 1; }
        easy_install -q greenlet gevent
        [ "$FWS" = "enable" ] && { apt-get -yq install apache2 || { echo ""; echo -e "# [\033[31;1mCannot Install Apache as Fake Web Server, Please Check Your Network or Errors Noticed!\033[0m]"; echo ""; exit 1; }; }
    elif [ "$packagemanagertype" = "y" ]; then
        yum -y update || { echo ""; echo -e "# [\033[31;1mCannot Update Source, Please Check Your Network or Errors Noticed!\033[0m]"; echo ""; exit 1; }
        yum -y upgrade || { echo ""; echo -e "# [\033[31;1mCannot Upgrade Source, Please Check Your Network or Errors Noticed!\033[0m]"; echo ""; exit 1; }
        yum -y install epel-release yum-utils bind-utils || { echo -e "# [\033[31;1mCannot Add EPEL repository. Aborting!\033[0m]"; exit 1; }
        yum-config-manager --enable epel || { echo -e "# [\033[31;1mCannot Enable EPEL repository. Aborting!\033[0m]"; exit 1; }
        yum -y install wget gawk grep cpio swig sed net-tools greenlet rng-tools pcre-devel perl-devel expat-devel openssl-devel || { echo ""; echo -e "# [\033[31;1mCannot Install Depends On, Please Check Your Network or Errors Noticed!\033[0m]"; echo ""; exit 1; }
        yum -y install gcc gettext-devel autoconf automake make zlib-devel libtool xmlto asciidoc git udns-devel libev-devel c-ares-devel || { echo ""; echo -e "# [\033[31;1mCannot Install Depends On, Please Check Your Network or Errors Noticed!\033[0m]"; echo ""; exit 1; }
        yum -y install python-devel python-setuptools python-pip libevent curl curl-devel zlib-devel gevent fail2ban || { echo ""; echo -e "# [\033[31;1mCannot Install Depends On, Please Check Your Network or Errors Noticed!\033[0m]"; echo ""; exit 1; }
        [ "$FWS" = "enable" ] && { yum -y install httpd || { echo ""; echo -e "# [\033[31;1mCannot Install Apache as Fake Web Server, Please Check Your Network or Errors Noticed!\033[0m]"; echo ""; exit 1; }; }
    else
        pacman -Syu --noconfirm || { echo ""; echo -e "# [\033[31;1mCannot Update Source, Please Check Your Network or Errors Noticed! \033[0m]"; echo ""; exit 1; }
        pacman -S --noconfirm wget git gawk grep sed net-tools rng-tools curl perl cpio || { echo ""; echo -e "# [\033[31;1mCannot Install Depends On, Please Check Your Network or Errors Noticed!\033[0m]"; echo ""; exit 1; }
        pacman -S --noconfirm gettext gcc autoconf libtool autoconf automake make asciidoc xmlto udns libev || { echo ""; echo -e "# [\033[31;1mCannot Install Depends On, Please Check Your Network or Errors Noticed!\033[0m]"; echo ""; exit 1; }
        pacman -S --noconfirm python python-pip python-setuptools python2-m2crypto python-greenlet python-gevent openssl fail2ban || { echo ""; echo -e "# [\033[31;1mCannot Install Depends On, Please Check Your Network or Errors Noticed!\033[0m]"; echo ""; exit 1; }
        [ "$FWS" = "enable" ] && { pacman -S --noconfirm apache || { echo ""; echo -e "# [\033[31;1mCannot Install Apache as Fake Web Server, Please Check Your Network or Errors Noticed!\033[0m]"; echo ""; exit 1; }; }
    fi
    pip install -q qrcode || { echo ""; echo -e "# [\033[31;1mCannot Install QRCode, You are Unable to Configure Clients by Using QRCode!\033[0m]"; echo ""; sleep 3; }
}

function configbbr(){
    if [ "$BBR" = "enable" ]; then
        if [ $(echo ${kernelverheader} | awk -v ver=4.10 '{print($1>ver)? "1":"0"}') -eq "1" ] || [ "$kernelupdated" = "true" ]; then
            if [ ! "$(sysctl net.ipv4.tcp_available_congestion_control | awk '{print $3}')" = "bbr" ]; then
                sed -i '/net.ipv4.tcp_congestion_control/d' /etc/sysctl.conf
                echo "net.ipv4.tcp_congestion_control = bbr" >> /etc/sysctl.conf
            fi
        else
            echo "net.ipv4.tcp_congestion_control = hybla" >> /etc/sysctl.conf
            updatekernel
        fi
    fi
}

function updatekernel(){
    if [ "$packagemanagertype" = "a" ]; then
        KERNELVER="$(wget -qO- http://kernel.ubuntu.com/~kernel-ppa/mainline/ | awk -F'\"v' '/v[4-9]./{print $2}' | cut -d/ -f1 | grep -v -  | sort -V | tail -1)"
        [ -z "$KERNELVER" ] && { BBR="disable"; echo -e "# [\033[31;1mCannot Get Newest Linux KERNEL Verison, BBR will NOT Enabled on Your Server!\033[0m]"; }
        if [ "$BBR" = "enable" ]; then
            SYSTYPE="$(dpkg --print-architecture)"
            [ "$SYSTYPE" = "amd64" ] && KERNEL="$(wget -qO- http://kernel.ubuntu.com/~kernel-ppa/mainline/v${KERNELVER}/ | grep "linux-image" | grep "generic" | awk -F'\">' '/amd64.deb/{print $2}' | cut -d'<' -f1 | head -1)"
            [ "$SYSTYPE" = "i386" ] && KERNEL="$(wget -qO- http://kernel.ubuntu.com/~kernel-ppa/mainline/v${KERNELVER}/ | grep "linux-image" | grep "generic" | awk -F'\">' '/i386.deb/{print $2}' | cut -d'<' -f1 | head -1)"
            [ "$SYSTYPE" = "armhf" ] && KERNEL="$(wget -qO- http://kernel.ubuntu.com/~kernel-ppa/mainline/v${KERNELVER}/ | grep "linux-image" | grep "generic" | awk -F'\">' '/armhf.deb/{print $2}' | cut -d'<' -f1 | head -1)"
            [ "$SYSTYPE" = "arm64" ] && KERNEL="$(wget -qO- http://kernel.ubuntu.com/~kernel-ppa/mainline/v${KERNELVER}/ | grep "linux-image" | grep "generic" | awk -F'\">' '/arm64.deb/{print $2}' | cut -d'<' -f1 | head -1)"
            [ "$SYSTYPE" = "ppc64el" ] && KERNEL="$(wget -qO- http://kernel.ubuntu.com/~kernel-ppa/mainline/v${KERNELVER}/ | grep "linux-image" | grep "generic" | awk -F'\">' '/ppc64el.deb/{print $2}' | cut -d'<' -f1 | head -1)"
            [ "$SYSTYPE" = "s390x" ] && KERNEL="$(wget -qO- http://kernel.ubuntu.com/~kernel-ppa/mainline/v${KERNELVER}/ | grep "linux-image" | grep "generic" | awk -F'\">' '/s390x.deb/{print $2}' | cut -d'<' -f1 | head -1)"
            [ -z "$KERNEL" ] && { echo ""; echo -e "[# \033[31;1mUnable to Get New KERNEL, BBR will NOT Enabled on Your Server!\033[0m]"; echo ""; sleep 3; BBR="disable"; }
            [ "$BBR" = "enable" ] && wget -t 3 -T 30 -nv -O "$KERNEL" "http://kernel.ubuntu.com/~kernel-ppa/mainline/v${KERNELVER}/${KERNEL}" || { echo ""; echo -e "# [\033[31;1mCannot Download Linux KERNEL, Please Check Your Network or Errors Noticed, BBR will NOT Enabled on Your Server!\033[0m]"; echo ""; sleep 3; BBR="disable"; }
            [ "$BBR" = "enable" ] && { dpkg -i $KERNEL || { echo ""; echo -e "# [\033[31;1mCannot Update Kernel, BBR will NOT Enabled on Your Server!\033[0m]"; echo ""; sleep 3; BBR="disable"; }; }
            [ "$BBR" = "enable" ] && { dpkg -l | grep linux-image; rm -f $KERNEL; update-grub; }
        fi
    elif [ "$packagemanagertype" = "y" ]; then
        yum --enablerepo=elrepo-kernel install kernel-ml kernel-ml-devel || { echo ""; echo -e "# [\033[31;1mCannot Update Kernel, BBR will NOT Enabled on Your Server!\033[0m]"; echo ""; sleep 3; BBR="disable"; }
        if grep -qs "release 7" /etc/*-release; then
            [ "$BBR" = "enable" ] && grub2-set-default 0
        elif grep -qs "release 6" /etc/*-release; then
            [ "$BBR" = "enable" ] && sed -i 's/^default=.*/default=0/g' /boot/grub/grub.conf
        fi
    elif [ "$packagemanagertype" = "p" ]; then
        if grep -Eqi "IgnorePkg|IgnoreGroup" /etc/pacman.conf; then
            sed -i "/IgnorePkg/d;/IgnoreGroup/d" /etc/pacman.conf
        fi
        pacman -Syu --noconfirm || { echo ""; echo -e "# [\033[31;1mCannot Update Kernel Source, BBR will NOT Enabled on Your Server!\033[0m]"; echo ""; sleep 3; BBR="disable"; }
    fi
    [ "$BBR" = "enable" ] && { kernelupdated="true"; serverrestart="true"; }
    kernelverheader="$(uname -r | grep -oE '[0-9]+\.[0-9]+')"
    configbbr
}

function installsslibev(){
    libsodiumver="$(wget -qO- https://api.github.com/repos/jedisct1/libsodium/releases/latest | grep 'tag_name' | cut -d\" -f4)"
    wget -t 3 -T 30 -nv -O libsodium-${libsodiumver}.tar.gz https://github.com/jedisct1/libsodium/releases/download/${libsodiumver}/libsodium-${libsodiumver}.tar.gz
    [ "$?" != "0" ] && { echo ""; echo -e "# [\033[31;1mCannot Download Libsodium Source. Aborting!\033[0m]"; echo ""; exit 1; }
    [ -d libsodium-${libsodiumver} ] && rm -rf libsodium-${libsodiumver}
    tar zxf libsodium-${libsodiumver}.tar.gz
    pushd libsodium-${libsodiumver}
    ./configure --prefix=/usr && make && make install || { echo ""; echo －e "# [\033[31;1mLibsodium Failed to Build. Aborting!\033[0m]"; echo ""; exit 1; }
    popd
    ldconfig
    mbedver="$(wget -qO- https://tls.mbed.org/download-archive | grep -oE '[0-9]+\.[0-9]+\.[0-9]+' | cut -d'.' -f1,2,3 | sort -V | tail -1)"
    wget -t 3 -T 30 -nv -O mbedtls-${mbedver}-gpl.tgz https://tls.mbed.org/download/mbedtls-${mbedver}-gpl.tgz
    [ "$?" != "0" ] && { echo ""; echo -e "# [\033[31;1mCannot Download mbed Source. Aborting!\033[0m]"; echo ""; exit 1; }
    [ -d mbedtls-${mbedver} ] && rm -rf mbedtls-${mbedver}
    tar xf mbedtls-${mbedver}-gpl.tgz
    pushd mbedtls-${mbedver}
    make SHARED=1 CFLAGS=-fPIC
    make DESTDIR=/usr install || { echo ""; echo －e "# [\033[31;1mmbed Failed to Build. Aborting!\033[0m]"; echo ""; exit 1; }
    popd
    ldconfig
    sslibevtag="$(wget -qO- https://api.github.com/repos/shadowsocks/shadowsocks-libev/releases/latest | grep 'tag_name' | cut -d\" -f4)"
    sslibevver="shadowsocks-libev-$(echo ${sslibevtag} | sed -e 's/^[a-zA-Z]//g')"
    wget -t 3 -T 30 -nv -O ${sslibevver}.tar.gz https://github.com/shadowsocks/shadowsocks-libev/releases/download/${sslibevtag}/${sslibevver}.tar.gz
    [ "$?" != "0" ] && { echo ""; echo -e "# [\033[31;1mCannot Download Shadowsocks-libev Source. Aborting!\033[0m]"; echo ""; exit 1; }
    [ -d ${sslibevver} ] && rm -rf $sslibevver
    tar zxf ${sslibevver}.tar.gz
    pushd $sslibevver
    ./configure
    make || { echo ""; echo －e "# [\033[31;1mShadowsocks-libev Failed to Build. Aborting!\033[0m]"; echo ""; exit 1; }
    make install || { echo ""; echo －e "# [\033[31;1mShadowsocks-libev Failed to Build. Aborting!\033[0m]"; echo ""; exit 1; }
    popd
    ldconfig
    [ -d simple-obfs ] && rm -rf simple-obfs
    git clone https://github.com/shadowsocks/simple-obfs.git
    pushd simple-obfs
    git submodule update --init --recursive
    ./autogen.sh
    ./configure
    make || { echo ""; echo －e "# [\033[31;1mSimple-obfs Failed to Build. Aborting!\033[0m]"; echo ""; exit 1; }
    make install || { echo ""; echo －e "# [\033[31;1mSimple-obfs Failed to Build. Aborting!\033[0m]"; echo ""; exit 1; }
    popd
    ldconfig
    rm -rf libsodium-${libsodiumver}.tar.gz libsodium-${libsodiumver} mbedtls-${mbedver}-gpl.tgz mbedtls-${mbedver} ${sslibevver}.tar.gz $sslibevver simple-obfs
}

function configsslibev(){
    date="$(date +%Y-%m-%d-%H:%M:%S)"
    OBFSLOCAL="obfs-host"
    [ -z "$PASSWORD" ] && PASSWORD="$(< /dev/urandom tr -dc 'A-HJ-NPR-Za-km-z2-9' | head -c 32)"
    [ "$FWS" = "enable" ] && OBFSLOCAL="failover"
    [ -d /etc/shadowsocks-libev ] || mkdir -p /etc/shadowsocks-libev
    cat > /etc/shadowsocks-libev/config.json<<EOF
{
    "server":${SSLOCAL},
    "server_port":${PORT},
    "local_address":"${LOACL}",
    "local_port":${LOCALPORT},
    "password":"${PASSWORD}",
    "nameserver":"${DNS}",
    "timeout":${TIMEOUT},
    "udp_timeout":${TIMEOUT},
    "method":"${METHOD}",
    "plugin":"obfs-server",
    "plugin_opts":"obfs=${OBFS};fast-open;${OBFSLOCAL}=${OBFSHOST}",
    "mode":"tcp_and_udp",
    "fast_open":true,
    "workers":${WORKERS},
}
EOF
    if ! grep -qs "Twist" /etc/sysctl.conf; then
        /bin/cp -f /etc/sysctl.conf "/etc/sysctl.conf.old-${date}" 2>/dev/null
        cat >> /etc/sysctl.conf <<EOF
# Twist
fs.file-max = 1024000
kernel.msgmnb = 65536
kernel.msgmax = 65536
kernel.shmall = 4294967296
kernel.shmmax = 68719476736
net.core.rmem_max = 12582912
net.core.wmem_max = 12582912
net.core.default_qdisc = fq
net.ipv4.ip_forward = 1
net.ipv4.tcp_rmem = 10240 87380 12582912
net.ipv4.tcp_wmem = 10240 87380 12582912
net.ipv4.tcp_syncookies = 1
net.ipv4.tcp_tw_reuse = 1
net.ipv4.tcp_tw_recycle = 0
net.ipv4.tcp_fin_timeout = 30
net.ipv4.tcp_keepalive_time = 1200
net.ipv4.tcp_mtu_probing = 1
net.ipv4.tcp_fastopen = 3
net.ipv4.conf.all.accept_source_route = 1
net.ipv4.conf.default.accept_source_route = 1
net.ipv4.conf.all.accept_redirects = 0
net.ipv4.conf.default.accept_redirects = 0
net.ipv4.conf.all.send_redirects = 0
net.ipv4.conf.default.send_redirects = 0
net.ipv4.conf.lo.send_redirects = 0
net.ipv4.conf.${ETH}.send_redirects = 0
net.ipv4.conf.all.rp_filter = 0
net.ipv4.conf.default.rp_filter = 0
net.ipv4.conf.lo.rp_filter = 0
net.ipv4.conf.${ETH}.rp_filter = 0
net.ipv4.icmp_echo_ignore_broadcasts = 1
net.ipv4.icmp_ignore_bogus_error_responses = 1
net.ipv6.conf.all.forwarding = 1
net.ipv6.conf.all.accept_source_route = 1
net.ipv6.conf.default.accept_source_route = 1
net.ipv6.conf.all.accept_redirects = 0
net.ipv6.conf.default.accept_redirects = 0
net.ipv6.conf.all.autoconf = 1
net.ipv6.conf.all.accept_ra = 2
net.ipv6.conf.${ETH}.accept_ra = 2
EOF
        echo "*                soft    nofile           512000" >> /etc/security/limits.conf
        echo "*                hard    nofile          1024000" >> /etc/security/limits.conf
        echo "" >> /etc/security/limits.conf
        if ! grep -qs "pam_limits.so" /etc/pam.d/login; then
            [ "$systemtype" = "0" ] && echo "session    required     pam_limits.so" >> /etc/pam.d/login
        fi
    fi
}

function configiptables(){
    if ! grep -qs "Twist" /etc/sysctl.conf; then
        iptables-save > "/etc/iptables.rules.old-${date}"
        iptables -I INPUT 1 -m conntrack --ctstate INVALID -j DROP
        iptables -I INPUT 2 -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT
        iptables -I INPUT 3 -p udp -m multiport --dports $PORT -j ACCEPT
        iptables -I FORWARD 1 -m conntrack --ctstate INVALID -j DROP
        iptables -I FORWARD 2 -p tcp --tcp-flags SYN,RST SYN -j TCPMSS --clamp-mss-to-pmtu
        iptables -I INPUT -m state --state NEW -m tcp -p tcp --dport $PORT -j ACCEPT
        iptables -I INPUT -m state --state NEW -m udp -p udp --dport $PORT -j ACCEPT
        /bin/cp -f /etc/ip6tables.rules "/etc/ip6tables.rules.old-${date}" 2>/dev/null
        [ -f /etc/iptables/rules.v6 ] || cat > /etc/ip6tables.rules <<EOF
*filter
:INPUT ACCEPT [0:0]
:FORWARD DROP [0:0]
:OUTPUT ACCEPT [0:0]
-A INPUT -i lo -j ACCEPT
-A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
-A INPUT -m rt --rt-type 0 -j DROP
-A INPUT -s fe80::/10 -j ACCEPT
-A INPUT -p ipv6-icmp -j ACCEPT
-A INPUT -j DROP
COMMIT
EOF
        [ -f /etc/iptables/rules.v6 ] && /bin/cp -f /etc/iptables/rules.v6 "/etc/iptables/rules.v6.old-${date}"
        [ -f /etc/iptables/rules.v6 ] && /bin/cp -f /etc/ip6tables.rules /etc/iptables/rules.v6  
        if [ "$systemtype" = "0" ]; then
            systemctl start firewalld
            firewall-cmd --permanent --zone=public --add-port=${PORT}/tcp
            firewall-cmd --permanent --zone=public --add-port=${PORT}/udp
            firewall-cmd --reload
            cat > /etc/network/if-pre-up.d/iptablesload <<EOF
#!/bin/sh

iptables-restore < /etc/iptables.rules
exit 0
EOF
        else
            cat > /etc/network/if-pre-up.d/iptablesload <<EOF
#!/bin/sh

iptables-restore < /etc/iptables.rules
exit 0
EOF
            cat > /etc/network/if-pre-up.d/ip6tablesload <<EOF
#!/bin/sh

ip6tables-restore < /etc/ip6tables.rules
exit 0
EOF
        fi
        [ ! -f /etc/fail2ban/jail.local ] && echo "" > /etc/fail2ban/jail.local
        [ "$ABB" = "enable" ] && cat >> /etc/fail2ban/jail.local <<EOF

[ssh-iptables]
enabled = true
filter  = sshd
action  = iptables[name=SSH, port=ssh, protocol=tcp]
logpath = /var/log/auth.log

[ssh-ddos]
enabled = true
filter  = sshd-ddos
action  = iptables[name=ssh-ddos, port=ssh,sftp protocol=tcp,udp]
logpath = /var/log/messages

[osx-ssh-ipfw]
enabled = true
filter  = sshd
action  = osx-ipfw
logpath = /var/log/auth.log

[ssh-apf]
enabled = true
filter  = sshd
action  = apf[name=SSH]
logpath = /var/log/auth.log

[osx-ssh-afctl]
enabled = true
filter  = sshd
action  = osx-afctl
logpath = /var/log/auth.log

[selinux-ssh]
enabled = true
filter  = selinux-ssh
action  = iptables[name=SELINUX-SSH, port=ssh, protocol=tcp]
logpath = /var/log/audit/audit.log

[apache-tcpwrapper]
enabled = true
filter  = apache-auth
action  = hostsdeny
logpath = /var/log/httpd/error_log

[apache-badbots]
enabled = true
filter  = apache-badbots
action  = iptables-multiport[name=BadBots, port="http,https"]
logpath = /var/log/httpd/access_log

[apache-shorewall]
enabled = true
filter  = apache-noscript
action  = shorewall
logpath = /var/log/httpd/error_log
EOF
    fi
}

function startservices(){
    if [ -f /usr/local/bin/ss-server ]; then
        ssserverpath="/usr/local/bin/ss-server"
    elif [ -f /usr/bin/ss-server ]; then
        ssserverpath="/usr/bin/ss-server"
    elif [ ! -z "$(which ss-server)" ]; then
        ssserverpath="ss-server"
    else
        echo ""
        echo －e "# [\033[31;1mCannot Find Shadowsocks-libev Install Path. Aborting!\033[0m]"
        echo ""
        exit 1 
    fi
    [ -d /etc/init.d/shadowsocks ] && rm -rf /etc/init.d/shadowsocks
    echo "#!/bin/bash" > /etc/init.d/shadowsocks
    if [  "$systemtype" = "0" ]; then
        cat >> /etc/init.d/shadowsocks <<EOF
# chkconfig: 2345 90 10
# description: Start, Stop or Restart Shadowsocks-libev Server
EOF
    fi
    cat >> /etc/init.d/shadowsocks <<EOF

### BEGIN INIT INFO
# Provides:          Shadowsocks
# Required-Start:    \$network \$local_fs $remote_fs
# Required-Stop:     \$network \$local_fs $remote_fs
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Shadowsocks-libev
# Description:       Start, Stop or Restart Shadowsocks-libev Server
### END INIT INFO

sysctl -q -p
rngd -r /dev/urandom
exitstatus=0

if [ ! -d /var/run ]; then
    mkdir -p /var/run
    if [ \$? -ne 0 ]; then
        echo -e "# \033[31;1mStarting Shadowsocks-libev Failed...\033[0m"
        exit 1
    fi
fi

if [ ! -f /etc/shadowsocks-libev/config.json ]; then
    echo -e "# \033[31;1mStarting Shadowsocks-libev Failed...\033[0m"
    exit 1
fi

sslibev_running() {
    if [ -r /var/run/shadowsocks-libev.pid ]; then
        read PID < /var/run/shadowsocks-libev.pid
        if [ -d "/proc/\${PID}" ]; then
            return 0
        else
            rm -f /var/run/shadowsocks-libev.pid
            return 1
        fi
    else
        return 2
    fi
}

sslibev_status() {
    sslibev_running
    case \$? in
        0)
        echo -e "# \033[32;1mShadowsocks-libev is Running...\033[0m"
        ;;
        1|2)
        echo -e "# \033[34;1mShadowsocks-libev is Stopped...\033[0m"
        exitstatus=1
        ;;
    esac
}

sslibev_start() {
    if sslibev_running; then
        echo -e "# \033[32;1mShadowsocks-libev is Running...\033[0m"
        return 0
    fi
    ${ssserverpath} -u -c /etc/shadowsocks-libev/config.json -f /var/run/shadowsocks-libev.pid
    if sslibev_running; then
        echo -e "# \033[32;1mStarting Shadowsocks-libev Success...\033[0m"
    else
        echo -e "# \033[31;1mStarting Shadowsocks-libev Failed...\033[0m"
        exitstatus=1
    fi
}

sslibev_stop() {
    if sslibev_running; then
        kill -9 \$PID
        rm -f /var/run/shadowsocks-libev.pid
        echo -e "# \033[32;1mStopping Shadowsocks-libev Success...\033[0m"
    else
        echo -e "# \033[34;1mShadowsocks-libev is Stopped...\033[0m"
        exitstatus=1
    fi
}

sslibev_restart() {
    sslibev_stop
    sslibev_start
}

case "\$1" in
    start|stop|restart|status)
    sslibev_\${1}
    ;;
    *)
    echo "Usage: \$0 { start | stop | restart | status }"
    exitstatus=1
    ;;
esac

exit \$exitstatus

EOF
    sysctl -p
    chmod +x /etc/init.d/shadowsocks
    chmod +x /etc/network/if-pre-up.d/iptablesload
    chmod +x /etc/network/if-pre-up.d/ip6tablesload
    if [ "$systemtype" = "1" ]; then
        update-rc.d -f shadowsocks defaults
        ip6tables-restore < /etc/ip6tables.rules
        systemctl enable fail2ban
    else
        chkconfig --add shadowsocks
        chkconfig shadowsocks on
        iptables-restore < /etc/sysconfig/iptables
        systemctl --now mask firewalld
        systemctl enable iptables fail2ban
    fi
    ldconfig
    rngd -r /dev/urandom
    [ "$FWS" = "enable" ] && { a2enmod ssl; systemctl restart apache2; }
    service fail2ban restart
    /etc/init.d/shadowsocks start
}

function twiststatus(){
    clear
    twist
    echo -e "                            [\033[32;1mInstall Complete\033[0m]"
    echo -e "          [\033[32;1mPlease Press Enter to Show Login Infomation and EXIT\033[0m]"
    echo -e "########################################################################"
    read -p ""
    echo "ss://$(echo -n "${METHOD}:${PASSWORD}@${PUBLICIP}:${PORT}" | base64 -w 0)" | qr
    echo -e "# [\033[32;1mss://\033[0m\033[34;1m$(echo -n "${METHOD}:${PASSWORD}@${PUBLICIP}:${PORT}" | base64 -w 0)\033[0m]"
    echo -e "# [\033[32;1mServer IP:\033[0m \033[34;1m${PUBLICIP}\033[0m\c"
    [ ! "$AddrV6" = "false" ] && echo -e "(\033[34;1m${PUBLICIPv6}\033[0m)\c"
    echo -e " \033[32;1mPassWord:\033[0m \033[34;1m${PASSWORD}\033[0m \033[32;1mEncryption:\033[0m \033[34;1m${METHOD}\033[0m \033[32;1mOBFS:\033[0m \033[34;1m${OBFS}\033[0m \033[32;1mOBFS-HOST:\033[0m \033[34;1m${OBFSHOST}\033[0m \033[32;1mLOCALHOST:\033[0m \033[34;1m${LOACL}:${LOCALPORT}\033[0m]"
    if [ "$serverrestart" = "true" ]; then
        echo -e "# [\033[34;1mThe Server Requires Restart to Enable Google BBR, Please Press Enter to Reboot!\033[0m]"
        read -p ""
        sleep 3
        reboot
    fi
}

action=$1
[ -z $1 ] && action=install
case "$action" in
    install|update|uninstall)
        ${action}_twist
        ;;
    *)
        echo "Usage: $0 { install | update | uninstall }"
        ;;
esac
