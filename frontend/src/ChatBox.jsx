import { useState } from "react";
import axios from "axios";

function ChatBox() {
  const [prompt, setPrompt] = useState("");
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);

  const sendPrompt = async () => {
    if (!prompt.trim()) return;
    setLoading(true);
    try {
      const res = await axios.post("http://localhost:8000/chat/", {
        prompt: prompt.trim(),
      });
      setResponse(res.data.response);
    } catch (err) {
      setResponse("⚠️ Something went wrong!");
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="p-6 max-w-xl mx-auto">
      <h1 className="text-2xl font-bold mb-4">💬 Gemini Chat</h1>
      <textarea
        className="w-full border p-2 rounded"
        rows={3}
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        placeholder="Type your prompt here..."
      />
      <button
        className="mt-2 bg-blue-600 text-white px-4 py-2 rounded"
        onClick={sendPrompt}
        disabled={loading}
      >
        {loading ? "Thinking..." : "Ask Gemini"}
      </button>
      {response && (
        <div className="mt-4 p-3 bg-gray-100 rounded text-black whitespace-pre-wrap">
          {response}
        </div>
      )}
    </div>
  );
}

export default ChatBox;
