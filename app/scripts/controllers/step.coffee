define ['app', 'underscore'], (App, _) ->

  StepController = ($scope, $location, $routeParams, $rootScope, StepsService) ->

    # Retrieve all steps from the service.
    StepsService.all (steps) ->
      $rootScope.$emit 'onStepsLoaded', steps
      $scope.steps = steps
      $scope.step = _.find steps, (step) -> step.number is Number($routeParams.stepNum)

      # This step may already be done, therefore verified.
      $scope.verified = $scope.step.done

      # Get previous and next steps (if exist).
      if $scope.step.next
        $scope.nextStep = _.find steps, (step) -> step.id is $scope.step.next
      if $scope.step.previous
        $scope.prevStep = _.find steps, (step) -> step.id is $scope.step.previous

      # Navigation for prev/next.
      $scope.prev = -> 
        $location.url '/steps/' + $scope.prevStep.number

      $scope.next = -> 
        $location.url '/steps/' + $scope.nextStep.number

    # Verification for questions.
    $scope.verify = (step) ->
      StepsService.verify step, (response) ->
        $scope.verified = response.correct


  App.controller 'StepController', StepController
