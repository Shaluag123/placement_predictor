const express = require("express");
const router = express.Router();
const Student = require("../models/Student");

// POST: Save Student Data
router.post("/", async (req, res) => {
    try {
        const student = new Student(req.body);
        await student.save();
        res.status(201).json(student);
    } catch (error) {
        res.status(500).json({ error: "Error saving student data" });
    }
});

// GET: Fetch all Students
router.get("/", async (req, res) => {
    try {
        const students = await Student.find();
        res.json(students);
    } catch (error) {
        res.status(500).json({ error: "Error fetching students" });
    }
});

module.exports = router;
