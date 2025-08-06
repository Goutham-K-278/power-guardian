const express = require('express');
const dotenv = require('dotenv');
const connectDB = require('./config/db');
const sensorRoutes = require('./routes/sensordata');

dotenv.config(); // Load environment variables

const app = express();
const PORT = process.env.PORT || 5000;

// Middleware to parse JSON
app.use(express.json());

// DB Connection
connectDB();

// API Routes
app.use('/api/sensor', sensorRoutes);

// Health check
app.get('/', (req, res) => {
  res.send('Power Guardian Ingestion API is running...');
});

// Start server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
