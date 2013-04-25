define ['app'], (App) ->

  class ProfileService
    constructor: ($resource, $http, $rootScope, AppCache) ->
      @Profile = $resource 'data/profile.json'
      @cache = AppCache
      @rootScope = $rootScope

    getProfile: (respond) -> 
      profile = @cache.get 'profile'

      if profile
        respond profile
      else
        @Profile.get (profile) =>
          @cache.put 'profile', profile
          respond profile


  App.service 'ProfileService', ProfileService
