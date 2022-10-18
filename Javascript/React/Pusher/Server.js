import cors from "cors";
import express from "express";
import mongoose from "mongoose";
import Pusher from "pusher";
const port = process.env.PORT || 4000;

import Messages from "./Message.js";

const app = express();

const mongoUrl =
	"mongodb+srv://admin:sansasnow@cluster0.10qe7.mongodb.net/chatdb?retryWrites=true&w=majority";
const pusher = new Pusher({
	appId: "1141501",
	key: "520ab2b3bec6fff9f8d3",
	secret: "881bba51e13f9efc0b77",
	cluster: "eu",
	useTLS: true,
});

app.use(express.json());
app.use(cors());

//getting
app.get("/", (req, res) => {
	res.status(200).send("hello world");
});

app.get("/messages/sync", (req, res) => {
	Messages.find((err, data) => {
		if (err) return res.status(500).send(err);
		res.status(200).send(data);
	});
});

//posting
app.post("/messages/new", (req, res) => {
	//testing with postman
	const dbMessages = req.body;

	Messages.create(dbMessages, (err, data) => {
		if (err) return res.status(500).send(err);
		res.status(201).send(data);
	});
});

//connecting to mongoDB
mongoose.connect(mongoUrl, {
	useCreateIndex: true,
	useNewUrlParser: true,
	useUnifiedTopology: true,
});

//triggering pusher
const db = mongoose.connection;
db.once("open", () => {
	console.log("connected to db");

	const msgCollection = db.collection("messages");
	const changeStream = msgCollection.watch();

	changeStream.on("change", (change) => {
		const messageDetails = change.fullDocument;
		if (change.operationType === "insert") {
			pusher.trigger("messages", "inserted", {
				name: messageDetails.name,
				message: messageDetails.message,
				timestamp: messageDetails.timestamp,
				received: messageDetails.received,
			});
		} else {
			console.log("error triggering pusher");
		}
	});
});

app.listen(port, console.log(`listening on port${port}...`));
