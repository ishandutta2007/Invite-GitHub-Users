import os
import time
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# --- Configuration ---
ADMIN_TOKEN = os.getenv("ADMIN_TOKEN")
OWNER = 'ishandutta2007'
REPO = 'Top-AI-repos'
TBI_FILE = 'to_be_invited.txt'
SUCCESS_FILE = 'successful_invites.txt'

def invite_collaborator(token, owner, repo, username, permission='push'):
    # Strip '@' if present and any whitespace
    username = username.strip().lstrip('@')
    if not username:
        return False

    url = f'https://api.github.com/repos/{owner}/{repo}/collaborators/{username}'

    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }

    # Permissions: pull, push, triage, maintain, admin
    payload = {'permission': permission}

    try:
        response = requests.put(url, headers=headers, json=payload)
        if response.status_code == 201:
            print(f"Success: Invitation sent to {username}.")
            return True
        elif response.status_code == 204:
            print(f"Success: {username} is already a collaborator.")
            return True
        else:
            print(f"Error {response.status_code} for {username}: {response.json().get('message')}")
            return False, response.json().get('message')
    except Exception as e:
        print(f"Exception for {username}: {e}")
        return False

def main():
    if not ADMIN_TOKEN:
        print("Error: ADMIN_TOKEN not found in .env file.")
        return

    if not os.path.exists(TBI_FILE):
        print(f"Error: {TBI_FILE} not found.")
        return

    with open(TBI_FILE, 'r') as f:
        lines = f.readlines()

    if not lines:
        print("TBI file is empty.")
        return

    to_process = lines[:60]
    remaining = lines[60:]
    
    successful_usernames = []
    failed_lines = []
    is_not_a_user = []

    for idx, line in enumerate(to_process):
        username = line.strip()
        if not username:
            continue
        print(f"[{idx+1}/{len(to_process)}]")
        is_invited_success, invite_message = invite_collaborator(ADMIN_TOKEN, OWNER, REPO, username)
        if is_invited_success:
            successful_usernames.append(line)
        else:
            if invite_message and "is not a user" in invite_message:
                is_not_a_user.append(line)
            else:
                failed_lines.append(line)
        time.sleep(3)

    # Append successful to success file
    if successful_usernames:
        with open(SUCCESS_FILE, 'a') as f:
            f.writelines(successful_usernames)

    # Update TBI file: keep failed ones from the first 60 at the top, followed by the rest
    new_tbi_content = failed_lines + remaining
    with open(TBI_FILE, 'w') as f:
        f.writelines(new_tbi_content)

    print(f"Processed {len(to_process)} users. {len(successful_usernames)} successful, {len(is_not_a_user)} not a user, {len(failed_lines)} other failure.")

if __name__ == "__main__":
    main()
