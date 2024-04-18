# increase the file descriptor limit in /etc/default/nginx
exec {'increase-file-descriptor-limit':
    command => "sed -i 's/^ULIMIT=.*/ULIMIT=\"-n 10000\"/Ig' /etc/default/nginx",
    path    => '/usr/local/bin/:/bin/',
}

exec { 'restart-nginx':
    command     => '/usr/bin/service nginx restart',
    refreshonly => true,
    subscribe   => Exec['increase-file-descriptor-limit'],
    path        => '/usr/sbin:/usr/bin:/sbin/bin',
}
