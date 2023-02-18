#!/bin/bash
#<<<----------colour substitution by variables---------->>>
B0="$(printf '\033[100m')" S0="$(printf '\033[30m')"
B1="$(printf '\033[101m')" S1="$(printf '\033[31m')"
B2="$(printf '\033[102m')" S2="$(printf '\033[32m')"
B3="$(printf '\033[103m')" S3="$(printf '\033[33m')"
B4="$(printf '\033[104m')" S4="$(printf '\033[34m')"
B5="$(printf '\033[105m')" S5="$(printf '\033[35m')"
B6="$(printf '\033[106m')" S6="$(printf '\033[36m')"
B7="$(printf '\033[107m')" S7="$(printf '\033[37m')"
R1="$(printf '\033[0;1m')" R0="$(printf '\033[00m')"
#<<<----------BANNER--------->>>
echo
wait() {
sleep 0.02
}
printf "${S7}╔═══╦╗        ╔╗╔═╦╗${R0}\n"; wait
printf "${S6}║╔═╗║║        ║║║╔╣║${R0}\n"; wait
printf "${S2}║║ ╚╣║╔══╦╗╔╦═╝╠╝╚╣║╔══╦═╦══╗${R0}\n"; wait
printf "${S2}║║ ╔╣║║╔╗║║║║╔╗╠╗╔╣║║╔╗║╔╣║═╣${R0}\n"; wait
printf "${S3}║╚═╝║╚╣╚╝║╚╝║╚╝║║║║╚╣╔╗║║║║═╣${Rp}\n"; wait
printf "${S1}╚═══╩═╩══╩══╩══╝╚╝╚═╩╝╚╩╝╚══╝${R0}${B5}${S2} INSTALLER ${R0}${R1}\n"; wait
echo; wait
printf "${S1}Authored by:- Suman Kumar ~BHUTUU${R0}\n"; wait
echo
sleep 3
#<<----Downloader function---->>#
WGET() {
  while true; do
    wget $1
    if [ "$?" == '0' ]; then
      break
    else
      printf "\n${S2}Try using sudo if using linux | Run in administrative mode in windows | Or check your networkss${R0}\n\n"
    fi
  done
}
#<<<<<--------WINDOWS------>>>>>
_win64_() {
  cd /usr/bin
  WGET 	"https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-windows-amd64.exe"
  mv cloudflared-windows-amd64.exe cloudflared
}
_win32_() {
  WGET "https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-windows-386.exe"
  mv cloudflared-windows-386.exe cloudflared
}
#<<<<<--------LINUX-------->>>>>
#<<----aarch64---->>
__aarch64__() {
 cd $HOME
 WGET "https://github.com/cloudflare/cloudflared/releases/download/2021.10.3/cloudflared-linux-arm64"
 mv cloudflared-linux-arm64 cloudflared
 chmod +x cloudflared
 }
#<<----aarch32----->>
__aarch32__() {
 cd $HOME
 WGET "https://github.com/cloudflare/cloudflared/releases/download/2021.10.3/cloudflared-linux-arm"
 mv cloudflared-linux-arm cloudflared
 chmod +x cloudflared
}
#<<----32bit---->>
__32bit__() {
 cd $HOME
 WGET "https://github.com/cloudflare/cloudflared/releases/download/2021.10.3/cloudflared-linux-386"
 mv cloudflared-linux-386 cloudflared
 chmod +x cloudflared
}
#<<----amd64---->>
__amd64__() {
 cd $HOME
 WGET "https://github.com/cloudflare/cloudflared/releases/download/2021.10.3/cloudflared-linux-amd64"
 mv cloudflared-linux-amd64 cloudflared
 chmod +x cloudflared
}
#####################################<<INSTALLATION>>##########################################
OS=$(uname -o)
archit=$(uname -m)
#<<<----------ANDROID---------->>>
if [[ ${OS^^} == *'ANDROID'* ]]; then
  apt update && apt upgrade -y
  apt install git wget curl -y
  apt install findutils -y
  apt install proot -y
  apt install unzip -y
  sleep 2
  cd $HOME
  distro=$(pwd)
  rm -rf *ngrok*
#<<<-----TERMUX----->>>
  if [[ ${distro} == *'com.termux'* ]]; then
    if [[ -f "$PREFIX/bin/cloudflared" ]]; then
      rm -rf $PREFIX/bin/cloudflared
    else
      :
    fi
    echo; wait
    printf "${S2}YOU ARE USING ${S7}     ╔════╗${R0}\n"; wait
    printf "                   ${S3}║╔╗╔╗║${R0}\n"; wait
    printf "                   ${S3}╚╝║║╠╩═╦═╦╗╔╦╗╔╦╗╔╗${R0}\n"; wait
    printf "                   ${S2}  ║║║║═╣╔╣╚╝║║║╠╬╬╝${R0}\n"; wait
    printf "                   ${S6}  ║║║║═╣║║║║║╚╝╠╬╬╗${R0}\n"; wait
    printf "                   ${S1}  ╚╝╚══╩╝╚╩╩╩══╩╝╚╝ !! :)${R0}\n"; wait
    echo; wait
    printf "${S3}DOWNLOADING CLOUDFLARE....${R0}\n"; wait
    echo
    if [[ ${archit^^} == *'AARCH64'* || ${archit^^} == *'ARMV8'* ]]; then
      __aarch64__
    elif [[ ${archit^^} == *'AARCH32'* || ${archit^^} == *'ARMV7'* ]]; then
      __aarch32__
    elif [[ ${archit^^} == *'386'* || ${archit^^} == 'X86' || ${archit^^} == *'686'* || ${archit^^} == *'X86_32'* || ${archit^^} == 'AMD' ]]; then
      __32bit__
    elif [[ ${archit^^} == *'X86_64'* || ${archit^^} == *'AMD64'* ]]; then
      __amd64__
    else
      echo
      printf "${S5}THIS INSTALLER IS NOT FOR YOUR SYSTEM! PLESAE INSTALL ${B3}cloudflare${R1} MANUALLY!!${R0}\n"
      echo
      exit 1
    fi
    printf "${S6}INSTALLING CLOUDFLARE IN YOUR SYSTEM!! :)${R0}\n"
    echo
    mv -v ${HOME}/cloudflared $PREFIX/bin
    echo
    printf "${S4}${B1}cloudflare${R1} IS INSTALLED IN YOUR SYSTEM ~SUCESSFULLY!! :)${R0}\n"
    echo
#<<</-----TERMUX----->>>

#<<<-----PWN-TERM------>>>
  elif [[ ${distro} == *'hilled.pwnterm'* ]]; then
    if [[ -f "$PREFIX/bin/cloudflared" ]]; then
      rm -rf $PREFIX/bin/cloudflared
    else
     :
    fi
  echo; wait
  printf "${S2}YOU ARE USING ${S7}     ╭━━━┳╮╭╮╭┳━╮╱╭╮╱╭━━━━┳━━━┳━━━┳━╮╭━╮${R0}\n"; wait
  printf "                   ${S3}┃╭━╮┃┃┃┃┃┃┃╰╮┃┃╱┃╭╮╭╮┃╭━━┫╭━╮┃┃╰╯┃┃${R0}\n"; wait
  printf "                   ${S3}┃╰━╯┃┃┃┃┃┃╭╮╰╯┃╱╰╯┃┃╰┫╰━━┫╰━╯┃╭╮╭╮┃${R0}\n"; wait
  printf "                   ${S2}┃╭━━┫╰╯╰╯┃┃╰╮┃┣━━╮┃┃╱┃╭━━┫╭╮╭┫┃┃┃┃┃${R0}\n"; wait
  printf "                   ${S6}┃┃╱╱╰╮╭╮╭┫┃╱┃┃┣━━╯┃┃╱┃╰━━┫┃┃╰┫┃┃┃┃┃${R0}\n"; wait
  printf "                   ${S1}╰╯╱╱╱╰╯╰╯╰╯╱╰━╯╱╱╱╰╯╱╰━━━┻╯╰━┻╯╰╯╰╯!! :)${R0}\n"; wait
    echo; wait
    printf "${S3}DOWNLOADING CLOUDFLARED....${R0}\n"; wait
    echo
    if [[ ${archit^^} == *'AARCH64'* || ${archit^^} == *'ARMV8'* ]]; then
      __aarch64__
    elif [[ ${archit^^} == *'AARCH32'* || ${archit^^} == *'ARMV7'* ]]; then
      __aarch32__
    elif [[ ${archit^^} == *'386'* || ${archit^^} == 'X86' || ${archit^^} == *'686'* || ${archit^^} == *'X86_32'* || ${archit^^} == 'AMD' ]]; then
      __32bit__
    elif [[ ${archit^^} == *'X86_64'* || ${archit^^} == *'AMD64'* ]]; then
      cd $HOME
      __amd64__
    else
      echo
      printf "${S5}THIS INSTALLER IS NOT FOR YOUR SYSTEM! PLESAE INSTALL ${B3}cloudflare${R1} MANUALLY!!${R0}\n"
      echo
      exit 1
    fi
    printf "${S6}INSTALLING CLOUDFLARE IN YOUR SYSTEM!! :)${R0}\n"
    echo
    mv -v ${HOME}/cloudflared $PREFIX/bin
    echo
    printf "${S4}${B1}CLOUDFLARE${R1} IS INSTALLED IN YOUR SYSTEM ~SUCESSFULLY!! :)${R0}\n"
#<<</-----PWN-TERM----->>>
  fi
#<<</----------ANDROID---------->>>

elif [[ ${OS^^} == *'LINUX'* ]]; then
  sudo apt update && apt upgrade -y
  sudo apt install git wget curl -y
  sudo apt install findutils -y
  sudo apt install unzip -y
  sleep 2
  apt update && apt upgrade -y
  apt install git wget curl -y
  apt install findutils -y
  apt install unzip -y
  sleep 2
  cd $HOME
  rm -rf *cloudflare*
  sbingrok=$(sudo find /usr/bin/cloudflared)
  if [[ ${sbingrok} == '/usr/bin/cloudflared' ]]; then
    sudo rm -rf ${sbingrok}
  else
    :
  fi
  bingrok=$(find /usr/bin/cloudflared)
  if [[ ${bingrok} == '/usr/bin/cloudflared' ]]; then
    rm -rf ${bingrok}
  else
    :
  fi
    echo; wait
    echo; wait
    printf "${S2}YOU ARE USING      ${S7}██╗░░░░░██╗███╗░░██╗██╗░░░██╗██╗░░██╗${R0}\n"; wait
    printf "                   ${S3}██║░░░░░██║████╗░██║██║░░░██║╚██╗██╔╝${R0}\n"; wait
    printf "                   ${S3}██║░░░░░██║██╔██╗██║██║░░░██║░╚███╔╝░${R0}\n"; wait
    printf "                   ${S2}██║░░░░░██║██║╚████║██║░░░██║░██╔██╗░${R0}\n"; wait
    printf "                   ${S6}███████╗██║██║░╚███║╚██████╔╝██╔╝╚██╗${R0}\n"; wait
    printf "                   ${S1}╚══════╝╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝!! :)${R0}\n"; wait
    printf "                                ${B5}${S2} ${OS} ${R0}${R1}\n"; wait
    echo; wait
    printf "${S3}DOWNLOADING CLOUDFLARE....${R0}\n"
    echo
    if [[ ${archit^^} == *'AARCH64'* || ${archit^^} == *'ARMV8'* ]]; then #BY THE WAY THIS IS NOT USED IN COMPUTERSS! SO IT IS JUST WASTE ONLY IN THIS SECTION!!
      __aarch64__
    elif [[ ${archit^^} == *'AARCH32'* || ${archit^^} == *'ARMV7'* ]]; then #ALSO THIS IS NOT USED IN COMPUTERSS! SO IT'S ALSO A WASTE IN THIS SECTION!!
      __aarch32__
    elif [[ ${archit^^} == *'386'* || ${archit^^} == 'X86' || ${archit^^} == *'686'* || ${archit^^} == *'X86_32'* || ${archit^^} == 'AMD' ]]; then #THIS IS FOR RECOGNOSING 32-BIT COMPUTERSS
      __32bit__
    elif [[ ${archit^^} == *'X86_64'* || ${archit^^} == *'AMD64'* ]]; then #THIS IS FOR RECOGNOSING 64_BIT COMPUTERSS
      __amd64__
    else
      echo
      printf "${S5}THIS INSTALLER IS NOT FOR YOUR SYSTEM! PLESAE INSTALL ${B3}cloudflare${R1} MANUALLY!!${R0}\n"
      echo
      exit 1
    fi
    printf "${S6}INSTALLING NGROK IN YOUR SYSTEM!! :)${R0}\n"
    echo
    sudo mv -v ${HOME}/cloudflared /usr/bin > /dev/null 2>&1
    mv -v ${HOME}/cloudflared /usr/bin > /dev/null 2>&1
    echo
    printf "${S4}${B1}CLOUDFLARE${R1} IS INSTALLED IN YOUR SYSTEM ~SUCESSFULLY!! :)${R0}\n"
elif [[ ${OS^^} == *'MSYS'* || ${OS^^} == *'WINDOWS'* ]]; then
  echo; wait
  echo; wait
  echo -e "${S2}YOU ARE USING: ${R0}\n"; wait
  printf "${S7}██████          ██████ ██████████ ██████          ██████ ████████████   ██████████████ ██████          ██████ ██████████████ ${R0}\n"; wait
  printf "${S7}██░░██          ██░░██ ██░░░░░░██ ██░░██████████  ██░░██ ██░░░░░░░░████ ██░░░░░░░░░░██ ██░░██          ██░░██ ██░░░░░░░░░░██ ${R0}\n"; wait
  printf "${S3}██░░██          ██░░██ ████░░████ ██░░░░░░░░░░██  ██░░██ ██░░████░░░░██ ██░░██████░░██ ██░░██          ██░░██ ██░░██████████ ${R0}\n"; wait
  printf "${S3}██░░██          ██░░██   ██░░██   ██░░██████░░██  ██░░██ ██░░██  ██░░██ ██░░██  ██░░██ ██░░██          ██░░██ ██░░██         ${R0}\n"; wait
  printf "${S3}██░░██  ██████  ██░░██   ██░░██   ██░░██  ██░░██  ██░░██ ██░░██  ██░░██ ██░░██  ██░░██ ██░░██  ██████  ██░░██ ██░░██████████ ${R0}\n"; wait
  printf "${S2}██░░██  ██░░██  ██░░██   ██░░██   ██░░██  ██░░██  ██░░██ ██░░██  ██░░██ ██░░██  ██░░██ ██░░██  ██░░██  ██░░██ ██░░░░░░░░░░██ ${R0}\n"; wait
  printf "${S2}██░░██  ██░░██  ██░░██   ██░░██   ██░░██  ██░░██  ██░░██ ██░░██  ██░░██ ██░░██  ██░░██ ██░░██  ██░░██  ██░░██ ██████████░░██ ${R0}\n"; wait
  printf "${S2}██░░██████░░██████░░██   ██░░██   ██░░██  ██░░██████░░██ ██░░██  ██░░██ ██░░██  ██░░██ ██░░██████░░██████░░██         ██░░██ ${R0}\n"; wait
  printf "${S6}██░░░░░░░░░░░░░░░░░░██ ████░░████ ██░░██  ██░░░░░░░░░░██ ██░░████░░░░██ ██░░██████░░██ ██░░░░░░░░░░░░░░░░░░██ ██████████░░██ ${R0}\n"; wait
  printf "${S6}██░░██████░░██████░░██ ██░░░░░░██ ██░░██  ██████████░░██ ██░░░░░░░░████ ██░░░░░░░░░░██ ██░░██████░░██████░░██ ██░░░░░░░░░░██ ${R0}\n"; wait
  printf "${S1}██████  ██████  ██████ ██████████ ██████          ██████ ████████████   ██████████████ ██████  ██████  ██████ ██████████████${R0}\n\n";wait

  printf "${S3}DOWNLOADING CLOUDFLARE....${R0}\n"
  if [[ ${archit^^} == *'X86_64'* || ${archit^^} == *'AMD64'* ]]; then
    _win64_
    mv -v cloudflared /usr/bin
    printf "\n${S4}${B1}cloudflare${R1} IS INSTALLED IN YOUR SYSTEM ~SUCESSFULLY!! :)${R0}\n"
  elif [[ ${archit^^} == *'386'* || ${archit^^} == 'X86' || ${archit^^} == *'686'* || ${archit^^} == *'X86_32'* || ${archit^^} == 'AMD' ]]; then
    _win32_
    mv -v cloudflared /usr/bin
    printf "\n${S4}${B1}cloudflare${R1} IS INSTALLED IN YOUR SYSTEM ~SUCESSFULLY!! :)${R0}\n"
  else
    printf "${S2}[${S1}!${S2}]${S1} SORRY!! BUT THIS INSTALLER IS NOT FOR YOUR SYSTEM SO INSTALL CLOUDFLARE MANNUALY!!!${R0}\n"
  fi
else
  printf "${S2}[${S1}!${S2}]${S1} SORRY!! BUT THIS INSTALLER IS NOT FOR YOUR SYSTEM SO INSTALL CLOUDFLARE MANNUALY!!!${R0}\n"
fi