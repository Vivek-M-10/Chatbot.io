# 🤖 Chatbot.io

An AI-powered chatbot application built using FastAPI for the backend and Vite + React for the frontend. It leverages Google’s Gemini 1.5 Flash model to generate intelligent and contextual responses.

---

## 🚀 Features

- ⚡ FastAPI backend serving AI responses
- 💬 Gemini 1.5 Flash model integration
- 🌐 Vite + React modern frontend
- 🔐 Secure API key handling with `.env`
- 🌍 CORS-enabled for local frontend/backend communication

---

## 📦 Tech Stack

- **Frontend**: React (Vite)
- **Backend**: FastAPI (Python)
- **AI Model**: Google Generative AI (Gemini)
- **Others**: Axios, dotenv, CORS

---

## 🧑‍💻 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/chatbot.io.git
cd chatbot.io
````

---

### 2. Backend Setup (`/backend`)

#### 📦 Install dependencies

```bash
cd backend
pip install -r requirements.txt
```

#### 🔐 Create `.env` file

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

#### 🚀 Run FastAPI server

```bash
uvicorn main:app --reload
```

Backend runs at: `http://localhost:8000`

---

### 3. Frontend Setup (`/frontend`)

#### 📦 Install dependencies

```bash
cd ../frontend
npm install
```

#### 🚀 Start the frontend server

```bash
npm run dev
```

Frontend runs at: `http://localhost:5173`

---

## 🔗 API Endpoint

### `POST /chat/`

**Request:**

```json
{
  "prompt": "Tell me a joke"
}
```

**Response:**

```json
{
  "response": "Why don't scientists trust atoms? Because they make up everything!"
}
```

---

## 📸 Preview

> *Add a screenshot or GIF demo here if available.*

---

## 🛡️ Environment Variables

Backend `.env`:

```env
GEMINI_API_KEY=your_actual_api_key
```

> 🔑 Get your Gemini API key from: [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)

---

## 🧠 Credits

* 💻 Built by [Your Name](https://github.com/your-username)
* 🤖 Powered by [Google Generative AI](https://ai.google.dev/)

---

## 📄 License

This project is licensed under the **MIT License**. Feel free to use and modify it.

```

---

Let me know if:
- You want to add deployment steps (like Vercel + Railway/Fly.io)
- You'd like a project badge or logo at the top
- You're ready to publish and want a `.gitignore`, `Dockerfile`, or `LICENSE` file added
```
