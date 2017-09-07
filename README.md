# scrape-atl-code-camp

I wanted to take the sessions from [Atlanta Code Camp](https://atlantacodecamp.com/2017/Schedule) and prioritize them in some notes.  Instead of doing the boring thing (spending 5 minutes to write down some notes), I decided to do the technical thing (scrape the website in python and dump it to json -- and somewhere else I'll probably write a small webapp to allow me to order them, favorite/star, and save: or I'll run out of time and end up spending the 5 minutes taking down notes).

What's interesting so far is the unicode characters people threw in (which blew up the initial version of my hacked-together-json-printing code) -- one of which is not visible.  I think I'll definitely go to that session out of principle :)

I also initially screwed up when string quotes were in the string (since I'm just printing it, it produced invalid JSON).

Another thing that was annoying was the lack of an obvious class to use on the time slots' markup.  It took a little tinkering with the css selectors to find the right bootstrap class to identify the divs and headers and such that I wanted.

## Python Version

Tested in Python 2.7.6

## Usage

```shell
python scrape_to_json.py > data.json
```

## TODO
* Populate a dict and use a JSON library instead of the hacky thing you've done
* After that, try putting the unicode back to unicode instead of replacing it with ?s
