define ['app'], (App) ->

  App.controller 'WelcomeController', ($scope, $location, $rootScope, StepsService, percentCompletion) ->
    StepsService.all()

    $rootScope.$on 'onStepsLoaded', (evt, steps) ->
      $scope.steps = steps
      $scope.percentCompleted = percentCompletion.calculateStepsCompletion($scope.steps) is 100

    # Class methods
    $scope.start = ->
      $location.url '/steps/1/'

    $scope.resume = ->
      step = StepsService.getFirstIncomplete $scope.steps
      $location.url "/steps/#{step.number}/"
