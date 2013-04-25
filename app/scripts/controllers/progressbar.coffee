define ['app'], (App) ->

  ProgressBarController = ($rootScope) ->
      $rootScope.percentCompleted = 0


  App.controller 'ProgressBarController', ProgressBarController
