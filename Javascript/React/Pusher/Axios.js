import axios from "axios";

const instance = axios.create({
	baseURL: "http://localhost:4000", //replace this with heroku when deployings
});

export default instance;
