# 🤖 KAIRO AI – Personal Voice Assistant

KAIRO AI is a powerful **voice-controlled personal assistant** that can control your PC, automate tasks, send messages, and answer questions using an AI brain — all through natural voice commands.

---

## 🚀 Features

* 🎤 Voice Command Recognition
* 💻 Open & Control System Applications
* 🌐 Search Google & Play YouTube Songs
* 💬 Send WhatsApp Messages
* 🧠 AI Chat (Offline using Ollama)
* 🗣️ Text-to-Speech Response
* 🧠 Context Memory (Remembers last contact)
* 🎨 GUI Interface with Chat History
* ⚡ Always Listening Mode

---

## 🧠 Technologies Used

* Python
* SpeechRecognition
* pyttsx3
* pyautogui
* requests
* Tkinter (GUI)
* Ollama (Local AI Model)

---

## 📁 Project Structure

```
Kairo-ai/
│
├── main.py
├── gui.py
├── requirements.txt
│
├── brain/
│   ├── parser.py
│   ├── ai_brain.py
│   └── memory.py
│
├── voice/
│   ├── input.py
│   └── output.py
│
├── modules/
│   ├── system_control.py
│   ├── web.py
│   └── whatsapp.py
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```
git clone <your-repo-link>
cd Kairo-ai
```

---

### 2️⃣ Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Install Ollama

Download & install from: https://ollama.com

---

### 5️⃣ Run AI Model

For low RAM (4GB):

```
ollama run phi
```

---

### 6️⃣ Run Project

```
python main.py
```

OR (GUI):

```
python gui.py
```

---

## 🎤 Usage

Say commands like:

* “baby open chrome”
* “baby send hello to ankur”
* “baby play khairiyat”
* “baby what is artificial intelligence”

---

## 📱 WhatsApp Setup

* Open https://web.whatsapp.com
* Scan QR code
* Keep browser open

---

## 🚨 Troubleshooting

### ❌ Microphone not working

* Install PyAudio
* Check input device

### ❌ AI not responding

* Ensure Ollama is running
* Check model name (`phi`)

### ❌ WhatsApp not sending

* Increase delay in code
* Keep browser active

---

## 📦 Build Executable

```
pip install pyinstaller
pyinstaller --onefile --noconsole gui.py
```

---

## 🔮 Future Enhancements

* 📱 Mobile App Integration
* 🔐 Face & Voice Authentication
* ☁️ Cloud Sync
* 🧠 Advanced Memory System

---

## 👨‍💻 Author

**Sumit Mandal**

---

## ⭐ Show Your Support

If you like this project, please ⭐ star the repository!

---
