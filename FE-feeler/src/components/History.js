import React, { useEffect, useState } from "react";
import { getHistory } from "../api";

const History = () => {
  const [history, setHistory] = useState([]);
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchHistory = async () => {
      const token = localStorage.getItem("accessToken");
      try {
        const response = await getHistory(token);
        setHistory(response.data);
      } catch (err) {
        setError("Failed to fetch history.");
      }
    };
    fetchHistory();
  }, []);

  return (
    <div className="history-container">
      <h1>Emotion History</h1>
      {error && <p className="error">{error}</p>}
      {history.length === 0 ? (
        <p>No history available.</p>
      ) : (
        <div className="history-list">
          {history.map((item, index) => (
            <div className="history-card" key={index}>
              <div className="profile">
                <img
                  src={`https://i.pravatar.cc/150?img=${3}`}
                  alt="Profile"
                  className="profile-pic"
                />
                <div className="username">@janymuong</div>
              </div>
              <div className="history-content">
                <p className="text">{item.text}</p>
                <p className="sentiment">
                  <strong>Sentiment:</strong> {item.sentiment}
                </p>
                <p className="confidence">
                  <strong>Confidence:</strong> {item.confidence.toFixed(4)}
                </p>
                <p className="date">
                  <strong>Date:</strong> {new Date(item.created_at).toLocaleString()}
                </p>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default History;
