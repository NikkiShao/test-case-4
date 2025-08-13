import React from 'react';

const Slime = ({ slime }) => {
  return (
    <div className="slime">
      <img src={slime.imageUrl} alt={slime.name} />
      <p>{slime.name}</p>
    </div>
  );
};

export default Slime;
