import React, { useState } from "react";
import { predict } from "../api";

const Dashboard = () => {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);

  const handleAnalyze = async () => {
    const token = localStorage.getItem("accessToken");
    if (!text.trim()) return;
    try {
      const response = await predict({ text }, token);
      setResult(response.data);
    } catch (err) {
      alert("Error analyzing sentiment.");
    }
  };

  return (
    <div className="dashboard-container">
      <h1>feeler</h1>
      <textarea
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Type out your thoughts in here..."
      />
      <button onClick={handleAnalyze} className="analyze-btn">
        Analyze Emotion
      </button>
      {result && (
        <div className="result">
          <p><strong>Sentiment:</strong> {result.sentiment}</p>
          <p><strong>Confidence:</strong> {result.confidence.toFixed(4)}</p>
        </div>
      )}
    </div>
  );
};

export default Dashboard;
