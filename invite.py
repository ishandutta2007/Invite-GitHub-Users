import os
import time
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class GitHubInviter:
    def __init__(self, token=None, owner=None, repo=None, tbi_file=None, success_file=None):
        self.token = token or os.getenv("ADMIN_TOKEN")
        self.owner = owner or 'ishandutta2007'
        self.repo = repo or 'Top-AI-repos'
        self.tbi_file = tbi_file or 'to_be_invited.txt'
        self.success_file = success_file or 'successful_invites.txt'

    def invite_collaborator(self, username, permission='push'):
        # Strip '@' if present and any whitespace
        username = username.strip().lstrip('@')
        if not username:
            return False, "Empty username"

        url = f'https://api.github.com/repos/{self.owner}/{self.repo}/collaborators/{username}'

        headers = {
            'Authorization': f'token {self.token}',
            'Accept': 'application/vnd.github.v3+json'
        }

        # Permissions: pull, push, triage, maintain, admin
        payload = {'permission': permission}

        try:
            response = requests.put(url, headers=headers, json=payload)
            if response.status_code == 201:
                return True, "Invitation sent"
            elif response.status_code == 204:
                return True, "Already a collaborator"
            else:
                message = response.json().get('message', 'Unknown error')
                return False, message
        except Exception as e:
            return False, str(e)

    def run(self, max_invites=60, usernames_list=None):
        if not self.token:
            yield "Error: ADMIN_TOKEN not found."
            return

        source_is_file = False
        if usernames_list:
            to_process = [u.strip() for u in usernames_list if u.strip()][:max_invites]
            remaining = [] 
        else:
            if not os.path.exists(self.tbi_file):
                yield f"Error: {self.tbi_file} not found."
                return
            with open(self.tbi_file, 'r') as f:
                lines = f.readlines()
            if not lines:
                yield "TBI file is empty."
                return
            to_process = lines[:max_invites]
            remaining = lines[max_invites:]
            source_is_file = True

        successful_usernames = []
        failed_lines = []
        is_not_a_user = []

        yield f"Starting invitations for {len(to_process)} users..."

        for idx, line in enumerate(to_process):
            username = line.strip()
            if not username:
                continue
            
            is_invited_success, invite_message = self.invite_collaborator(username)
            status_prefix = f"[{idx+1}/{len(to_process)}]"
            
            if is_invited_success:
                successful_usernames.append(line)
                yield f"{status_prefix} Success: {username} ({invite_message})"
            else:
                if invite_message and "is not a user" in invite_message:
                    is_not_a_user.append(line)
                    yield f"{status_prefix} Failed: {username} (User not found)"
                else:
                    failed_lines.append(line)
                    yield f"{status_prefix} Error: {username} ({invite_message})"
            
            if idx < len(to_process) - 1:
                time.sleep(3)

        # Append successful to success file
        if successful_usernames:
            with open(self.success_file, 'a') as f:
                f.writelines([u if u.endswith('\n') else u + '\n' for u in successful_usernames])

        # Update TBI file if source was file
        if source_is_file:
            new_tbi_content = failed_lines + remaining
            with open(self.tbi_file, 'w') as f:
                f.writelines(new_tbi_content)
        elif failed_lines:
            yield f"Note: {len(failed_lines)} invites failed. Since you entered usernames directly, the input file was not updated."

        yield f"--- Summary ---"
        yield f"Processed {len(to_process)} users."
        yield f"Successful: {len(successful_usernames)}"
        yield f"Not a user: {len(is_not_a_user)}"
        yield f"Other failures: {len(failed_lines)}"

def main():
    inviter = GitHubInviter()
    for log in inviter.run():
        print(log)

if __name__ == "__main__":
    main()
