const { insertSensorData } = require('../models/sensormodel');

const receiveSensorData = async (req, res) => {
  try {
    const savedData = await insertSensorData(req.body);
    res.status(201).json({
      message: 'Sensor data saved successfully.',
      data: savedData
    });
  } catch (error) {
    console.error('Error saving sensor data:', error);
    res.status(500).json({ error: 'Failed to save sensor data.' });
  }
};

module.exports = {
  receiveSensorData
};
