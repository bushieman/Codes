const functions = require("firebase-functions");
const express = require("express");
const cors = require("cors");
const stripe = require("stripe")(
  "sk_test_51IVytKFaT1g74tpRefqze0GAumQvXc39b0C0UeG8hYGFubOIPRhuIesHJrBnXiz0Tq31Fdf6QuhOmimYe1CwsJer00uty8UfZJ"
);

const app = express();

//middlewares
app.use(cors({ origin: true }));
app.use(express.json());

app.get("/", (request, response) => response.status(200).send("firebase app"));

app.post("/checkout/create", async (req, res) => {
  const total = req.query.total;
  const paymentIntent = await stripe.paymentIntents.create({
    amount: total,
    currency: "usd",
  });
  res.status(201).send({ clientSecret: paymentIntent.client_secret });
});

exports.api = functions.https.onRequest(app);
