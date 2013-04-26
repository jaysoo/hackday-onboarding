define [
    'angular'
    'angular-bootstrap'
    'angular-cookies'
    'angular-resource'
  ], (angular) ->
    return angular.module('app', [
      'ngCookies'
      'ngResource'
      'ui.bootstrap'
    ])
