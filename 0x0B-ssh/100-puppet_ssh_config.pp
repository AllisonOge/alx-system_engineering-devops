# Manifest to custom configure SSH file
  exec { 'Turn off passwd auth':
    command     => '/usr/bin/sed -i "s/^#*PasswordAuthentication.*/PasswordAuthentication no/" /etc/ssh/sshd_config',
    refreshonly => true,
    subscribe   => File['/etc/ssh/sshd_config'],
  }

  exec { 'Declare identity file':
    command     => '/usr/bin/echo "IdentityFile ~/.ssh/school" >> /etc/ssh/sshd_config',
    unless      => '/usr/bin/grep -q "^#*IdentityFile ~/.ssh/school" /etc/ssh/sshd_config',
    refreshonly => true,
    subscribe   => File['/etc/ssh/sshd_config'],
  }

  file { '/etc/ssh/sshd_config':
    ensure => file,
    owner  => 'root',
    group  => 'root',
    mode   => '0644',
  }
