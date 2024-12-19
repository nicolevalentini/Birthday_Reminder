To set up your script so that a window pops up on your desktop to notify you of birthdays, you can automate it using a combination of a plist (for macOS LaunchAgents) and a shell script to run the Python script. 

Guide:

Step 1: Create a Shell Script - You need a shell script that will execute your Python script.

1. Create a new file named e.g. “birthday_reminder.sh” (you can place it in your home directory, e.g., /Users/namesurname/).
2. Add the following lines to the file:

Bash

  #!/bin/bash
  /usr/bin/python3 /Users/namesurname/birthday_reminder.py

Replace /Users/namesurname/birthday_reminder.py with the full path to your Python script.

3. Make the script executable by running the following command in your terminal:

 Bash
 chmod +x /Users/namesurname/birthday_reminder.sh


Step 2: Create a LaunchAgent Plist File
A plist file schedules tasks to run at specific times or intervals on macOS. You will set one up for your script.

1. Navigate to the ~/Library/LaunchAgents/ folder (create it if it doesn't exist):

Bash
mkdir -p ~/Library/LaunchAgents

2. Create a new plist file, e.g., com.birthdayreminder.plist, in the ~/Library/LaunchAgents/ folder:

Bash
nano ~/Library/LaunchAgents/com.birthdayreminder.plist

3. Add the following content to the plist file:

Xml
   <?xml version="1.0" encoding="UTF-8"?>
   <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
   <plist version="1.0">
   <dict>
       <key>Label</key>
       <string>com.birthdayreminder</string>
       <key>ProgramArguments</key>
       <array>
           <string>/Users/namesurname/birthday_reminder.sh</string>
       </array>
       <key>StartCalendarInterval</key>
       <dict>
           <key>Hour</key>
           <integer>9</integer>
           <key>Minute</key>
           <integer>0</integer>
       </dict>
       <key>RunAtLoad</key>
       <true/>
       <key>StandardErrorPath</key>
       <string>/tmp/birthday_reminder.err</string>
       <key>StandardOutPath</key>
       <string>/tmp/birthday_reminder.out</string>
   </dict>
   </plist>


-Replace `/Users/namesurname/birthday_reminder.sh` with the full path to your shell script.

- Adjust `<integer>9</integer>` and `<integer>0</integer>` under <key>StartCalendarInterval</key>` to set the time you want the reminder to run (e.g., 9:00 AM).

4. Save and exit by pressing Ctrl+O, Enter, and Ctrl+X.


Step 3: Load the Plist File
To enable the scheduled task:

1. Load the plist file into launchctl:

Bash
   launchctl load ~/Library/LaunchAgents/com.birthdayreminder.plist

2. Verify that it’s loaded:

Bash
launchctl list | grep com.birthdayreminder

Step 4: Test the Setup
To test that everything works:

1. Run the shell script manually to ensure the Python script executes correctly:

Bash
 /Users/namesurname/birthday_reminder.sh
 

2. If you see the popup, your script is working fine.
3. Wait for the scheduled time to confirm that the `plist` file triggers the script as expected.

Debugging
- If the popup doesn't appear at the scheduled time, check the logs in `/tmp/birthday_reminder.err` and `/tmp/birthday_reminder.out` for errors.
- Ensure the paths to the Python script and shell script are correct.
- Use `launchctl unload ~/Library/LaunchAgents/com.birthdayreminder.plist` to unload and reload the plist file if you make changes.
