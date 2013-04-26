define ['app'], (App) ->

  class StepsService
    constructor: ($resource, $http, $rootScope, AppCache, BadgeService) ->
      @Step = $resource '/api/tasks/'
      @http = $http
      @cache = AppCache
      @rootScope = $rootScope
      @BadgeService = BadgeService

    # Gets all steps.
    all: (respond) ->
      steps = @cache.get 'steps'

      if steps
        @updateBadgeStatus(step) for step in steps
        @rootScope.$broadcast 'onStepsLoaded', steps
        @initStuff(steps)
        respond?(steps)
      else
        @Step.query (steps) =>
          # Sort by step number in ascending order.
          steps = _.sortBy steps, 'number'

          @cache.put 'steps', steps
          @updateBadgeStatus(step) for step in steps
          @initStuff(steps)
          @rootScope.$broadcast 'onStepsLoaded', steps
          respond?(steps)

    get: (id, respond) ->
      @all (steps) ->
        step = _.find steps, (step) -> step.id is id
        respond step

    markDone: (step) =>
      # Check if this step can be marked as done (no questions).
      step.done = true
      step.incorrect = false
      @rootScope.$broadcast 'onStepComplete', step
      @updateBadgeStatus step

    verify: (step, respond) =>
      @markDone(step) if step.type is 'task'

      @http.get('data/answer.json').then((resp) =>
          # Mark step as completed and emit event.
          if resp.data.correct
            @markDone(step)
          else
            step.incorrect = true

          respond?(resp.data)
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

    updateBadgeStatus: (step) =>
      # Unlocking badges
      if step.done and (badgeId = step.badge)
        @BadgeService.get badgeId, (badge) =>
          badge.unlocked = true
          @rootScope.$emit 'onBadgeUnlock', badge

    # Sets up the proper prev/next chain.
    # Sets up the proper type.
    initStuff: (steps) =>
      prev = null
      next = null
      for step in steps
        if step.choices?.length
          step.type = 'multiple_choice'
        else if step.open_ended
          step.type = 'text'
        else
          step.type = 'task'

        step.prev = prev?.number
        prev?.next = step.number
        prev = step

      console.log steps


  App.service 'StepsService', StepsService
