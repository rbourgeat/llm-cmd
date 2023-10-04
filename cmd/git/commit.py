#!/usr/bin/env python3
import re
import json
import requests
import subprocess


def main():
    git_diff = subprocess.check_output(["git", "diff", "--cached"]).decode("utf-8")

    changed_lines = [
        line.strip() for line in git_diff.split("\n") if line.startswith("+")
    ]

    if not changed_lines:
        print("No changes staged for commit.")
        return

    commit_message = "\n".join(changed_lines)

    template = f"<s>[INST] You are a developer who is working \
        on a project and wants to push his work to a git repository. \
        Write a one-line commit message, this is the `git diff --cached` command result: \
        ```{git_diff}```[/INST]</s>"
    
    url = "http://localhost:8080/completion"
    headers = {"Content-Type": "application/json"}
    data = {"prompt": template, "n_predict": 150}

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        response_data = json.loads(response.text)

        if response_data["content"] == "":
            main()
            return

        commit_message = response_data["content"].replace("\n", "")
        commit_message = commit_message.replace("<s>", "")
        commit_message = commit_message.replace("</s>", "")
        commit_message = commit_message.replace("<br>", "")
        commit_message = commit_message.replace('"', "")
        commit_message = commit_message.replace("`", "")

        subprocess.call(["git", "commit", "-m", commit_message])

        print(f'git commit -m "{commit_message}"')

    else:
        print(f"Error: Request failed with status code {response.status_code}")
        print(response.text)


if __name__ == "__main__":
    main()
