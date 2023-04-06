#!/usr/bin/env bash
# Set up my web servers for the deployment of `web_static`

# Install Nginx (if it's not already installed)
# sudo apt-get -y update
# sudo apt-get -y install nginx

# Create necessary folders and files
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
touch /data/web_static/releases/test/index.html

# Populate `index.html`
echo "Hello. Welcome to my page" > /data/web_static/releases/test/index.html

# Create a symbolic link. If the link already exists,
# it should be deleted and recreated
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Change ownership `/data/` directory to `ubuntu` user and group
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content of
# /data/web_static/current/ to hbnb_static
# (ex: https://mydomainname.tech/hbnb_static)
repl_str="error_page 404 \/error.html;\n\n\tlocation \/hbnb_static\/ {\n\t\talias \/data\/web_static\/current\/;\n\t}"
sudo sed -i "s/error_page 404 \/error.html;/$repl_str/" /etc/nginx/sites-available/default

sudo service nginx restart
