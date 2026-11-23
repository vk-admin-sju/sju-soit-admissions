# SJU SoIT Admissions 2026: Terminal Edition

St Joseph's University, School of Information Technology, Bengaluru.

Want to see our admissions poster **inside your terminal**? Follow the steps below. It takes about 10 minutes and you pick up some real developer skills on the way.

> The official source for all admissions information is **https://www.sju.edu.in/admissions**. This repo is just for fun and learning.

---

## Words you will meet

| Word | One-line meaning |
|---|---|
| **Terminal / CLI** | A text window where you type commands instead of clicking (CLI = Command Line Interface). |
| **Command** | An instruction you type, then press Enter to run. |
| **Folder / directory** | Same thing: a place that holds files. |
| **`cd`** | "Change directory": moves you into a folder. |
| **`dir` (Windows) / `ls` (Linux)** | Lists what is inside the current folder. |
| **Python** | A programming language. Our script is written in it. |
| **PATH** | A list of places your computer looks when you type a command. Python must be on it, or the terminal says "not recognized". |
| **Git** | A tool that downloads and tracks code. |
| **Repository (repo)** | A project folder stored on GitHub. |
| **Clone** | Download a repo to your computer. |
| **Requirements** | Extra libraries our script needs. They are listed in `requirements.txt`. |

---

## Windows

### 1. Open a terminal
Press the **Windows key**, type **PowerShell**, press Enter. (Command Prompt, called `cmd`, also works.)

### 2. Install Python
1. Download it from https://www.python.org/downloads/ and run the installer.
2. **Important:** on the first screen, tick **"Add python.exe to PATH"**, then click Install Now.
3. Close the terminal and open a new one. Check that it worked:
   ```
   python --version
   ```
   A version number such as `Python 3.12.x` means success.

### 3. Install Git
Download from https://git-scm.com/download/win, run it and click Next on every screen. Open a **new** terminal and check:
```
git --version
```

### 4. Download this project
```
cd Documents
git clone https://github.com/vk-admin-sju/sju-soit-admissions.git
cd sju-soit-admissions
dir
```
You should see `admissions.py` and `requirements.txt` in the list.

*(No Git? On the GitHub page click **Code → Download ZIP**, extract it, then `cd` into the extracted folder.)*

### 5. Install the requirements and run
```
python -m pip install -r requirements.txt
python admissions.py
```
Maximise the window for the best view, then scan the QR codes with your phone.

---

## Linux (Ubuntu / Debian)

Open **Terminal** (Ctrl + Alt + T), then:
```
sudo apt update
sudo apt install -y git python3 python3-venv python3-pip
cd ~
git clone https://github.com/vk-admin-sju/sju-soit-admissions.git
cd sju-soit-admissions
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python admissions.py
```
`venv` is a private sandbox for the libraries, so nothing on your system gets messed up. Type `deactivate` to leave it.

---

## Stuck?

| Problem | Fix |
|---|---|
| `'python' is not recognized` | Python is not on PATH. Reinstall Python and tick **Add python.exe to PATH**, then open a new terminal. Quick test: try `py --version`. |
| `'git' is not recognized` | Install Git, then close and reopen the terminal. |
| `cd` says path not found | Run `dir` (or `ls`) to see the exact folder names, then try again. |
| Boxes or QR look broken | Maximise the window. Use Windows Terminal or PowerShell, not an old window. |
| QR will not scan | Try zooming the terminal in with Ctrl and +, or copy the links printed under the QR codes. |

---

## Useful terminal commands to remember

```
cd folder_name     go into a folder
cd ..              go back up one folder
dir  /  ls         list files (Windows / Linux)
cls  /  clear      clear the screen (Windows / Linux)
```

Questions about admissions? Visit **https://www.sju.edu.in/admissions**.
