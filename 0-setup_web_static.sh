#!/usr/bin/env bash
#

# Install Nginx if not already installed
if ! command -v nginx &> /dev/null
then
    apt-get update
    apt-get install -y nginx
fi

# Create necessary folders if they don't exist
folders=("/data" "/data/web_static" "/data/web_static/releases" "/data/web_static/shared" "/data/web_static/releases/test")
for folder in "${folders[@]}"
do
    mkdir -p "$folder"
done

# Create a fake HTML file
echo "<html><head></head><body>Hello Holberton</body></html>" > /data/web_static/releases/test/index.html

# Create or recreate symbolic link
rm -rf /data/web_static/current
ln -s /data/web_static/releases/test/ /data/web_static/current

# Set ownership of /data folder to ubuntu user and group recursively
chown -R ubuntu:ubuntu /data

# Update Nginx configuration
config_file="/etc/nginx/sites-available/default"
echo "server {
    location /hbnb_static {
        alias /data/web_static/current/;
        index index.html index.htm;
    }
}" > "$config_file"

# Restart Nginx
service nginx restart

# Exit successfully
exit 0

