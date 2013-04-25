define ['app', 'underscore'], (App, _) ->

  StepController = ($scope, $location, $routeParams, $rootScope, StepsService) ->

    # Retrieve all steps from the service.
    StepsService.all (steps) ->
      ######################
      # Controller methods #
      ######################
      
      # Navigation for prev/next.
      $scope.prev = -> 
        $location.url "/steps/#{$scope.prevStep.number}"

      $scope.next = -> 
        $location.url "/steps/#{$scope.nextStep.number}"

      $scope.goto = (num) -> 
        $location.url "/steps/#{num}"

      $scope.finish = ->
        $location.url '/finished'
       
      ##################
      # Initialization #
      ##################

      $rootScope.$emit 'onStepsLoaded', steps
      $scope.steps = steps

      # Find the step we're on.
      $scope.step = _.find steps, (step) -> step.number is Number($routeParams.stepNum)

      # Get previous and next steps (if exist).
      if $scope.step.next
        $scope.nextStep = _.find steps, (step) -> step.id is $scope.step.next

      if $scope.step.previous
        $scope.prevStep = _.find steps, (step) -> step.id is $scope.step.previous

      # Check if we've completed the previous step first.
      # If not, then kick back to the first incomplete step.
      if $scope.prevStep and not $scope.prevStep.done
        $scope.goto(StepsService.getFirstIncomplete(steps).number or steps[0].number)


      # This step may already be done, therefore verified.
      $scope.verified = $scope.step.done

      # Global events when user answers a question.
      $rootScope.$on 'onIncorrectResponse', ->
        $scope.incorrect = true

      $rootScope.$on 'onStepComplete', ->
        $scope.incorrect = false

    # Verification for questions.
    $scope.verify = (step) ->
      StepsService.verify step, (response) ->
        $scope.verified = response.correct


  App.controller 'StepController', StepController
