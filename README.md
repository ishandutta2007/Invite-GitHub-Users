# 🚀 Invite-GitHub-Users

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub API](https://img.shields.io/badge/API-GitHub-lightgrey.svg)](https://docs.github.com/en/rest)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/ishandutta2007/Invite-GitHub-Users/graphs/commit-activity)

**Automate your GitHub collaboration workflow with ease.** This Python script allows you to bulk-invite users to your GitHub repositories using the GitHub REST API. Perfect for managing large-scale projects, educational courses, or community-driven repositories.

---

## 🌟 Key Features

- **Web UI:** Modern browser-based interface for configuration and real-time log monitoring.
- **Bulk Invitation:** Process up to 60 users per run (batch-limited to stay within safe API limits).
- **Smart Queue Management:** Automatically updates your invitation list, moving successful invites to a log and keeping failed ones for retries.
- **Rate Limit Friendly:** Built-in delays (3 seconds between requests) to avoid triggering GitHub's secondary rate limits.
- **Simple Configuration:** Environment-based setup for security and portability.
- **Duplicate Handling:** Gracefully handles users who are already collaborators.

---

## 🛠️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/ishandutta2007/Invite-GitHub-Users.git
cd Invite-GitHub-Users
```

### 2. Install Dependencies
Ensure you have Python 3.6+ installed. Install the required libraries using pip:
```bash
pip install requests python-dotenv flask
```

### 3. Configure Environment Variables
Copy the example environment file and add your GitHub Personal Access Token (PAT).
```bash
cp .env.example .env
```
Edit `.env` and provide your `ADMIN_TOKEN`.

> **Note:** Your token needs **Fine-grained permissions** or **Classic scope** with `repo` (Administration: Read and Write) for the target repository.

### 4. Prepare User Lists
- Edit `to_be_invited.txt` and add the GitHub usernames you wish to invite (one per line).
- Alternatively, you can paste them directly into the Web UI.

---

## 🌐 Web Interface (Recommended)

The project now includes a modern web-based UI for easier management.

### How to Start the Server
```bash
python app.py
```
Once started, open your browser and navigate to: **`http://127.0.0.1:5000`**

### UI Features:
- **Live Logs:** Real-time terminal output in the browser.
- **Direct Entry:** Paste usernames directly into the UI (overrides file input).
- **On-the-fly Config:** Change target repo, owner, or max invites without editing code.
- **Smart Fallbacks:** Leave fields empty to use your `.env` or script defaults.

---

## 🚀 CLI Usage (Legacy)

Simply run the script:
```bash
python invite.py
```

### How it works:
1. The script reads the first 60 names from `to_be_invited.txt`.
2. It sends an invitation to each user for the repository defined in `invite.py`.
3. Successful invites are appended to `successful_invites.txt`.
4. `to_be_invited.txt` is updated: successful users are removed, and failed ones are kept at the top for the next run.

---

## ⚙️ Configuration

You can customize the script by editing the following variables in `invite.py`:

| Variable | Description | Default |
| :--- | :--- | :--- |
| `OWNER` | Your GitHub Username / Org Name | `ishandutta2007` |
| `REPO` | The name of the target repository | `Top-AI-repos` |
| `permission` | Access level (`pull`, `push`, `triage`, `maintain`, `admin`) | `push` |
| `TBI_FILE` | Input file for usernames | `to_be_invited.txt` |
| `SUCCESS_FILE`| Log file for successes | `successful_invites.txt`|

---

## 🛡️ Security

- **Never** commit your `.env` file or hardcode your tokens.
- Use **Fine-grained Personal Access Tokens** for better security, limiting access only to specific repositories.

---

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improvements or bug fixes, feel free to:
1. Fork the repo.
2. Create a new branch.
3. Submit a Pull Request.

---

## 📄 License

Distributed under the MIT License. See `LICENSE` (if applicable) or the badge above for more information.

---

## 👤 Author

**Ishan Dutta**
- GitHub: [@ishandutta2007](https://github.com/ishandutta2007)

---


## 📈 Star History

<div align="center">
  <a href="https://www.star-history.com/?repos=ishandutta2007%2FInvite-GitHub-Users&type=date&legend=bottom-right">
   <picture>
     <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Invite-GitHub-Users&type=date&theme=dark&legend=bottom-right" />
     <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Invite-GitHub-Users&type=date&legend=bottom-right" />
     <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=ishandutta2007/Invite-GitHub-Users&type=date&legend=bottom-right" />
   </picture>
  </a>
</div>

---


*Keywords: GitHub API, Python Automation, Bulk Invite, GitHub Collaborators, Repository Management, DevOps Tools.*
