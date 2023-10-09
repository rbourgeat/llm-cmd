#!/usr/bin/env python3
import os
import sys
import json
import requests


def main():
    template = ""
    file_content = ""
    arg_file_path = ""

    if os.path.isfile("README.md"):
        with open("README.md", "r") as readme_file:
            readme_content = readme_file.read()
        print("README.md exists. Rewriting the README.md...")
    else:
        print(
            "README.md does not exist in the current directory. Creating README.md from scratch..."
        )

    if len(sys.argv) > 1:
        arg_file_path = sys.argv[1]

        try:
            with open(arg_file_path, "r") as file:
                file_content = file.read()
        except FileNotFoundError:
            print(f"File not found: {arg_file_path}")
    else:
        print(
            "No command-line arguments provided. Please provide a file path as an argument."
        )
        return

    if file_content:
        template = f"<s>[INST] You are a developer who is working \
            on a project and wants to write a readme.md file. \
            Write a detailed readme for the `{arg_file_path}` file, this is the content file: \
            ```{file_content}```[/INST]</s>"

    url = "http://localhost:8080/completion"
    headers = {"Content-Type": "application/json"}
    data = {"prompt": template, "n_predict": -1}

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        response_data = json.loads(response.text)

        if response_data["content"] == "":
            main()
            return

        with open("README.md", "a") as file:
            file.write(response_data["content"])

        print(f"Documentation of {arg_file_path} added to README.md")
    else:
        print(f"Error: Request failed with status code {response.status_code}")
        print(response.text)


if __name__ == "__main__":
    main()
