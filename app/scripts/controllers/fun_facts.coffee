define ['app'], (App) ->

  App.controller 'FunFactsController', ($scope, $rootScope, $http) ->
    timer = null

    randomPerson = ->
      len = $scope.people.length
      index = parseInt(Math.random() * len, 10)
      $rootScope.person = $scope.people[index]
      $rootScope.$apply() unless $rootScope.$$phase

    $scope.start = ->
      randomPerson()
      timer = setInterval randomPerson, 6000

    $scope.stop = ->
      clearInterval timer
    
    # Fetch all the people!
    $http.get('data/people.json')
      .then(
        # Success
        (resp) ->
          $scope.people = resp.data
          $scope.start()
      ,
        # Error
        ->
      )


