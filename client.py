import os
import yaml
import githubapimock as api 

config_path = os.path.expanduser("~/repo.yml")
settings = yaml.load(open(config_path))

org = settings["org"]
repo = settings["repo"]
user = settings["user"]
token = settings["token"]

title = ""
while title != "q":
   title = input("Title: ")
   body = input("Body: ")
   label = input("Label: ")
   labels = [label]
   
   issue_id = api.create_issue(org, repo, user, token, title, body)



