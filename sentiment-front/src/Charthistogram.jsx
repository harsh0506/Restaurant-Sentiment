import React from 'react';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';

const HistogramChart = ({ data , text }) => {
  return (
    
        <div className="text-center">
          <h2 className="text-blue-600 text-2xl font-semibold mb-4">{text} Review Ratings</h2>
          <div className="bg-white rounded-lg shadow-lg p-3">
            <BarChart width={350} height={250} data={data}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="rating" />
              <YAxis />
              <Tooltip />
              <Legend />
              <Bar dataKey="count" fill="#82ca9d" />
            </BarChart>
          </div>
        </div>
      );
};

export default HistogramChart;
