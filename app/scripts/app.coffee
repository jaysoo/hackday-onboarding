define [
    'angular'
    'angular-resource'
    'angular-bootstrap'
  ], (angular) -> 
    return angular.module('app', [
      'ngResource'
      'ui.bootstrap'
    ])
