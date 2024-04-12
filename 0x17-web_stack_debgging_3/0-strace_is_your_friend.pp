# fix typo error in /var/www/html/wp-settings.php
exec {'fix-typo':
    command => '/usr/bin/sed -i s/phpp/php/g /var/www/html/wp-settings.php',
}
