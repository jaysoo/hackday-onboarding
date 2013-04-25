require
  paths:
    'jquery': '../components/jquery/jquery'
    'underscore': '../components/underscore/underscore'
    'angular': '../vendor/angular'
    'angular-resource': '../components/angular-resource/angular-resource'
    'angular-bootstrap': '../components/angular-bootstrap/ui-bootstrap'
  shim:
    'underscore':
      exports: '_'
    'angular':
      exports: 'angular'
    'angular-resource': ['angular']
    'angular-bootstrap': ['angular']
  [
    # Third party stuff
    'require'
    'angular'

    # Our App
    'app'

    # Controllers
    'controllers/welcome'
    'controllers/progressbar'
    'controllers/step'
    'controllers/finish'

    # Services
    'services/steps'

    # Factories
    'factories/cache'
    'factories/calculate_completion'

    # Routes
    'routes'
  ], (require, angular) ->
    angular.bootstrap document, ['app']
