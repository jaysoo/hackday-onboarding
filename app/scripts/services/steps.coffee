define ['app'], (App) ->

  class StepsService
    constructor: ($resource, $http, AppCache) ->
      @Step = $resource 'data/steps.json'
      @http = $http
      @cache = AppCache

    # Gets all steps.
    all: (respond) -> 
      steps = @cache.get 'steps'

      if steps
        respond steps
      else
        @Step.query (steps) =>
          @cache.put 'steps', steps
          respond steps

    verify: (step, respond) ->
      @http.get('data/answer.json').then((resp) ->
        respond resp.data
      )


  App.service 'StepsService', StepsService
