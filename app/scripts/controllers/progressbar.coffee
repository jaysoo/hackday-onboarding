define ['app'], (App) ->

  ProgressBarController = ($scope, $rootScope, percentCompletion) ->
      $scope.percentCompleted = 0

      $rootScope.$on 'onStepsLoaded', (evt, steps) ->
        $scope.steps = steps
        $scope.percentCompleted = percentCompletion.calculateStepsCompletion steps

        if $scope.percentCompleted is 100
          $scope.isFinished = true

      $rootScope.$on 'onStepComplete', (evt, step) ->
        if $scope.steps
          $scope.percentCompleted = percentCompletion.calculateStepsCompletion $scope.steps

          if $scope.percentCompleted is 100
            $scope.isFinished = true


  App.controller 'ProgressBarController', ProgressBarController
