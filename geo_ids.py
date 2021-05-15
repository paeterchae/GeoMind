import os
import json

BASE_PATH = ""

count = 0
ids = open("tweet_ids.txt","a")
for f in os.listdir(BASE_PATH + "GeoCoV19/raw/"):
    if f[-5:] == ".json":
        for line in open("GeoCoV19/raw/" + f, "r"):
            tweet = json.loads(line)
            try:
                if tweet["geo_source"] == "coordinates" and tweet["geo"]["country_code"] == "us":
                    ids.write(tweet["tweet_id"] + "\n")
                    count += 1
            except Exception as e:
                print(e)
                continue
        print(f + " complete")

print("total tweet count: " + str(count))