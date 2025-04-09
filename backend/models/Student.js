const mongoose = require("mongoose");

const StudentSchema = new mongoose.Schema({
    name: String,
    email: String,
    testScore: Number,
    percentage: Number,
    skills: [String],
    certifications: [String],
});

module.exports = mongoose.model("Student", StudentSchema);
