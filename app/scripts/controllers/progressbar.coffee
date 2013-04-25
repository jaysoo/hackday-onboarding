define ['app'], (App) ->

  ProgressBarController = ($scope, $rootScope, percentCompletion) ->
      $scope.percentCompleted = 0

      $rootScope.$on 'onStepsLoaded', (evt, steps) ->
        $scope.steps = steps
        $scope.percentCompleted = percentCompletion.calculateStepsCompletion $scope.steps

      $rootScope.$on 'onStepComplete', ->
        if $scope.steps
          $scope.percentCompleted = percentCompletion.calculateStepsCompletion $scope.steps


  App.controller 'ProgressBarController', ProgressBarController
