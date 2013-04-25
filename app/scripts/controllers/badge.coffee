define ['app', 'underscore'], (App, _) ->

  App.controller 'BadgeController', ($scope, $location, BadgeService) ->
    BadgeService.all (badges) ->
      $scope.badges = badges
