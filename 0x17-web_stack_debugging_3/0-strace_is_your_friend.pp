# debug the apache2
exec { 'restart':
command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php; service apache2 restart'
path    => ['/bin', '/usr/bin', '/usr/sbin']
}
