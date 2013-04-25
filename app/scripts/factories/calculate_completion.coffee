define ['app'], (App) ->

  App.factory 'percentCompletion', ->
    return {
      # Updates completion percentage.
      calculateStepsCompletion: (steps)->
        completed = _.filter steps, (step) -> step.done
        return completed.length / steps.length * 100
    }
