import os
import sys
import subprocess
import requests
import json


def get_model():
    return os.getenv("AICMT_MODEL", "gpt-4o-mini")

def get_source_type():
    return os.getenv("AICMT_SOURCE_TYPE", "openai")

def get_api_base_url():
    return os.getenv("AICMT_API_BASE_URL", "https://api.openai.com/v1")

def get_diff_max_length():
    return int(os.getenv("AICMT_DIFF_MAX_LENGTH", 500))

def get_api_key():
    return os.getenv("AICMT_API_KEY", "")

def get_remove_chars():
    return os.getenv("AICMT_REMOVE_CHARS", '`,"').split(",")

def get_git_status_items():

    diff_files = []
    diff_lines = subprocess.getoutput("git diff --cached --name-status").splitlines()
    for line in diff_lines:
        action, file = line[:1].strip(), line[2:].strip()
        diff_files.append(file)

    output_lines = []
    status_lines = subprocess.getoutput("git status --porcelain").splitlines()
    for line in status_lines:
        action, file = line[:2].strip(), line[3:].strip()
        if file in diff_files:
            output_lines.append({
                "action": action,
                "file": file
            })
    
    return output_lines
        
def get_file_diff(file):
    diff = subprocess.getoutput(f"git diff --cached {file}").splitlines()
    if(len(diff) <= 0):
        diff.append("File: " + file)
        with open(file, 'r') as f:
            diff += f.readlines()
    return "\n".join(diff)

def check_api_running():
    if not get_api_key():
        print("API key not found. Please set AICMT_API_KEY environment variable.")
        sys.exit(1)
    
    if get_source_type() == "openai":
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {get_api_key()}"
        }
        response = requests.get(f"{get_api_base_url()}/models", headers=headers)
        if response.status_code != 200:
            print("API key is invalid or the API is down.")
            sys.exit(1)
    elif get_source_type() == "ollama":
        headers = {"Content-Type": "application/json"}
        response = requests.get(f"{get_api_base_url()}/models", headers=headers)
        if response.status_code != 200:
            print("API key is invalid or the API is down.")
            sys.exit(1)
            

def ask_api(content):
    model = get_model()
    prompt = f"""
Generate a commit message for the following changes. 
Explains what changes have been made. 
Do not include any description only the message. 
Only output the message.

----------

{content}
"""

    if get_source_type() == "openai":
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {get_api_key()}"
        }
        data = {
            "model": model,
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        }
        response = requests.post(f"{get_api_base_url()}/chat/completions", headers=headers, json=data)
        response = response.json().get('choices', [{}])[0].get('message', {}).get('content', '')
    elif get_source_type() == "ollama":
        headers = {"Content-Type": "application/json"}
        data = {
            "model": model,
            "prompt": json.dumps(prompt),
            "stream": False
        }
        response = requests.post(f"{get_api_base_url()}/generate", headers=headers, json=data)
        response = response.json().get('response', '')

    stripped_response = response
    for char in get_remove_chars():
        stripped_response = stripped_response.replace(char, "")
    stripped_response = stripped_response.strip()
    
    return stripped_response

def execute():

    check_api_running()

    status_items = get_git_status_items()

    for item in status_items:
        action = item.get("action")
        file = item.get("file")
        commit_message = ""

        if action == "R":
            commit_message = f"Renamed {file}"
        elif action == "C":
            commit_message = f"Copied {file}"
        elif action == "T":
            commit_message = f"Type changed for {file}"
        elif action == "A":
            commit_message = f"Added {file}"
        elif action == "D":
            commit_message = f"Deleted {file}"
        elif action == "M" or action == "AM" or action == "MM":
            diff = get_file_diff(file)
            diff = diff[:get_diff_max_length()]
            commit_message = ask_api(diff)
        
        if commit_message:
            print(f"Committing: {commit_message}")
            subprocess.run(["git", "commit", "-m", commit_message])

