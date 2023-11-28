# installs flask from pip3
exec { 'install':
  ensure   => '2.1.0',
  provider => 'pip3',
  command  => 'pip3 install Flask',
}
