#
# Funcrusher Puppet manifest for Vagrant
#   Will automatically install nginx, gunicorn and postgresql
#

class debian-us-mirror {
  file { '/etc/apt/sources.list':
    source => "/vagrant/vagrantfiles/sources.list",
    mode => 0644,
    before => Exec['apt update'],
  }
}

class debian-backports {
  file { '/etc/apt/sources.list.d/debian-backports.list':
    source => "/vagrant/vagrantfiles/debian-backports.list",
    mode => 0644,
    before => Exec['apt update'],
  }
}

class debian-apt-upgrade {
  exec { 'apt update':
    command => '/usr/bin/aptitude update',
  }
  exec {'apt upgrade':
    require => Exec['apt update'],
    command => '/usr/bin/aptitude upgrade -y',
  }
}

class nginx-backports {
  package { "nginx-light":
    require => Exec['apt upgrade'],
    ensure => installed,
  }
  service { "nginx":
    require => Package['nginx-light'],
    ensure => running,
  }
}

class gunicorn-backports {
  file { "/etc/apt/preferences.d/00-gunicorn.pref":
    source => "/vagrant/vagrantfiles/gunicorn.pref",
    before => Package['gunicorn'],
  }
  package { "gunicorn":
    require => Exec['apt upgrade'],
    ensure => installed,
  }
  service { "gunicorn":
    require => Package['gunicorn'],
    ensure => running,
  }
}

class mercurial {
  package { "mercurial":
    require => Exec['apt upgrade'],
    ensure => installed,
  }
}

class python-pip {
  package { "python-pip":
    require => Exec['apt upgrade'],
    ensure => installed,
  }
}

include debian-us-mirror
include debian-backports
include debian-apt-upgrade
include nginx-backports
include gunicorn-backports
include mercurial
include python-pip

# Remove default nginx configuration
file { '/etc/nginx/sites-enabled/default':
  require => Package['nginx-light'],
  ensure => absent,
  notify => Service['nginx'],
}

# Add funcrusher nginx configuration
file { '/etc/nginx/sites-enabled/100_funcrusher':
  require => Package['nginx-light'],
  source => "/vagrant/vagrantfiles/nginx.conf",
  notify => Service['nginx'],
}

# Add funcrusher gunicorn configuration
file { '/etc/gunicorn.d/100_funcrusher':
  require => Package['gunicorn'],
  source => "/vagrant/vagrantfiles/gunicorn-debian.py",
  notify => Service['gunicorn'],
}

# Install environment for funcrusher
exec { 'virtualenv':
  require => Package['python-pip'],
  command => '/usr/bin/pip install -b /tmp/funcrusher/build --src=/tmp/funcrusher/src --install-option="--prefix=/tmp/funcrusher" -r /vagrant/REQUIREMENTS',
}
