define ['app'], (App) ->

  class Routes
    constructor: ($routeProvider) ->
      $routeProvider
        .when '/',
          templateUrl: 'views/welcome.html'
          controller: 'WelcomeController'
        .when '/steps/:stepNum',
          templateUrl: 'views/step.html'
          controller: 'StepController'
        .otherwise
          redirectTo: '/'   


  App.config  Routes
