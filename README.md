<p align="center" width="100%">
<img src="./assets/llm-cmd-logo.jpeg" alt="Vigogne" style="width: 40%; min-width: 300px; display: block; margin: auto;">
</p>

<p align="center">
    <img alt="Python" src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">
    <img alt="Docker" src="https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white">
</p>

<p align="center">
    ✨ LLM CMD is a toolbox allowing you to use LLM in daily developer commands 💻
</p>

## 🤗 Fun Facts

• This readme was largely generated with `cmd/readme.py`.

• All commit messages were generated with `cmd/git/commit.py`.

• All code comments were generated with `cmd/comment.py`

## 📚 Table of commands

- 📝 [readme](#readme)
- 🚀 [git commit](#git-commit)
- 💭 [comment](#comment)

## 🎬 Setup

Execute the following command:

```bash
make
```

It will download the [Hugging Face](https://huggingface.co/) model (you can change it in the top of the `Makefile`) and run it with llama.cpp server.

## 📝 readme

This is a Python script that generates a README.md file based on user input and a file path provided as an argument. The script uses the `requests` library to interact with an API endpoint that generates the README content, and writes it to a local README file.

### Usage

Run the script with the necessary arguments:

```bash
python3 cmd/readme.py path/to/your/file
```

Replace `path/to/your/file` with the actual path to your project file.

### Functionality

The `cmd/readme.py` script performs the following tasks:

1. Checks whether a README.md file exists in the current directory. If it does, it rewrites the file using the provided content.
2. Takes command-line arguments that specify a file path to use as the prompt for the language model.
3. Reads the content of the specified file and uses it to generate a README.md template.
4. Sends a POST request to a pre-trained language model API (http://localhost:8080/completion) with the generated template as input. The API generates completion prompts based on the template, which are then written to the README.md file.
5. If the generated prompt is empty, the script calls itself recursively with the original command-line arguments to continue generating prompts until a non-empty prompt is obtained.

## 🚀 git commit

This script is a simple command-line tool that helps you write commit messages for your Git repository using an artificial intelligence (AI) completion system. The AI system generates completion suggestions based on the commit message prompt provided by the user.

### Usage

To use this tool, follow these steps:

1. Run the following command to add your file to your repo git:
```bash
git add path/to/your/file
```
2. Run the following command to execute the script:
```bash
python3 cmd/git/commit.py
```
3. Git will automatically commit your changes with the generated commit message.
4. Now you can execute the following command for push:
```bash
git push
```

## 💭 comment

This script is a simple Python script that takes a file path as an argument and attempts to add comments to the code within it. The script uses an API endpoint to generate completion suggestions for comments and replaces any lines that match the specified comment pattern with empty strings.

### Usage

To use this script, run it from the command line with the path to the file you want to add comments to as an argument:

```sh
python3 cmd/comment.py /path/to/your/file.py
```
