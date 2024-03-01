# track

this will eventually:
- listens for keyboard hotkey trigger
- prompts user to categorize and provide input value
- writes input to events table
- exports events table as csv

## INSTALLATION

an install.sh script is included at the root level
- run this installatino script
- a new plist will be created `track.plist`
- this plist functions as the launch agent, ensuring that the keyboard listener is running

## DATABASE CONFIGURATION

the application expects an environment variable `TRACK_DATABASE_URI`
- this should be written in your .zshrc file (or however you load environment variable)
- this should be written as: `export TRACK_DATABASE_URI='postgresql://username:password@localhost/track'`
- where you will replace username and password with your own username and password

