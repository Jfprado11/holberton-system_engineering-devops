# debug the apache2
exec { 'restart':
path    => ['/bin', '/usr/bin', '/usr/sbin']
command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php; service apache2 restart'
}
