#!/usr/bin/env python3
import re
import json
import requests
import subprocess


def main():
    git_diff = subprocess.check_output(["git", "diff", "--cached"]).decode("utf-8")

    git_status = subprocess.check_output(["git", "status"]).decode("utf-8")

    changed_lines = [
        line.strip() for line in git_diff.split("\n") if line.startswith("+")
    ]

    if not changed_lines:
        print("No changes staged for commit.")
        return

    commit_message = "\n".join(changed_lines)

    template = f"<s>[INST] You are a software developer currently working on a project. \
        You have made several changes to the codebase and are now ready to commit your work to a Git repository. \
        The changes you've made can be seen in the output of the git `diff --cached command`, which displays \
        the differences between the staged changes and the previous commit. Write a concise, informative, and \
        well-structured one-line commit message that accurately summarizes the changes you are about to push to \
        the repository based on the following `git diff --cached` output: ```{git_diff}``` and this is the \
        `git status` result: ```{git_status}```[/INST]</s>"

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
