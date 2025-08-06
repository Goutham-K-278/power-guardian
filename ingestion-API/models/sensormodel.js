const { pool } = require('../config/db');

const insertSensorData = async (data) => {
  const {
    timestamp,
    voltage,
    current,
    power,
    frequency,
    location,
    fault_type
  } = data;

  const query = `
    INSERT INTO sensor_data (timestamp, voltage, current, power, frequency, location, fault_type)
    VALUES ($1, $2, $3, $4, $5, $6, $7)
    RETURNING *;
  `;

  const values = [timestamp, voltage, current, power, frequency, location, fault_type];

  try {
    const result = await pool.query(query, values);
    return result.rows[0];
  } catch (err) {
    throw err;
  }
};

module.exports = {
  insertSensorData
};
