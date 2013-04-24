define ['app'], (App) ->

  App.controller 'WelcomeController', ($scope, $location) ->
    $scope.start = -> $location.url '/steps/1/'
