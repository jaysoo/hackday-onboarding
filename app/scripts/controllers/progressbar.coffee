define ['app'], (App) ->

  ProgressBarController = ($scope) ->
      $scope.percentCompleted = 0


  App.controller 'ProgressBarController', ProgressBarController
