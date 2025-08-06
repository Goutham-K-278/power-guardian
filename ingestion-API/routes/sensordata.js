const express = require('express');
const router = express.Router();
const { receiveSensorData } = require('../controllers/sensorcontroller');
const validatePayload = require('../middleware/validatepayloads');

// POST endpoint to receive data
router.post('/ingest', validatePayload, receiveSensorData);

module.exports = router;
