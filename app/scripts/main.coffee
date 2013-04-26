require
  paths:
    'jquery': '../components/jquery/jquery'
    'underscore': '../components/underscore/underscore'
    'angular': '../components/angular/angular'
    'angular-bootstrap': '../components/angular-bootstrap/ui-bootstrap'
    'angular-cookies': '../components/angular-cookies/angular-cookies'
    'angular-resource': '../components/angular-resource/angular-resource'
  shim:
    'underscore':
      exports: '_'
    'angular':
      exports: 'angular'
    'angular-bootstrap': ['angular']
    'angular-cookies': ['angular']
    'angular-resource': ['angular']
  [
    # Third party stuff
    'require'
    'angular'

    # Our App
    'app'

    # Controllers
    'controllers/app'
    'controllers/badge'
    'controllers/finish'
    'controllers/fun_facts'
    'controllers/level'
    'controllers/login'
    'controllers/progressbar'
    'controllers/step'
    'controllers/steps_nav'
    'controllers/welcome'

    # Services
    'services/badges'
    'services/profile'
    'services/steps'

    # Factories
    'factories/apploading'
    'factories/cache'
    'factories/calculate_completion'

    # Routes
    'routes'

    # Things to run immediately
    'run'

  ], (require, angular) ->
    angular.bootstrap document, ['app']
