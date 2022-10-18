import React, { useEffect, useState } from "react";
import Pusher from "pusher-js";

import axios from "./Axios";

function Main() {
	const [messages, setMessages] = useState([]);
	const [user, setUser] = useState("");
	const [newMessage, setNewMessage] = useState("");

	useEffect(() => {
		axios.get("/messages/sync").then((response) => {
			setMessages(response.data);
		});
	}, []);

	useEffect(() => {
		var pusher = new Pusher("520ab2b3bec6fff9f8d3", {
			cluster: "eu",
		});

		var channel = pusher.subscribe("messages");
		channel.bind("inserted", (data) => {
			setMessages([...messages, data]);
		});

		return () => {
			channel.unbind_all();
			channel.unsubscribe();
		};
	}, [messages]);

	const newMessageItem = {
		message: newMessage,
		timestamp: new Date().toUTCString(),
		name: user ? user : "guest",
		received: false,
	};

	const handleSubmit = (e) => {
		e.preventDefault();
		axios.post("/messages/new", newMessageItem);
		setNewMessage("");
	};

	return (
		<div className="main">
			<div className="messages">
				{messages?.map((message) => (
					<div
						className={`message__item ${
							!message.received ? "sent" : "received"
						}`}
					>
						<strong>{message.name}</strong>
						<span>{message.timestamp}</span>
						<p>{message.message}</p>
					</div>
				))}
			</div>
			<form onSubmit={handleSubmit}>
				<input
					type="text"
					placeholder="Enter your text here..."
					value={newMessage}
					onChange={(e) => setNewMessage(e.target.value)}
				/>
			</form>
		</div>
	);
}

export default Main;
