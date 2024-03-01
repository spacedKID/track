# track

this will eventually:
- listens for keyboard hotkey trigger
- prompts user to categorize and provide input value
- writes input to events table
- exports events table as csv

## DATABASE CONFIGURATION

the application expects an environment variable `TRACK_DATABASE_URI`
this should be written in your .zshrc file (or however you load environment variable)
this should be written as: `export TRACK_DATABASE_URI='postgresql://username:password@localhost/track'`
where you will replace username and password with your own username and password