# Manifest to install flask from pip3
  package {'python3-pip':
    ensure => latest,
  }

  package {'Werkzueg':
    ensure          => '2.1.1',
    provider        => 'pip3',
    install_options => ['--executable', '/usr/bin/python3 -m pip'],
    require         => Package['python3-pip'],
  }

  package {'flask':
    ensure   => '2.1.0', # ensures the package v2.1.0 is installed
    provider => 'pip3', # sets the provider to pip3 (optional)
    require  => Package['python3-pip'],
  }
