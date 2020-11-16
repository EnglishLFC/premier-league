# Ubersicht-Widgets: Premier League Table

Premier League Widget for Ubersicht http://tracesof.net/uebersicht-widgets/

This is based on a widget I found somewhere a long time ago, which stopped working, so I completely re-wrote it. I don't remember where I found the original (not that this contains anything from the original Python code any longer) and I can't find it now. If you come across the old, non-functional one, let me know and I'll credit the original here for giving me the idea.

Anyway, you'll need to visit https://www.footballwebpages.co.uk to sign up for a free account to get an API key. Then open the premier-league.py file in your favorite editor and put your API key in there (where it says **YOUR_API_KEY**).

If you want to color your favorite team, you'll need to change the **MY_TEAM_NAME** variable, and if you want to change the highlight color for your team, look in the index.coffee file for the *mightiest* and *mightyclass* sections.

Then put all this stuff in your local Ubersicht widgets directory. Either git clone the thing or download an archive, it's up to you.

## Requirements

I use Python from Mac Ports, which installs all it's bits and pieces in `/opt/local`, so if you don't use this and your Python is somewhere else, you'll need to change the path to your Python binary at the top of the Python script. Also, you'll need the following Python libraries:

```Python
urllib
json
requests
```

## Screenshot

[![Screenshot](screenshots/screenshot.png)]
