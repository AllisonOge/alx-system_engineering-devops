# Manifest to install flask from pip3
  package {'flask':
    ensure   => '2.1.0', # ensures the package v2.1.0 is installed
    provider => 'pip3', # sets the provider to pip3 (optional)
  }
