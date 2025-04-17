const express = require('express');
const router = express.Router();

const ADMIN_EMAIL = "admin@nextstep.com";
const ADMIN_PASS = "admin123";

router.post('/login', (req, res) => {
  const { email, password } = req.body;
  if (email === ADMIN_EMAIL && password === ADMIN_PASS) {
    return res.status(200).json({ message: "Admin login successful" });
  } else {
    return res.status(401).json({ message: "Invalid admin credentials" });
  }
});

module.exports = router;
