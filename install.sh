#!/bin/zsh

# Define paths and names
APP_NAME="track"
APP_LAUNCH_AGENT="/Library/LaunchAgents/$APP_NAME.plist"
APP_SCRIPT="~/Repos/git/track/src/keyboard_listener.py"

# Create a Launch Agent for the application
cat << EOF > $APP_LAUNCH_AGENT
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>$APP_NAME</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/bin/python3</string>
        <string>$APP_SCRIPT</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
</dict>
</plist>
EOF

# Load and start the Launch Agent
launchctl load $APP_LAUNCH_AGENT
launchctl start $APP_NAME

echo "Application setup completed."
