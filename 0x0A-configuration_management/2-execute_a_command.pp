# Manifest to execute a command to kill a process named killmenow
  exec {'pkill killmenow':
    provider => 'shell',  # enviroment to execute command
  }
