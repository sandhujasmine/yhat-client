import os
import shutil
import json


PROJECT_DIR = os.path.join(os.environ['HOME'], ".yhat/templates")

def setup(template_name, project_name):
    if template_name=='*new project*':
        return setup_new_project()
    elif template_name=="*download project*":
        return find_template(project_name)
	replacements = {
		"project_name": project_name
	}
	config_filepath = os.path.join(PROJECT_DIR, template_name + '.json')
	config = json.load(open(config_filepath))
	if os.path.isdir(project_name):
		shutil.rmtree(project_name)
	os.mkdir(project_name)
	for dirname in config.get("dirs", []):
		path = os.path.join(project_name, dirname)
		if os.path.isdir(path)==False:
			os.mkdir(path)
	for newfile in config.get("files", []):
		filename = os.path.join(project_name, newfile['name'])
		with open(filename, "w") as f:
			f.write(newfile['content'] % replacements)

def setup_new_project():
	pass

def find_template(query):
    ALL_TEMPLATES = [
        {"name": "something"}
    ]
    for template in ALL_TEMPLATES:
        if re.find(query, json.dumps(template)):
            yield template
