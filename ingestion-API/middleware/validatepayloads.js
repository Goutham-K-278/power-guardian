const validatePayload = (req, res, next) => {
  const { timestamp, voltage, current, power, frequency, location, fault_type } = req.body;

  if (
    !timestamp || typeof voltage !== 'number' || typeof current !== 'number' ||
    typeof power !== 'number' || typeof frequency !== 'number' ||
    typeof location !== 'string' || typeof fault_type !== 'string'
  ) {
    return res.status(400).json({
      error: 'Invalid sensor payload. Check all fields and data types.'
    });
  }

  next(); // Move to next middleware/controller
};

module.exports = validatePayload;
