define ['app', 'underscore'], (App, _) ->

  StepController = ($scope, $location, $routeParams, $rootScope, StepsService) ->

    # Retrieve all steps from the service.
    StepsService.all (steps) ->
      $scope.steps = steps
      $scope.step = _.find steps, (step) -> step.number is Number($routeParams.stepNum)

      # Check if this step can be marked as done (no questions).
      if not $scope.step.choices.length and not $scope.step.question
        $scope.step.done = true

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
        $scope.recalculatePercentageCompleted()

      # Updates completion percentage.
      $scope.recalculatePercentageCompleted = ->
        completed = _.filter $scope.steps, (step) -> step.done
        $rootScope.percentCompleted = completed.length / $scope.steps.length * 100

      $scope.recalculatePercentageCompleted()

    # Verification for questions.
    $scope.verify = (step) ->
      StepsService.verify step, (response) ->
        $scope.step.done = $scope.verified = response.correct


  App.controller 'StepController', StepController
