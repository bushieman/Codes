const functions = require("firebase-functions");
const admin = require("firebase-admin");
const algoliasearch = require("algoliasearch");
const faker = require("faker");

admin.initializeApp();
const db = admin.firestore();

//adding some data to the cloud
const fakeIt = () => {
	return db.collection("customers").add({
		username: faker.internet.userName(),
		email: faker.internet.email(),
		avatar: faker.internet.avatar(),
		bio: faker.hacker.phrase(),
		color: faker.commerce.color(),
	});
};
Array(20).fill(0).forEach(fakeIt);

//connecting to algolia
const client = algoliasearch("8PU2WDR4HM", "de2aac149a9c6f99560662c696f667f8");
const index = client.initIndex("customers");

//updating algolia
exports.addToIndex = functions.firestore
	.document("customers/{customerId}")
	.onCreate((snapshot) => {
		const data = snapshot.data();
		console.log("this is the data", data);
		const objectID = snapshot.id;

		return index.saveObject({ ...data, objectID });
	});
exports.updateIndex = functions.firestore
	.document("customers/{customerId}")

	.onUpdate((change) => {
		const newData = change.after.data();
		const objectID = change.after.id;
		return index.saveObject({ ...newData, objectID });
	});

exports.deleteFromIndex = functions.firestore
	.document("customers/{customerId}")

	.onDelete((snapshot) => index.deleteObject(snapshot.id));
