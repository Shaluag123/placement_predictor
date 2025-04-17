const express = require("express");
const mongoose = require("mongoose");
const cors = require("cors");
require("dotenv").config();

const app = express();
app.use(express.json());
app.use(cors());

// MongoDB Connection
mongoose.connect(process.env.MONGO_URI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log("✅ MongoDB connected"))
    .catch(err => console.log("❌ MongoDB error:", err));

// Routes
app.use("/api/students", require("./routes/studentRoutes")); // student signup/login
app.use("/api/admin", require("./routes/adminRoutes"));
app.use("/api/predict", require("./routes/predictRoutes"));
 // admin login

app.listen(5000, () => console.log("🚀 Server running on port 5000"));
