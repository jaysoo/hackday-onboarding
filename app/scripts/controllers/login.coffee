define ['app'], (App) ->

  LoginController = ($scope, $dialog, $rootScope, $http, $location, $cookies) ->
    # Try to login.
    $scope.login = (email) ->
      $http.get('data/login.json', {email: email})
      # $http.post('/api/login', {email: email})
        .then(
          # Success
          (resp) ->
            # Set in global scope and cookie.
            $cookies.loggedUser = JSON.stringify resp.data.user
            $rootScope.loggedUser = resp.data.user
            $rootScope.$apply() unless $rootScope.$$phase

            next = $rootScope.redirectUrl or '/'
            $location.url next
        ,
          # Error
          ->
        )


  App.controller 'LoginController', LoginController

