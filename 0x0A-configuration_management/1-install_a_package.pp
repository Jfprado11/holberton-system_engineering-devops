# install a lint for puppet
package { 'puppet-lint'
  ensure   => '1.1.0',
  provider => 'gem',
}
