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
| **Clipboard** | The hidden place where copied text waits until you paste it. |
 
---
 
## Copy and paste in the terminal (read this first!)
 
Copy and paste work **differently** in a terminal. The usual `Ctrl + C` and `Ctrl + V` can misbehave, because in a terminal `Ctrl + C` means **"stop the running program"**, not "copy".
 
You will copy commands from this page and paste them into the terminal, so learn this now.
 
### Windows (PowerShell / Command Prompt / Windows Terminal)
 
| I want to... | Do this |
|---|---|
| **Copy** text from the terminal | Select it with the mouse, then press **`Ctrl + Insert`** |
| **Paste** a command into the terminal | **Right-click** inside the terminal window |
| Paste (keyboard alternative) | `Shift + Insert` (or `Ctrl + V` in newer terminals) |
| Copy (keyboard alternative) | `Ctrl + Shift + C` in Windows Terminal |
 
Tips:
- To paste a command from this page: copy it here (`Ctrl + C` works fine in your browser), click on the terminal, **right-click** once, then press **Enter** to run.
- In **Windows Terminal**, right-click copies if text is selected and pastes if nothing is selected. Click once on empty space first so nothing is selected, then right-click.
- Do not use `Ctrl + C` to copy inside the terminal. Use it only when you want to **stop** a running program.
### Linux (Ubuntu / Debian)
 
| I want to... | Do this |
|---|---|
| **Copy** text from the terminal | Select it with the mouse, then press **`Ctrl + Shift + C`** (or `Ctrl + Insert`) |
| **Paste** a command into the terminal | **`Ctrl + Shift + V`** (or `Shift + Insert`) |
| Paste with the mouse | **Right-click** and choose **Paste** (GNOME Terminal), or **middle-click** (scroll wheel) |
 
Tips:
- On Linux, **just selecting text with the mouse already copies it** (to a second clipboard). Middle-click pastes it. This is handy and unique to Linux.
- Plain `Ctrl + V` does **not** paste in most Linux terminals. Always add `Shift`.
- `Ctrl + Insert` and `Shift + Insert` work on both Windows and Linux, so they are the easiest pair to remember.
### Quick summary
 
| | Copy | Paste | Stop a running program |
|---|---|---|---|
| **Windows** | `Ctrl + Insert` | Right-click (or `Shift + Insert`) | `Ctrl + C` |
| **Linux** | `Ctrl + Shift + C` (or `Ctrl + Insert`) | `Ctrl + Shift + V` (or `Shift + Insert`, right-click, middle-click) | `Ctrl + C` |
 
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
Copy each command block below, **right-click** in the terminal to paste, then press Enter.
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
 
To stop the program at any time, press `Ctrl + C`.
 
---
 
## Linux (Ubuntu / Debian)
 
Open **Terminal** (Ctrl + Alt + T). Copy the block below, paste with **`Ctrl + Shift + V`** (or right-click → Paste), then press Enter:
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
 
To stop the program at any time, press `Ctrl + C`.
 
---
 
## Stuck?
 
| Problem | Fix |
|---|---|
| `'python' is not recognized` | Python is not on PATH. Reinstall Python and tick **Add python.exe to PATH**, then open a new terminal. Quick test: try `py --version`. |
| `'git' is not recognized` | Install Git, then close and reopen the terminal. |
| `cd` says path not found | Run `dir` (or `ls`) to see the exact folder names, then try again. |
| Boxes or QR look broken | Maximise the window. Use Windows Terminal or PowerShell, not an old window. |
| QR will not scan | Try zooming the terminal in with Ctrl and +, or copy the links printed under the QR codes. |
| Paste does nothing (Windows) | Right-click inside the terminal, or press `Shift + Insert`. |
| `Ctrl + V` prints `^V` or does nothing (Linux) | Use `Ctrl + Shift + V` or `Shift + Insert`. |
| Copied with `Ctrl + C` and the program stopped | `Ctrl + C` is "stop" in a terminal. Select the text and use `Ctrl + Insert` instead. |
 
---
 
## Useful terminal commands to remember
 
```
cd folder_name     go into a folder
cd ..              go back up one folder
dir  /  ls         list files (Windows / Linux)
cls  /  clear      clear the screen (Windows / Linux)
```
 
Handy keys: `Up arrow` brings back your previous command, `Tab` auto-completes file and folder names, `Ctrl + C` stops a running program.
 
---
 
## Awesome GitHub repos to keep learning
 
**Terminal and command line**
- [jlevy/the-art-of-command-line](https://github.com/jlevy/the-art-of-command-line): master the command line, in one page.
- [agarrharr/awesome-cli-apps](https://github.com/agarrharr/awesome-cli-apps): a big list of useful and fun terminal apps.
- [alebcay/awesome-shell](https://github.com/alebcay/awesome-shell): a curated list of shell tools and resources.
- [microsoft/terminal](https://github.com/microsoft/terminal): the Windows Terminal itself, open source.
**Python**
- [vinta/awesome-python](https://github.com/vinta/awesome-python): a curated list of Python frameworks, libraries and resources.
- [trekhleb/learn-python](https://github.com/trekhleb/learn-python): playground and cheatsheet for learning Python by examples.
- [Textualize/rich](https://github.com/Textualize/rich): make terminal output colourful and beautiful in Python.
- [Textualize/textual](https://github.com/Textualize/textual): build full apps that run inside the terminal.
**Git and GitHub**
- [firstcontributions/first-contributions](https://github.com/firstcontributions/first-contributions): make your first open source contribution in minutes.
**General learning**
- [practical-tutorials/project-based-learning](https://github.com/practical-tutorials/project-based-learning): learn programming by building real projects.
- [EbookFoundation/free-programming-books](https://github.com/EbookFoundation/free-programming-books): free books and courses on almost every language.
- [kamranahmedse/developer-roadmap](https://github.com/kamranahmedse/developer-roadmap): step-by-step roadmaps for different tech careers.
- [sindresorhus/awesome](https://github.com/sindresorhus/awesome): the list of all awesome lists.
---
 
Questions about admissions? Visit **https://www.sju.edu.in/admissions**.
 
