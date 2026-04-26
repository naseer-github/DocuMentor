const mongoose = require("mongoose");
const bcryptjs = require("bcryptjs");
const dotenv = require("dotenv");
const userModel = require("./models/userModel");

// Load environment variables
dotenv.config();

// Connect to MongoDB
const connectDB = async () => {
  try {
    await mongoose.connect(process.env.MONGO_DB_URI || "mongodb://localhost:27017/docuMentor");
    console.log("MongoDB connected");
  } catch (error) {
    console.error("MongoDB connection error:", error);
    process.exit(1);
  }
};

const createAdminUser = async () => {
  try {
    const adminEmail = "admin@docuMentor.com";
    const adminPassword = "admin123";
    const adminUsername = "Admin";

    // Check if admin already exists
    const existingAdmin = await userModel.findOne({ email: adminEmail });
    if (existingAdmin) {
      console.log("Admin user already exists!");
      console.log("Email:", adminEmail);
      console.log("Password:", adminPassword);
      return;
    }

    // Hash password
    const hashedPassword = await bcryptjs.hash(adminPassword, 8);

    // Create admin user
    const adminUser = new userModel({
      username: adminUsername,
      email: adminEmail,
      password: hashedPassword,
      role: "admin",
      createdAt: Date.now(),
    });

    await adminUser.save();

    console.log("✅ Admin user created successfully!");
    console.log("Email:", adminEmail);
    console.log("Password:", adminPassword);
    console.log("Role: admin");

  } catch (error) {
    console.error("Error creating admin user:", error);
  } finally {
    mongoose.connection.close();
  }
};

// Run the script
connectDB().then(() => {
  createAdminUser();
});