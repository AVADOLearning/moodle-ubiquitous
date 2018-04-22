base:
  '*':
    - base

  'roles:app-.+':
    - match: grain_pcre
    - app
    - nginx
    - php-fpm

  'roles:app-moodle':
    - match: grain

  'platform-group:1':
    - match: grain
    - platforms-moodle-1
    - platforms-moodle-1-logos

  'platform-group:2':
    - match: grain
    - platforms-moodle-2
    - platforms-moodle-2-logos

  'roles:app-saml':
    - match: grain
    - platforms-saml-logos
  'G@roles:app-saml and G@saml-platforms:identity-provider':
    - match: compound
    - platforms-saml-identity-provider
  'G@roles:app-saml and G@saml-platforms:identity-proxy':
    - match: compound
    - platforms-saml-identity-proxy

  'roles:db-pgsql':
    - match: grain
    - db-pgsql
    - platforms-moodle-1
    - platforms-moodle-2

  'roles:gocd-agent':
    - match: grain
    - gocd

  'roles:gocd-server':
    - match: grain
    - gocd
    - nginx

  'roles:named':
    - match: grain
    - named

  'roles:selenium-.+':
    - match: grain_pcre
    - selenium

  'roles:redis':
    - match: grain
    - redis

  'roles:redis-sentinel':
    - match: grain
    - redis-sentinel
