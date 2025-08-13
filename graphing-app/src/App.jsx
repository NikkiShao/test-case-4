import { useState } from 'react';
import './App.css';
import Graph from './Graph';

function App() {
  const [fn, setFn] = useState('x');

  const handleInputChange = (event) => {
    setFn(event.target.value);
  };

  return (
    <>
      <h1>Function Grapher</h1>
      <div className="card">
        <input
          type="text"
          value={fn}
          onChange={handleInputChange}
          placeholder="Enter a function, e.g., x^2"
        />
        <p>
          Enter a function and see it plotted below.
        </p>
      </div>
      <div className="card">
        <Graph fn={fn} />
      </div>
    </>
  );
}

export default App;
