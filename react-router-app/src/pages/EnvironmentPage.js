import React from 'react';
import { backgrounds, slimes } from '../data/slimes';
import Egg from '../components/Egg';

const EnvironmentPage = ({ environment }) => {
  const backgroundUrl = backgrounds[environment];
  const environmentSlimes = slimes.filter(
    (slime) => slime.environment === environment
  );

  const pageStyle = {
    backgroundImage: `url(${backgroundUrl})`,
    backgroundSize: 'cover',
    backgroundPosition: 'center',
    minHeight: '100vh',
    padding: '20px',
  };

  return (
    <div style={pageStyle}>
      <h1 style={{ color: 'white', textAlign: 'center' }}>
        Welcome to the {environment}!
      </h1>
      <div className="egg-grid">
        {environmentSlimes.map((slime) => (
          <Egg key={slime.id} slime={slime} />
        ))}
      </div>
    </div>
  );
};

export default EnvironmentPage;
