# Manifest to install flask from pip3
  package {'Werkzeug':
    ensure   => '2.1.1',
    provider => 'pip3',
    before   => Package['Flask'], # ensure Werkzeug is installed before Flask
  }

  package {'Flask':
    ensure   => '2.1.0', # ensures the package v2.1.0 is installed
    provider => 'pip3', # sets the provider to pip3 (optional)
    require  => Package['Werkzeug'],
  }
