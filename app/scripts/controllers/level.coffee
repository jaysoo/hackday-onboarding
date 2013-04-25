define ['app'], (App) ->

  App.controller 'LevelController', ($scope, ProfileService) ->
    ProfileService.getProfile (profile) ->
      $scope.profile = profile
