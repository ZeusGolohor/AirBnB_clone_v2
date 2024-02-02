#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static.
config_file="/etc/nginx/sites-available/default"
sudo apt-get -y update
sudo apt-get -y install nginx
sudo service nginx start
sudo chown -R "$USER":"$USER" /var/www/html
sudo chmod -R 755 /var/www
sudo rm /var/www/html/index.nginx-debian.html
echo 'Hello World!' | sudo tee /var/www/html/index.nginx-debian.html > /dev/null
# created the needed dir.
dirc="/data/"
if [ ! -d "$dirc" ]; then
    sudo mkdir "$dirc"
    echo "making $dirc"
fi
dirc="/data/web_static/"
if [ ! -d "$dirc" ]; then
    sudo mkdir "$dirc"
fi
dirc="/data/web_static/releases/"
if [ ! -d "$dirc" ]; then
    sudo mkdir "$dirc"
fi
dirc="/data/web_static/shared/"
if [ ! -d "$dirc" ]; then
    sudo mkdir "$dirc"
fi
dirc="/data/web_static/releases/test/"
if [ ! -d "$dirc" ]; then
    sudo mkdir "$dirc"
fi
# creating the index file
echo "<html>
<head>
</head>
<body>
Holberton School
</body>
</html>" | sudo tee /data/web_static/releases/test/index.html
# creating sym link
ne="/data/web_static/current"
te="/data/web_static/releases/test/"
# delete the link if it already lives in the folder
if [ -L "$ne" ]; then
    sudo rm "$ne"
fi
sudo ln -sf "$te" "$ne"
sudo chown -R ubuntu:ubuntu /data/
# Check if the location block already exists
if ! grep -q "location /hbnb_static" "$config_file"; then
    new_string=$(cat <<-EOL
        server_name _;
        location /hbnb_static {
            alias /data/web_static/current/;
            index index.html index.htm;
        }
EOL
    )
    # Use awk to replace the "server_name _;" line with the new configuration block
    awk -v new_string="$new_string" '/server_name _;/ { print new_string; next }1' "$config_file" > "$config_file.tmp"
    # Replace the original configuration file with the temporary file
    sudo mv "$config_file.tmp" "$config_file"
fi
sudo service nginx restart
