import os
from fancyBackup import fancyBackup
from forceOpen import forceOpen

# Get SSID and password from user
usrSSID = input('Enter SSID (WPA-PSK only!): ')
usrPass = input('Enter SSID password: ')

# Enumerate network interfaces file
enumInterfaces='''auto lo

iface lo inet loopback
iface eth0 inet dhcp

allow-hotplug wlan0
iface wlan0 inet manual
wpa-roam /etc/wpa_supplicant/wpa_supplicant.conf
iface default inet dhcp'''

# Enumerate supplicant file with user inputs
print('Creating supplicant file, based on given information...', end='')
enumSupplicant = '''network={
	ssid="%s"
	scan_ssid=1
	psk="%s"
	mode=0
	proto=WPA2
	key_mgmt=WPA-PSK
	pairwise=CCMP
	group=CCMP
	auth_alg=OPEN
	id_str="raspi"
	priority=1
}''' %(usrSSID, usrPass)
print('... Done!')

# Back up existing interfaces file before changing
print('Backing up existing interfaces file...')
fancyBackup('interfaces', '/etc/network')
print('... Done!')

# Back up existing wpa_supplicant file before changing
print('Backing up existing wpa_supplicant file...')
fancyBackup('wpa_supplicant.conf', '/etc/wpa_supplicant/')
print('... Done!')

# Write to interfaces
print('Writing to interfaces...', end='')
w = open('/etc/network/interfaces', 'w')
w.write(enumInterfaces)
print('... Done!')
w.close()
print('Closed file')

# Write to wpa_supplicant
print('Writing to wpa_supplicant...', end='')
w = open('/etc/wpa_supplicant/wpa_supplicant.conf', 'w')
w.write(enumSupplicant)
print('... Done!')
w.close()
print('Closed file')

# Exit message
print('Please sudo reboot')
