import firebase from "firebase";

const firebaseConfig = {
  apiKey: "AIzaSyBB-7A9I50hiC8y9ohnyeW4_rzhBb6Sytw",
  authDomain: "twitter-42874.firebaseapp.com",
  databaseURL: "https://twitter-42874.firebaseio.com",
  projectId: "twitter-42874",
  storageBucket: "twitter-42874.appspot.com",
  messagingSenderId: "936146875849",
  appId: "1:936146875849:web:52439c0cce6f027fe9a418",
  measurementId: "G-09NLZGWJ87",
};

const firebaseApp = firebase.initializeApp(firebaseConfig);
const db = firebaseApp.firestore();
const auth = firebase.auth();
const provider = new firebase.auth.GoogleAuthProvider();
const analytics = firebase.analytics();

export { auth, provider, firebaseApp, analytics, db };
