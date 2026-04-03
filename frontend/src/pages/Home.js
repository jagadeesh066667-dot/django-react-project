import React from "react";
import { Link } from "react-router-dom";
import "../styles.css";

function Home() {
  return (
    <div className="container">
      <div className="card">
        <h2>Welcome 🚀</h2>

        <Link to="/login">Login</Link><br />
        <Link to="/register">Register</Link>
      </div>
    </div>
  );
}

export default Home;