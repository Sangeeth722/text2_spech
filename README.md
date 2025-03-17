# Vue 3 + Vite

This template should help get you started developing with Vue 3 in Vite. The template uses Vue 3 `<script setup>` SFCs, check out the [script setup docs](https://v3.vuejs.org/api/sfc-script-setup.html#sfc-script-setup) to learn more.

Learn more about IDE Support for Vue in the [Vue Docs Scaling up Guide](https://vuejs.org/guide/scaling-up/tooling.html#ide-support).

# Vue.js + Flask Text-to-Speech (TTS) App

This project is a **Text-to-Speech (TTS) app** built using **Vue.js** for the frontend and **Flask** for the backend. The app converts user-entered text into speech and provides an audio file for playback.

## 📂 Project Structure

```
text2_spech/
│── backend/         # Flask backend
│   ├── main.py      # Flask server code
│   ├── requirements.txt  # Python dependencies
│── frontend/        # Vue.js frontend
│   ├── src/         # Vue source files
│   ├── package.json # Vue dependencies
│── README.md        # Project documentation
│── .gitignore       # Files to ignore in Git
```

## 🛠️ Setup Instructions

### 1️⃣ Backend (Flask)

#### Prerequisites

- Python 3 installed
- Flask & dependencies

#### Installation Steps

```bash
cd backend
python -m venv venv  # Create a virtual environment
source venv/bin/activate  # (Linux/macOS) Activate virtual environment
venv\Scripts\activate  # (Windows) Activate virtual environment
pip install -r requirements.txt  # Install dependencies
python main.py  # Run Flask server
```

The Flask API will run on **`http://127.0.0.1:5000/api`**.

---

### 2️⃣ Frontend (Vue.js)

#### Prerequisites

- Node.js installed
- Vue CLI installed (`npm install -g @vue/cli`)

#### Installation Steps

```bash
cd frontend
npm install  # Install Vue dependencies
npm run dev  # Start Vue development server
```

The Vue app will run on **`http://localhost:5173/`** (default Vite port).

---

## 🚀 How It Works

1. Enter text in the input field on the frontend.
2. Click **Submit** to send the text to the Flask backend.
3. Flask uses **gTTS (Google Text-to-Speech)** to generate an audio file.
4. The audio file is sent back to the frontend and can be played or downloaded.

---

## 📝 API Endpoint

**POST /api** – Converts text to speech and returns an audio file.

**Request:**

```json
{
  "text": "Hello, how are you?"
}
```

**Response:**

- An audio file (`output.mp3`) is returned as a response.

---

## 🔥 Features

- 📝 **Text Input:** Users enter text to convert to speech.
- 🔊 **Audio Playback:** The generated speech is playable in the browser.
- ⬇️ **Download Audio:** Users can download the generated MP3 file.
- ⚡ **Fast API Calls:** Flask processes requests quickly using **gTTS**.
- 🔄 **Vue + Axios:** Uses Axios for HTTP requests to Flask.

---

## 📌 Technologies Used

- **Frontend:** Vue.js, Vite, Axios, Tailwind CSS
- **Backend:** Flask, gTTS (Google Text-to-Speech), Flask-CORS
- **Hosting:** Local development setup

---

## 🛑 Troubleshooting

- **CORS issues?** Install Flask-CORS: `pip install flask-cors`
- **Port conflicts?** Change the Vue or Flask port in `vite.config.js` or `main.py`
- **PermissionError on Windows?** Try deleting `output.mp3` manually before restarting Flask.

---

## 🤝 Contributing

Feel free to fork this repository, create issues, or submit pull requests!

---

## 📜 License

This project is open-source and available under the **MIT License**.

---

### 📧 Contact

For any queries, reach out via GitHub Issues or email at `your-email@example.com`.
