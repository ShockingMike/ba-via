#!/bin/sh
# shot.sh in.html out.png W H [scale]
"/c/Program Files/Google/Chrome/Application/chrome.exe" --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=${5:-1} --window-size=$3,$4 --screenshot="$(cygpath -w "$2")" "file:///$(cygpath -m "$1")" 2>/dev/null
