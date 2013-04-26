define ['app'], (App) ->
  App.run ($rootScope, $location, $cookies) ->
    if (user = $cookies.loggedUser)
      $rootScope.loggedUser = JSON.parse user

    $rootScope.$on '$routeChangeStart', (evt, next, current) ->
      # If we're not logged in AND we're not already going to the login page.
      if not $rootScope.loggedUser and next.$$route.controller isnt 'LoginController'
        $rootScope.redirectUrl = $location.url()
        $location.url  '/login'
