define ['app'], (App) ->

  App.controller 'FinishController', ($scope, $location, StepsService) ->
    StepsService.all (steps) ->
      $scope.steps = steps

      if (firstIncomplete = StepsService.getFirstIncomplete(steps))
        $location.url "/steps/#{firstIncomplete.number}"
