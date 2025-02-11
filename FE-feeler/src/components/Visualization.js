import React, { useEffect, useState } from "react";
import { Line } from "react-chartjs-2";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";
import { getVisualization } from "../api";

// Register components
ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend);

const Visualization = () => {
  const [data, setData] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      const token = localStorage.getItem("accessToken");
      try {
        const response = await getVisualization(token);
        setData(response.data);
      } catch (err) {
        alert("Error fetching visualization data.");
      }
    };
    fetchData();
  }, []);

  return (
    <div className="visualization-container">
      <h1>Past Sentiments</h1>
      {data ? (
        <Line
          data={{
            labels: data.labels,
            datasets: [
              {
                label: "Sentiments",
                data: data.sentiments,
                borderColor: "blue",
                backgroundColor: "rgba(0, 123, 255, 0.5)",
                fill: true,
              },
            ],
          }}
          options={{
            responsive: true,
            plugins: {
              legend: {
                position: "top",
              },
              title: {
                display: true,
                text: "Sentiment Analysis Trends",
              },
            },
          }}
        />
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
};

export default Visualization;
