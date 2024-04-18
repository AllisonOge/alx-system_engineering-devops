# increase the file descriptor limit in /etc/default/nginx
exec {'increase-file-descriptor-limit':
    command => "sed -i 's/ULIMIT=\"-n 15\"/ULIMIT=\"-n 10000\"/Ig' /etc/default/nginx",
    onlyif  => "grep -q 'ULIMIT=\"-n 15\"' /etc/default/nginx",
    path    => '/usr/local/bin/:/bin/',
}

exec { 'restart-nginx':
    command     => '/usr/bin/service nginx restart',
    refreshonly => true,
    subscribe   => Exec['increase-file-descriptor-limit'],
    path        => '/usr/sbin:/usr/bin:/sbin/bin',
}
