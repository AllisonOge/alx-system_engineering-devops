# install nginx using puppet
  exec {'apt-update':
    command => 'apt-get update',
    path    => '/usr/bin/',
  }

  package { 'nginx':
    ensure  => installed,
    require => Exec['apt-update'],
  }

  file { '/etc/nginx/sites-available/default':
    ensure  => file,
    content => "server {
      listen 80;
      listen [::]:80 default_server;

      location /redirect_me {
         return 301 https://www.youtube.com/;
      }

      root /var/www/html;
      index index.html index.htm;
      server_name _;

      location / {
         try_files \$uri \$uri/ =404;
      }
   }
  ",
    require => Package['nginx'],
    notify  => Exec['restart_nginx'],
  }

  file { '/var/www/html/index.html':
    ensure  => present,
    content => 'Hello World!',
    require => Package['nginx'],
  }

  exec { 'restart_nginx':
    command     => 'service nginx restart',
    path        => '/usr/sbin/',
    refreshonly => true,
    subscribe   => File['/etc/nginx/sites-available/default'],
    environment => ['PATH=/usr/sbin:/usr/bin:/sbin:/bin'],
  }
