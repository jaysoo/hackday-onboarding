define ['app'], (App) ->

  App.factory 'appLoading', ($rootScope) ->
    timer = null

    loading: ->
      clearTimeout timer
      $rootScope.status = 'loading'
      $rootScope.$apply() unless $rootScope.$$phase

    ready: (delay) ->
      ready = ->
        # First view loaded!
        $rootScope.initialized = true

        $rootScope.status = 'ready'
        $rootScope.$apply() unless $rootScope.$$phase
      clearTimeout timer
      delay = (if not delay? then 500 else false)
      if delay
        timer = setTimeout(ready, delay)
      else
        ready()
