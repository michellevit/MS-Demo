import React, { useState, useEffect } from "react";
import axios from 'axios';
import Plotly from "plotly.js-basic-dist";
import createPlotlyComponent from "react-plotly.js/factory";

const Plot = createPlotlyComponent(Plotly);

function Main() {
  const [miningData, setMiningData] = useState([]);

  useEffect(() => {
    async function fetchData() {
      try {
        const response = await axios.get('/api/mining-data/');
        setMiningData(response.data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    }

    fetchData();
  }, []);

  const heatmapData = {
    x: miningData.map(data => data.location_latitude),
    y: miningData.map(data => data.location_longitude),
    z: miningData.map(data => data.cu_grade),
    type: "heatmap",
    colorscale: "Hot"
  };

  return (
    <div className="main">
      <h1>Mining Data</h1>
      <Plot
        data={[heatmapData]}
        layout={{
          width: 800,
          height: 600,
          title: "Cu Grade Heatmap",
          xaxis: { title: "Latitude" },
          yaxis: { title: "Longitude" }
        }}
      />
    </div>
  );
}

export default Main;
