#!/usr/bin/env python3
import re
import os
import sys
import json
import requests


def main():
    # Initialize variables for template, file_content, and arg_file_path
    template = ""
    file_content = ""
    arg_file_path = ""

    # Check if command-line arguments are provided
    if len(sys.argv) > 1:
        # Set arg_file_path to the first argument
        arg_file_path = sys.argv[1]

        try:
            # Read file_content from arg_file_path
            with open(arg_file_path, "r") as file:
                file_content = file.read()
        except FileNotFoundError:
            # Print error message if file not found
            print(f"File not found: {arg_file_path}")
    else:
        # Print error message if no command-line arguments are provided
        print(
            "No command-line arguments provided. Please provide a file path as an argument."
        )
        return

    # Check if file_content is not empty
    if file_content:
        # Set template to the content of arg_file_path
        template = f"<s>[INST] You are a developer, edit the following code for \
            comment with `#` or `//` this: ```{file_content}```</s>"
    else:
        # Print error message if file_content is empty
        print(f"The {arg_file_path} is empty.")
        return

    # Set URL and headers for request to the completion endpoint
    url = "http://localhost:8080/completion"
    headers = {"Content-Type": "application/json"}

    # Set data for the request
    data = {"prompt": template, "n_predict": -1}

    # Send a POST request to the completion endpoint with the specified data
    response = requests.post(url, headers=headers, json=data)

    # Check if the status code of the response is 200 (indicating success)
    if response.status_code == 200:
        # Parse the response text as JSON
        response_data = json.loads(response.text)

        # Check if the content returned by the completion endpoint is empty
        if response_data["content"] == "":
            # Call main() recursively to continue adding comments
            main()
            return

        # Create a regex pattern to match lines starting with the specified pattern
        regex_pattern = re.compile(r"^" + re.escape(pattern), re.MULTILINE)

        # Use re.sub to replace matching lines with an empty string
        result_string = regex_pattern.sub("", response_data["content"])

        # Write the content returned by the completion endpoint to arg_file_path
        with open(arg_file_path, "w") as file:
            file.write(result_string)

        # Print success message
        print(f"Comments added to {arg_file_path}")
    else:
        # Print error message if the status code of the response is not 200
        print(f"Error: Request failed with status code {response.status_code}")
        print(response.text)


if __name__ == "__main__":
    main()
