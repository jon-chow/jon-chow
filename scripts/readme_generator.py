import sys
import json
from colored import Fore, Style

content_json_file_path = "./content.json"
base_readme_file_path = "./README.base.md"
write_readme_file_path = "../README.md"

replace_string = "PYTHON_TECHNOLOGY_STACK" # search and replace this string in README.base.md
readme_string = "" # Generated markdown string

# Helper functions
def read_file(file_path):
  with open(file_path, "r", encoding="utf8") as file:
    return file.read()

def write_file(file_path, file_content):
  with open(file_path, "w", encoding="utf8") as file:
    file.write(file_content)

def build_markdown_item(item, iconSize, iconSource):
  return f"""
<a href="{item["url"]}" title="{item["name"]}" target="_blank" rel="noreferrer">
  <img src="{iconSource}{item["icon"]}" height="{iconSize}" />
  {item["name"]}
</a>"""

# Main functions
def generate_readme_string():
  global readme_string
  content = json.loads(read_file(content_json_file_path))
  iconSize = content["iconSize"]
  iconSource = content["iconSource"]
  technologies = content["technologies"]
  for technology in technologies:
    if technology != technologies[0]:
      readme_string += "\n"
    readme_string += f"### `{technology['title']}`"
    for item in technology["items"]:
      readme_string += build_markdown_item(item, iconSize, iconSource)
      if item != technology["items"][-1]:
        readme_string += "<br />"
    readme_string += "\n"

# Main
def main(args):
  global write_readme_file_path
  write_readme_file_path = args[1:][0] if len(args[1:]) > 0 else "../README.md"
  print(f"{Fore.rgb(0, 200, 255)}Generating README file...")
  generate_readme_string()
  readme = read_file(base_readme_file_path)
  readme = readme.replace(replace_string, readme_string)
  write_file(write_readme_file_path, readme)
  print(f"{Fore.rgb(0, 255, 0)}README file generated!{Style.reset}")

if __name__ == "__main__":
  main(sys.argv)