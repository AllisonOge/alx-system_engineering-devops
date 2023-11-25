# Manifest to create a file sets its permission, owner, group and content
  file {'/tmp/school':
    ensure  => present,  # ensure the file exists
    mode    => '0744',
    owner   => 'www-data',
    group   => 'www-data',
    content => 'I love Puppet', # sets the content of the file
  }
