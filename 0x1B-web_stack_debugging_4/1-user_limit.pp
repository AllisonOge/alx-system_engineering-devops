# fix OS config for user holberton with soft and hard limit settings
exec { 'increase-soft-limit':
    command => "sed -i 's/^holberton soft nofile.*/holberton soft nofile 8192/' /etc/security/limits.conf",
    path    => '/usr/local/bin/:/bin/',
}

exec { 'increase-hard-limit':
    command => "sed -i 's/^holberton hard nofile.*/holberton hard nofile 8192/' /etc/security/limits.conf",
    path    => '/usr/local/bin/:/bin/',
}
