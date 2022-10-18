import mongoose from "mongoose";

const schema = mongoose.Schema({
  name: String,
  message: String,
  timestamp: String,
  received: Boolean
});

export default mongoose.model("messages", schema);
