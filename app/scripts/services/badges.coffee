define ['app'], (App) ->

  class BadgeService
    constructor: ($resource, $http, $rootScope, AppCache) ->
      @Badge = $resource 'data/badges.json'
      @cache = AppCache
      @rootScope = $rootScope

    all: (respond) ->
      badges = @cache.get 'badges'

      if badges
        respond badges
      else
        @Badge.query (badges) =>
          @cache.put 'badges', badges
          respond badges

    # Gets a badge by its ID.
    get: (id, respond) ->
      @all (badges) ->
        badge = _.find badges, (badge) -> badge.id is id
        respond  badge


  App.service 'BadgeService', BadgeService
