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
      else
        @Step.query (steps) =>
          # Sort by step number in ascending order.
          steps = _.sortBy steps, 'number'

          @cache.put 'steps', steps
          respond steps

    updateStatus: (step) ->
      # Check if this step can be marked as done (no questions).
      if not step.choices.length and not step.is_text_question
        step.done = true
        @rootScope.$emit 'onStepComplete', step

    verify: (step, respond) =>
      @http.get('data/answer.json').then((resp) =>
          # Mark step as completed and emit event.
          if resp.data.correct
            @updateStatus(step)
            step.done = true
            @rootScope.$emit 'onStepComplete', step
          else
            @rootScope.$emit 'onIncorrectResponse', step

          respond resp.data
        )

    # Assume that steps is sorted, which the should be if loaded
    # from this service. Returns `null` if all are done.
    getFirstIncomplete: (steps) ->
      firstIncompleteStep = null  # Defaults to first step.
      for step in steps
        unless step.done
          firstIncompleteStep = step
          break
      return firstIncompleteStep


  App.service 'StepsService', StepsService
