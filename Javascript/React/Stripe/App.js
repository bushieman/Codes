import React from "react";
import { loadStripe } from "@stripe/stripe-js";
import { Elements } from "@stripe/react-stripe-js";

import Checkout from "./Checkout";
import Products from "./Products";

const stripe = loadStripe(
  "pk_test_51IVytKFaT1g74tpRdSkYBRvazh9CD2tuRoW5UGjjdmhj8LAKL5qQsznAU136npBmGq0VOMIaKE1iPDT3fYLtBUw100SndZVNUJ"
);

function App() {
  return (
    <div>
      <Products />
      <Elements stripe={stripe}>
        <Checkout />
      </Elements>
    </div>
  );
}

export default App;
