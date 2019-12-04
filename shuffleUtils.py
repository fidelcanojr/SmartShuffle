import csv
import sys

FLAG_TRACK_FILE='flaggedTracks.csv'

def get_flagged_tracks():
    forbidden_fruit = set()
    current_to_next_map = {}
    with open(FLAG_TRACK_FILE, 'r') as file:
        flagreader = csv.reader(file)
        for line in flagreader:
            current_to_next_map[line[0]]=line[1]
            forbidden_fruit.add(line[1])
    return (forbidden_fruit, current_to_next_map)

def is_flagged(track_id):
    reader = csv.reader(open(FLAG_TRACK_FILE))
    for row in reader:
        if row[0] == track_id:
            return True
    return False

def add(prev, next):
    if not is_flagged(prev):
        with open(FLAG_TRACK_FILE, 'a') as file:
            flagwriter = csv.writer(file)
            flagwriter.writerow([prev, next])

if __name__ == '__main__':
    try:
        previous_track = sys.argv[1]
        next_track = sys.argv[2]
        add(previous_track, next_track)
    except IndexError:
        print("Please provide tracks to flag. Usage: ")
        print("python3 shuffleUtils.py <PREV_TRACK_ID> <NEXT_TRACK_ID>")
