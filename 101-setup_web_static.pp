# web_servers.pp

# Install Nginx if not already installed
package { 'nginx':
  ensure => installed,
}

# Create necessary folders if they don't exist
file { ["/data", "/data/web_static", "/data/web_static/releases", "/data/web_static/shared", "/data/web_static/releases/test"]:
  ensure  => 'directory',
  recurse => true,
}

# Create a fake HTML file
file { '/data/web_static/releases/test/index.html':
  ensure  => 'file',
  content => '<html><head></head><body>Hello Holberton</body></html>',
}

# Create or recreate symbolic link
file { '/data/web_static/current':
  ensure  => 'link',
  target  => '/data/web_static/releases/test/',
  force   => true,
  require => File['/data/web_static/releases/test/index.html'],
}

# Set ownership of /data folder to ubuntu user and group recursively
file { '/data':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  recurse => true,
}

# Update Nginx configuration
file { '/etc/nginx/sites-available/default':
  ensure  => 'file',
  content => "server {
    location /hbnb_static {
        alias /data/web_static/current/;
        index index.html index.htm;
    }
}",
  notify => Service['nginx'],
}

# Restart Nginx
service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}
