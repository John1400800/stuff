setxkbmap -layout "us, ru" -option "grp:alt_shift_toggle"
xrdb -merge ~/.Xresources

xsetroot -solid white
while true
do
DATE=$(date +"%a %d %b %R")
BATT_CAPACITY=$(cat /sys/class/power_supply/BAT1/capacity)
xsetroot -name "$DATE $BATT_CAPACITY%"
sleep 1m
done &

exec dwm
