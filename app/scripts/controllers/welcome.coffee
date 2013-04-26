define ['app'], (App) ->

  App.controller 'WelcomeController', ($scope, $location, $rootScope, StepsService, percentCompletion, appLoading) ->
    StepsService.all()

    $rootScope.$on 'onStepsLoaded', (evt, steps) ->
      $scope.steps = steps
      $scope.percentCompleted = percentCompletion.calculateStepsCompletion($scope.steps)

    # Class methods
    $scope.start = ->
      $location.url '/steps/1/'

    $scope.resume = ->
      step = StepsService.getFirstIncomplete $scope.steps
      $location.url "/steps/#{step.number}/"

    $scope.finish = ->
      $location.url '/finished'
