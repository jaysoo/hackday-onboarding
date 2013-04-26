define ['app'], (App) ->

  class Routes
    constructor: ($routeProvider) ->
      $routeProvider
        .when '/',
          templateUrl: 'views/welcome.html'
          controller: 'WelcomeController'
        .when '/login',
          templateUrl: 'views/login.html'
          controller: 'LoginController'
        .when '/steps/:stepNum',
          templateUrl: 'views/step.html'
          controller: 'StepController'
        .when '/finished',
          templateUrl: 'views/finish.html'
          controller: 'FinishController'
        .otherwise
          redirectTo: '/'


  App.config  Routes
