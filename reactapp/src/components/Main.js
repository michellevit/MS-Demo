import React, { useState, useEffect } from "react";
import axios from 'axios';

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

  return (
    <div className="main">
      <h1>Mining Data</h1>
      <ul>
        {miningData.map(data => (
          <li key={data.id}>
            Date: {data.date}, Time: {data.time}, Latitude: {data.location_latitude}, Longitude: {data.location_longitude}, Cu Grade: {data.cu_grade}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Main;
