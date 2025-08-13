import React, { useState } from 'react';
import Slime from './Slime';
import { eggImage } from '../data/slimes';

const Egg = ({ slime }) => {
  const [hatched, setHatched] = useState(false);

  const handleHatch = () => {
    setHatched(true);
  };

  return (
    <div className="egg-container" onClick={!hatched ? handleHatch : null}>
      {hatched ? (
        <Slime slime={slime} />
      ) : (
        <img src={eggImage} alt="An egg" className="egg" />
      )}
    </div>
  );
};

export default Egg;
