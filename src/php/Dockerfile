FROM php:8.3.9-apache

RUN apt-get update && apt-get install -y \
    zip unzip git zip

RUN a2enmod rewrite
RUN docker-php-ext-install mysqli

COPY --from=composer:latest /usr/bin/composer /usr/bin/composer
WORKDIR /var/www/html

COPY index.php /var/www/html/
COPY metrics.php /var/www/html/
COPY .htaccess /var/www/html/

RUN composer require promphp/prometheus_client_php
EXPOSE 80

CMD ["apache2-foreground"]
