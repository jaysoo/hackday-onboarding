define ['app'], (App) ->

  class StepsService
    constructor: ($resource, $http, $rootScope, AppCache) ->
      @Step = $resource 'data/steps.json'
      @http = $http
      @cache = AppCache
      @rootScope = $rootScope

    # Gets all steps.
    all: (respond) -> 
      steps = @cache.get 'steps'

      if steps
        respond steps
        @_initStatus(step) for step in steps
      else
        @Step.query (steps) =>
          @cache.put 'steps', steps
          @_initStatus(step) for step in steps
          respond steps

    _initStatus: (step) ->
      # Check if this step can be marked as done (no questions).
      if not step.choices.length and not step.is_text_question
        step.done = true
        @rootScope.$emit 'onStepComplete', step

    verify: (step, respond) =>
      @http.get('data/answer.json').then((resp) =>
        # Mark step as completed and emit event.
        if resp.data.correct
          step.done = true
          @rootScope.$emit 'onStepComplete', step

        respond resp.data
      )


  App.service 'StepsService', StepsService
