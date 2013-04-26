This is the Onboarding frontend for Wave Hack Days

Getting Started
---------------

You will need [NodeJS](http://nodejs.org/) (0.8+) installed on your machine. (`node --version` to check your installed version).

**Note**: If you have Grunt installed previously, you will need to uninstall it first:

    sudo npm uninstall -g grunt

Now, install grunt-cli and bower:

    sudo npm install -g bower grunt-cli@latest

Make sure that you add the npm bin directory to your PATH in `.bashrc`:

    # Sample path if npm installed through Homebrew
    export PATH="/usr/local/share/npm/bin:$PATH"



Installing/Updating dependencies
--------------------------------

These commands will update both NodeJS and client-side dependences. The latter probably changes more often.

Install NodeJS dependencies:

    npm install --dev

Install client-side JavaScript components:

    bower install


Running
-------

You can start the server using the `grunt --force` command.

Todo page: [http://localhost:9001/app/](http://localhost:9001/app/)

The browser will refresh whenever a file is changed (HTML, LESS, CoffeeScript). :)


Releasing
---------

Using grunt:

    grunt release

This will create a dist folder that can be `scp`ed to whereever you want.
