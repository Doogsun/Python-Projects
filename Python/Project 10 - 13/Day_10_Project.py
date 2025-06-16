"""Use sys variables to analyze itunes API search values
https://itunes.apple.com/search
https://publicapis.io/i-tunes-search-api
https://music.apple.com/

'Day_10_Project.py'
"""

import sys
import json
import requests

def prompting():
    if len(sys.argv) >= 2:
        prompt = int(input("How many songs would you like to find the name of?:" ))
        return prompt
    if len(sys.argv) == 1:
        print("lololol! I didn't tell you this was sys program blub \n\n(I know because I wrote it! Write 'Gooby Zooby Gloop' into the terminal after the run stuff!) \n\n#TerminalWork")
        sys.exit()


def itunes_search(amount_songs):
    song = "drake"
    output_data = requests.get(f"https://itunes.apple.com/search?entity=song&limit={amount_songs}&term=" + song)
    names_list = output_data.json()
    for name in names_list["results"]:
        print(name["trackName"])

def main():
    numsongs = prompting()
    itunes_search(numsongs)


if __name__ == "__main__":
    main()
