import React, { useEffect, useRef } from 'react';
import functionPlot from 'function-plot';

function Graph({ fn }) {
  const graphRef = useRef(null);

  useEffect(() => {
    if (graphRef.current) {
      try {
        functionPlot({
          target: graphRef.current,
          width: 500,
          height: 400,
          grid: true,
          data: [{
            fn: fn || 'x^2', // Default function if none is provided
            graphType: 'polyline'
          }]
        });
      } catch (e) {
        console.error(e);
      }
    }
  }, [fn]);

  return (
    <div ref={graphRef} />
  );
}

export default Graph;
