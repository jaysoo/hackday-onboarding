define ['app'], (App) ->

  App.controller 'FunFactsController', ($scope, $rootScope, $http) ->
    timer = null

    randomPerson = ->
      len = $scope.people.length
      index = parseInt(Math.random() * len, 10)
      $scope.person = $scope.people[index]

    $scope.start = ->
      randomPerson()
      timer = setInterval randomPerson, 10000

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


