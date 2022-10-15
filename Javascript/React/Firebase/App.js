import React, { useState } from "react";
import { useHistory } from "react-router";

import { auth, provider } from "./Firebase";

function App() {
	const history = useHistory();
	const [email, setEmail] = useState("");
	const [password, setPassword] = useState("");

	const handleSignUp = () => {
		auth.createUserWithEmailAndPassword(email, password).then((user) => {
			if (user) {
				history.push("/workspace");
				console.log("signup successfull");
			} else {
				console.log("user already exists ,sign in instead");
			}
		});
	};

	const handleSignIn = () => {
		auth.signInWithEmailAndPassword(email, password).then((user) => {
			if (user) {
				history.push("/workspace");
				console.log("signin successfull");
			} else {
				console.log("don't have an account? Sign up instead");
			}
		});
	};

	const handleSignInGoogle = () => {
		auth.signInWithPopup(provider).then((user) => {
			if (user) {
				history.push("/workspace");
				console.log("signin with google successfull");
			} else {
				console.log("don't have an account? Sign up instead");
			}
		});
	};

	return (
		<div>
			<input
				type="text"
				placeholder="email"
				value={email}
				onChange={(e) => setEmail(e.target.value)}
			/>
			<input
				type="text"
				placeholder="password"
				value={password}
				onChange={(e) => setPassword(e.target.value)}
			/>
			<button onClick={handleSignUp}>Sign up</button>
			<button onClick={handleSignIn}>Sign in</button>
			<button onClick={handleSignInGoogle}>Sign in with Google</button>
		</div>
	);
}

export default App;
