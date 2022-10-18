import axios from "axios";

const instance = axios.create({
  baseURL: "http://localhost:5001/twitter-42874/us-central1/api", //from firebase functions
});

export default instance;
