import json
import pandas as pd
import time
import base64
import requests
from github import Github
from pprint import pprint



# url to request
url = f"https://api.github.com/users/{username}"
# make the request and return the json
user_data = requests.get(url).json()
# pretty print JSON data
pprint(user_data)


# Github username
username = "YOUR_USERNAME"
# pygithub object
g = Github()
# get that user by username
org = g.get_organization("eHealthAfrica")

def get_repos(artifact):
    repos = []
    counter = 1
    for repo in artifact:
        obj = {}
        obj['name'] = repo.full_name
        obj['description'] = repo.description
        obj['date_created'] = str(repo.created_at)
        obj['last_push'] = str(repo.pushed_at)
        obj['language'] = repo.language
        obj['fork_count'] = repo.forks
        obj['private'] = repo.private
        obj['archived'] = repo.archived
        obj['url'] = repo.html_url
        obj['forks_url'] = repo.forks_url
        repos.append(obj)
        print(counter)
        counter += 1
        time.sleep(1)
    return repos


def write_to_json(filename, my_arr):

    with open(filename, 'w') as outfile:
        json.dump(my_arr, outfile)


def get_members(artifact):

    members = []
    counter = 1

    for member in artifact:
        obj = {}
        obj['username'] = member.login
        obj['url'] = member.html_url
        members.append(obj)
        print(obj)
        print(counter)
        counter += 1
        time.sleep(1)

    return members


# Convert JSON to CSV
def jsont_to_csv(input,output):
    df = pd.read_json(input)
    df.to_csv(output)
    print('Conversion completed!')


# repos = get_repos(org.get_repos())
# write_to_json('./repositories.json', repos)
# jsont_to_csv('./repositories.json', './repositories.csv')

members = get_members(org.get_members())
write_to_json('./members.json', members)
jsont_to_csv('./members.json', './members.csv')
