# 🚀 InvitePilot: Ultimate GitHub Collaborator Automator

<div align="center">

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![GitHub API](https://img.shields.io/badge/API-GitHub-lightgrey.svg?style=for-the-badge&logo=github)](https://docs.github.com/en/rest)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg?style=for-the-badge)](https://github.com/ishandutta2007/Invite-GitHub-Users/graphs/commit-activity)

**Streamline your GitHub workflow. Invite hundreds of collaborators in seconds.**

[Features](#-key-features) • [Web UI](#-modern-web-interface) • [Setup](#-installation--setup) • [Contributing](#-contributing)

</div>

---

## 📖 Overview

**InvitePilot** is a high-performance Python-based automation tool designed for developers, educators, and community managers who need to manage large-scale GitHub repository access. Whether you're running an open-source project, a coding bootcamp, or a corporate team, InvitePilot takes the manual labor out of collaborator management.

> [!TIP]
> **Why use InvitePilot?** Manually adding 100+ users via the GitHub UI takes hours. InvitePilot does it in minutes while you grab a coffee. ☕

---

## 🌟 Key Features

- **🎨 Professional Web UI:** A beautiful, responsive dashboard to manage invitations and monitor progress in real-time.
- **⚡ Bulk Invitation:** Process large batches of users efficiently via the GitHub REST API.
- **🔄 Smart Queueing:** Automatically tracks successes and retries failures. Your `to_be_invited.txt` stays clean.
- **🛡️ Rate Limit Protection:** Built-in intelligent delays to keep your GitHub account safe from secondary rate limits.
- **⚙️ Dynamic Configuration:** Override defaults via the UI or keep things stable with `.env` files.
- **📝 Detailed Logging:** Terminal-style logs with a full summary of every session.

---

## 🌐 Modern Web Interface

InvitePilot now features a high-end web dashboard named **InvitePilot Console**.

![InvitePilot Demo Placeholder](https://via.placeholder.com/800x400.png?text=InvitePilot+Web+UI+Demo+Coming+Soon)
*Real-time log streaming with glassmorphism aesthetics.*

### 🛠️ How to Start the Web Server
1. Ensure dependencies are installed: `pip install requests python-dotenv flask`
2. Launch the app:
   ```bash
   python app.py
   ```
3. Open your browser: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🛠️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/ishandutta2007/Invite-GitHub-Users.git
cd Invite-GitHub-Users
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
# OR
pip install requests python-dotenv flask
```

### 3️⃣ Configure Secrets
Create a `.env` file from the example:
```bash
cp .env.example .env
```
Add your **GitHub Personal Access Token** to `ADMIN_TOKEN`.

---

## 🚀 Usage Modes

### Method A: The Web Dashboard (Recommended)
Launch `app.py`, paste your list of usernames, and hit **Initialize Automation**.

### Method B: The CLI Power-User
Populate `to_be_invited.txt` with usernames and run the script. You can use optional arguments to override settings:
```bash
python invite.py --delay 5.0 --max-invites 100 --repo My-Awesome-Repo
```

#### Available CLI Arguments:
| Argument | Description |
| :--- | :--- |
| `--token` | GitHub Admin Token (overrides .env) |
| `--owner` | GitHub Repository Owner |
| `--repo` | GitHub Repository Name |
| `--max-invites`| Maximum number of invites to send (default: 60) |
| `--delay` | Delay in seconds between invites (default: 3.0) |
| `--input` | Path to input file (default: to_be_invited.txt) |
| `--success-log`| Path to success log (default: successful_invites.txt) |

---

## ⚙️ Configuration Parameters

| Parameter | Type | Description | Default |
| :--- | :--- | :--- | :--- |
| `OWNER` | String | GitHub Username / Organization | `ishandutta2007` |
| `REPO` | String | Target Repository Name | `Top-AI-repos` |
| `PERMISSION`| Enum | `pull`, `push`, `triage`, `maintain`, `admin` | `push` |
| `DELAY` | Float | Seconds to wait between API calls | `3.0` |

---

## 🛡️ Security Best Practices

- **Token Safety:** Never share your `.env` file or commit it to version control.
- **Scoped Access:** Use **Fine-grained Personal Access Tokens** to limit the script's reach to only necessary repositories.

---

## 🤝 Contributing

We love contributions! 
1. 🍴 Fork the Project
2. 🌿 Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. 💾 Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. 🚀 Push to the Branch (`git push origin feature/AmazingFeature`)
5. 📬 Open a Pull Request

---

## 📄 License

Distributed under the **MIT License**. See `LICENSE` for more information.

---

## 👤 Author

**Ishan Dutta**
- GitHub: [@ishandutta2007](https://github.com/ishandutta2007)
- Website: [ishandutta2007.github.io](https://ishandutta2007.github.io)

---

<div align="center">

### 📈 Project Velocity

![Star History Chart](https://api.star-history.com/chart?repos=ishandutta2007/Invite-GitHub-Users&type=date&theme=dark)

</div>

**SEO Keywords:** *GitHub API Automation, Bulk Invite Users, GitHub Collaborator Tool, Repository Management Script, Python GitHub Bot, DevOps Automation, GitHub REST API Python.*
