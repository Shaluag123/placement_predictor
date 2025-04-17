const mongoose = require("mongoose");

const StudentSchema = new mongoose.Schema({
  name: { type: String, required: true },
  email: { type: String, required: true, unique: true },
  password: { type: String, required: true },
  
  // Extra fields for prediction (optional if student fills after login)
  testScore: { type: Number },
  percentage_10th: { type: Number },
  percentage_12th: { type: Number },
  percentage_grad: { type: Number },
  stream: { type: String },
  college_tier: { type: String },
  internship: { type: String },
  certifications: { type: Number },
  projects: { type: Number },
  skills: { type: String }
});

module.exports = mongoose.model("Student", StudentSchema);
