# Update and Upgrade all packages:

# sudo apt update
# sudo apt full-upgrade
# sudo apt install raspberrypi-kernel-headers
# sudo reboot

# Installing basic dependencies:
echo "Installing basic dependencies:"
sudo apt install python3
curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
sudo apt-get install -y nodejs

# Verifying nodejs info:
echo ""
echo "Verifying nodejs info:"
node -v
npm config get prefix

if [[ $(npm config get prefix) == 'usr/local' ]]; then

    mkdir ~/.npm-global
    npm config set prefix '~/.npm-global'
    echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.profile
fi

# Install Edge Impulse Cli
echo ""
echo "Installing Edge Impulse Cli:"
npm install -g edge-impulse-cli

# Install Edge Impulse Linux Platform
echo ""
echo "Installing Edge Impulse Linux Platform:"
sudo apt install -y gcc g++ make build-essential nodejs sox gstreamer1.0-tools gstreamer1.0-plugins-good gstreamer1.0-plugins-base gstreamer1.0-plugins-base-apps
npm config set user root && sudo npm install edge-impulse-linux -g --unsafe-perm

echo ""
echo "Installation Complete: It is reccomended that you reboot your device."

