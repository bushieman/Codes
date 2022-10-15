import React, { useEffect, useState } from "react";
import { CardElement, useElements, useStripe } from "@stripe/react-stripe-js";
import { useHistory } from "react-router-dom";
import styled from "styled-components";

import { getBasketTotal } from "./Reducer";
import { useStateValue } from "./Context";
import axios from "./Axios";
import * as actions from "./ActionTypes";

const Button = styled.button`
  background-color: aqua;
  border-radius: 5px;
  border-color: aqua;
  border-width: 1px;
  border-style: solid;
  padding-top: 10px;
  padding-bottom: 10px;
  padding-left: 20px;
  padding-right: 20px;
  font-size: 12px;
  font-weight: bold;
`;

function Checkout() {
  const history = useHistory();
  const [{ basket }, dispatch] = useStateValue();
  const [error, setError] = useState(null);
  const [disabled, setDisabled] = useState(true);
  const [succeded, setSucceeded] = useState(false);
  const [processing, setProcessing] = useState(true);
  const [clientSecret, setClientSecret] = useState("");
  const stripe = useStripe();
  const elements = useElements();

  useEffect(() => {
    const getClientSecret = async () => {
      const response = await axios({
        method: "POST",
        url: `/checkout/create?total=${getBasketTotal(basket) * 100}`,
      });
      setClientSecret(response.data.clientSecret);
    };
    getClientSecret();
  }, [basket]);

  const handleChange = async (e) => {
    setDisabled(e.empty);
    setError(e.error ? e.error.message : "");
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    const payload = await stripe.confirmCardPayment(clientSecret, {
      payment_method: {
        card: elements.getElement(CardElement),
      },
    });
    // handling orders in firestore
    //   .then(({ paymentIntent }) => {
    //     db.collection("users")
    //       .doc(reduxUser?.uid)
    //       .collection("orders")
    //       .doc(paymentIntent.id)
    //       .set({
    //         basket: reduxBasket,
    //         amount: paymentIntent.amount,
    //         created: paymentIntent.created,
    //       });
    setSucceeded(true);
    setError(null);
    setProcessing(false);
    dispatch({
      type: actions.emptyBasket,
    });
    history.replace("/orders"); //redirecting to my orders
  };
  return (
    <div>
      <p>this is the checkout</p>
      <span>{getBasketTotal(basket)}</span>
      <form onSubmit={handleSubmit}>
        <CardElement onChange={handleChange} />
      </form>
      <Button disabled={disabled || processing || succeded}>checkout</Button>
    </div>
  );
}

export default Checkout;
