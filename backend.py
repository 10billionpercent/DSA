const express = require("express");
const mongoose = require("mongoose");
const cors = require("cors");

const app = express();

// MIDDLEWARE (Very important)
app.use(express.json());  // lets backend read req.body
app.use(cors());          // lets React talk to backend


// 1️⃣ CONNECT TO MONGODB
mongoose.connect("mongodb://127.0.0.1:27017/examdb", {
    useNewUrlParser: true,
    useUnifiedTopology: true
})
.then(() => console.log("MongoDB connected ✔"))
.catch(err => console.log("Mongo error:", err));


// 2️⃣ SCHEMA — blueprint of each document
const ItemSchema = new mongoose.Schema({
    field: { type: String, required: true },  // you can add multiple fields too
    createdAt: { type: Date, default: Date.now } // optional field to show power
});


// 3️⃣ MODEL — actual collection + functions
const Item = mongoose.model("Item", ItemSchema);


// 4️⃣ CREATE — POST request
app.post("/add", async (req, res) => {
    try {
        const item = new Item({ field: req.body.field });
        await item.save();  // save to Mongo
        res.json({ status: "saved", item });
    } catch (err) {
        res.json({ status: "error", message: err.message });
    }
});


// 5️⃣ READ — GET request
app.get("/data", async (req, res) => {
    try {
        const items = await Item.find(); // get everything
        res.json(items);
    } catch (err) {
        res.json({ status: "error", message: err.message });
    }
});


// 6️⃣ UPDATE — PUT request (optional but shows POWER)
app.put("/update/:id", async (req, res) => {
    try {
        const updated = await Item.findByIdAndUpdate(
            req.params.id,
            { field: req.body.field },
            { new: true }
        );
        res.json({ status: "updated", updated });
    } catch (err) {
        res.json({ status: "error", message: err.message });
    }
});


// 7️⃣ DELETE — DELETE request
app.delete("/delete/:id", async (req, res) => {
    try {
        await Item.findByIdAndDelete(req.params.id);
        res.json({ status: "deleted" });
    } catch (err) {
        res.json({ status: "error", message: err.message });
    }
});


// SERVER LISTENING
app.listen(5000, () => console.log("Server running on port 5000 🚀"));