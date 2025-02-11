import React from "react";
import { BrowserRouter as Router, Routes, Route, Link, useNavigate } from "react-router-dom";
import Login from "./components/Auth/Login";
import Register from "./components/Auth/Register";
import Dashboard from "./components/Dashboard";
import History from "./components/History";
import Visualization from "./components/Visualization";
import { logout } from "./api";
import logo from "./assets/moodlens_logo.svg"; // Import the MoodLens logo
import "./styles.css";

const Navbar = () => {
  const navigate = useNavigate();

  const handleLogout = async () => {
    const accessToken = localStorage.getItem("accessToken");
    const refreshToken = localStorage.getItem("refreshToken");

    try {
      await logout(refreshToken, accessToken); // Invalidate tokens via API
    } catch (err) {
      console.error("Error logging out:", err);
    }

    // Clear tokens and redirect to login
    localStorage.removeItem("accessToken");
    localStorage.removeItem("refreshToken");
    navigate("/");
  };

  return (
    <nav className="navbar">
      <div className="navbar-logo-container">
        <img src={logo} alt="MoodLens Logo" className="logo" />
        <span className="app-name">SENTIMENT-140</span>
      </div>
      <div className="navbar-links">
        <Link to="/dashboard">Model</Link>
        <Link to="/history">Emotion History</Link>
        <Link to="/visualization">Emotion Graphs</Link>
        <button className="logout-link" onClick={handleLogout}>
          Logout
        </button>
      </div>
    </nav>
  );
};

const App = () => {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/history" element={<History />} />
        <Route path="/visualization" element={<Visualization />} />
      </Routes>
    </Router>
  );
};

export default App;
