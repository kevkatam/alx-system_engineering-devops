# Change the OS configuration so that it is possible to login with the
# holberton user and open a file without any error message

exec {'replace':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 5/nofile 5000/" /etc/security/limits.conf',
  before   => Exec['replace1'],
}

exec {'replace1':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 4/nofile 4000/" /etc/security/limits.conf',
}
