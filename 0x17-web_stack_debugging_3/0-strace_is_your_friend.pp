# debug the apache2
exec { 'restart':
  command   => 'service apache2 restart',
}
file_line {'changing':
  ensure  => 'present',
  path    => '/var/www/html/wp-settings.php',
  replace => true,
  match   => "require_once(ABSPATH . WPINC . '/class-wp-locale.phpp'",
  line    => "require_once(ABSPATH . WPINC . '/class-wp-locale.php'",
}
