import React from 'react';
import { Routes, Route, Link } from 'react-router-dom';
import Home from './components/Home';
import EnvironmentPage from './pages/EnvironmentPage';
import './App.css';

function App() {
  return (
    <div>
      <nav>
        <ul>
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <Link to="/forest">Forest</Link>
          </li>
          <li>
            <Link to="/field">Field</Link>
          </li>
          <li>
            <Link to="/sea">Sea</Link>
          </li>
        </ul>
      </nav>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route
          path="/forest"
          element={<EnvironmentPage environment="forest" />}
        />
        <Route
          path="/field"
          element={<EnvironmentPage environment="field" />}
        />
        <Route path="/sea" element={<EnvironmentPage environment="sea" />} />
      </Routes>
    </div>
  );
}

export default App;
