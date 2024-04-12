/*
Automate the task of creating a custom HTTP header response
with Puppet.

Requirements:
- The name of the custom HTTP header must be X-Served-By
- The value of the custom HTTP header must be the hostname
of the server Nginx is running on
- Write 2-puppet_custom_http_response_header.pp so that it
configures a brand new Ubuntu machine to the requirements
*/

# install and configure Nginx
exec {'apt-update':
    command => 'apt-get update',
    path    => '/usr/bin/',
}

package {'nginx':
    ensure  => installed,
    require => Exec['apt-update'],
}

file_line {'add_header':
    path     => '/etc/nginx/sites-available/default',
    match    => '^server {',
    line     => "server {\n\tadd_header X-Served-By \"${hostname}\";",
    multiple => false,
    notify   => Exec['restart_nginx'],
}

exec {'restart_nginx':
    command => '/usr/bin/service nginx restart',
}
