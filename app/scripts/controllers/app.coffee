define ['app'], (App) ->

  App.controller 'AppController', ($scope, $rootScope, $location, $cookies, $http, appLoading, AppCache) ->
    $rootScope.topScope = $rootScope
    $rootScope.$on '$routeChangeStart', -> appLoading.loading()
    $rootScope.$on '$routeChangeSuccess', -> appLoading.ready()

    $scope.logout = ->
      # Remove all objects currently cached in browser.
      AppCache.removeAll()

      # Log user out.
      $rootScope.loggedUser = $cookies.loggedUser = undefined

      $http.post('/api/logout')
        .then(->
          # Refresh browser to clear everything out.
          window.location.reload()
        )

