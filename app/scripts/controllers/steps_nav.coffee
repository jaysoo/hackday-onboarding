define ['app', 'underscore'], (App, _) ->

  StepsNavController = ($scope, $rootScope, $location, StepsService) ->
    StepsService.all (steps) ->
      $scope.steps = steps

      # Only unlock the done steps, and the one after.
      firstIncomplete = StepsService.getFirstIncomplete steps
      subsequentSteps = _.filter steps, (step) -> step.number > firstIncomplete.number

      _.each subsequentSteps, (step) ->
        step.locked = true

    $scope.goto = (step) ->
      $location.url "/steps/#{step.number}" unless step.locked

    $rootScope.$on 'onStepComplete', (evt, step) ->
      StepsService.get step.next, (nextStep) ->
        nextStep?.locked = false

  App.controller 'StepsNavController', StepsNavController
