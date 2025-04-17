const express = require('express');
const router = express.Router();
const {
  registerStudent,
  loginStudent,
  getStudentProfile
} = require('../controllers/studentController');
const verifyToken = require('../middleware/authMiddleware');

// Public
router.post('/register', registerStudent);
router.post('/login', loginStudent);

// Protected
router.get('/me', verifyToken, getStudentProfile);

module.exports = router;
