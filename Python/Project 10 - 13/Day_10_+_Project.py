#First time using an api! 
#imma recode this after 15-21

#https://itunes.apple.com/search
#https://publicapis.io/i-tunes-search-api
#https://music.apple.com/

#'Day_10_+_Project.py'




import sys
import json
import requests




def artist_prompting():
    if len(sys.argv) >= 2:
        artist = str(input("What artist would you like to search names for? \nPlease enter intunes search bar name!!!: "))
        return artist

    if len(sys.argv) == 1:
        print("lololol! I didn't tell you this was sys program blub \n\n(I know because I wrote it! Write 'Gooby Zooby Gloop' into the terminal after the run stuff!) \n\n#TerminalWork")
        sys.exit()


def line_prompting():
    while True:
        lines = input("How many song names would you like?: ")
        if lines.isdigit():
            return lines
            break

        else:
            print("Please type a number")


def itunes_search(lines, artist):

    output_data = requests.get(f"https://itunes.apple.com/search?entity=song&limit={lines}&term=" + f"{artist}")
    names_list = output_data.json()                 #enter artist name after = sign, but imma recode this
    for name in names_list["results"]:
        print(name["trackName"])


def main():
    artist_data = artist_prompting()
    num_lines = line_prompting()
    itunes_search(num_lines, artist_data)


if __name__ == "__main__":
    main()

