livereloadSnippet = require('grunt-contrib-livereload/lib/utils').livereloadSnippet
folderMount = (connect, point) -> connect.static(require('path').resolve(point))

projectConfig =
  app: 'app'
  tmp: '.tmp'
  dist: 'dist'
  test: 'test'

module.exports = (grunt) ->
  # Load all grunt tasks
  require('matchdep').filterDev('grunt-*').forEach(grunt.loadNpmTasks)

  # Grunt configuration:
  #
  # https://github.com/cowboy/grunt/blob/master/docs/getting_started.md
  #
  grunt.initConfig
    project: projectConfig

    clean:
      dist: ['<%= project.dist %>']


    # Task configurations
    # -------------------

    # Runs a test server
    connect:
      server:
        options:
          port: 9001
          middleware: (connect, options) -> [livereloadSnippet, folderMount(connect, '.')]


    # Headless testing through PhantomJS
    mocha:
      test:
        src: ['test/index.html']


    # Watch configuration
    watch:
      coffee:
        files: ['<%= project.app %>/scripts/{,*/}*.coffee']
        tasks: ['coffee:dist']
      coffeeTest:
        files: ['<%= project.app %>/test/spec/{,*/}*.coffee']
        tasks: ['coffee:test']
      stylesheets:
        files: ['{,*/}*.less']
        tasks: ['less']
      livereload:
        files: [
          '<%= project.app %>/{,*/}*.html'
          '{.tmp,<%= project.app %>}/scripts/{,*/}*.js'
          '{.tmp,<%= project.app %>}/styles/{,*/}*.css'
          '<%= project.app %>/images/{,*/}*.{png,jpg,jpeg,gif}'
          '<%= project.app %>/data/{,*/}*.json'
        ]
        tasks: ['livereload']

    coffee:
      dist:
        files: [
          expand: true
          cwd: '<%= project.app %>/scripts'
          src: '{,*/}*.coffee'
          dest: '<%= project.app %>/scripts'
          ext: '.js'
        ]
      test:
        files: [
          expand: true
          cwd: '<%= project.test %>/spec'
          src: '{,*/}*.coffee'
          dest: '<%= project.test %>/spec'
          ext: '.js'
        ]

    # JSHint options and globals
    # https://github.com/cowboy/grunt/blob/master/docs/task_lint.md#specifying-jshint-options-and-globals
    jshint:
      options:
        curly: true
        eqeqeq: true
        immed: true
        latedef: true
        newcap: true
        noarg: true
        sub: true
        undef: true
        boss: true
        eqnull: true
        browser: true

      globals:
        jQuery: true

    # RequireJS 2.0 configuration
    # http://requirejs.org/docs/optimization.html#mainConfigFile
    requirejs:

      # Dev version excludes require-cs and require-text plugins. You need to supply these in your
      # own project.
      #
      # Load float through RequireJS:
      #
      #     require(['float'], function (Float) {
      #       var Foo = Float.Facade.mvc.BaseModel.extend({
      #         // ...
      #       });
      #     });
      compile:
        options:
          baseUrl: '<%= project.app %>/scripts'
          mainConfigFile: '<%= project.app %>/scripts/main.js'
          stubModules: ['cs', 'text']
          out: '<%= project.tmp %>/scripts/main.js'
          optimize: 'uglify2'
          preserveLicenseComments: false
          generateSourceMaps: true
          name: 'app'

    less:
      compile:
        options:
          yuicompress: true
        files:
          '<%= project.app %>/styles/main.css': ['<%= project.app %>/styles/main.less']

    copy:
      dist:
        files: [

          # Float.js files
          src: ['<%= project.tmp %>/scripts/{,*/}*']
          dest: '<%= project.dist %>/scripts'
          flatten: true
          expand: true
        ,
          # Fonts and images
          src: ['<% project.app %>/images/{,*/}*']
          expand: true
          dest: '<%= project.dist %>/images'
        ]

  grunt.renameTask 'regarde', 'watch'

  grunt.registerTask 'default', [
      'coffee'
      'less'
      'livereload-start'
      'connect:server'
      'watch'
    ]
  grunt.registerTask 'release', [
      'clean'
      'coffee'
      'less'
      'requirejs'
      'copy'
    ]
  grunt.registerTask 'test', [
      'mocha'
    ]
