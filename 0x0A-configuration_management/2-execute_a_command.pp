# killin process
exec { 'killmenow':
  command => 'pkill killmenow'
  path    => '/usr/local/bin/:/bin/',
}
