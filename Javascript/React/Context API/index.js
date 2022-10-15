import React from "react";
import ReactDOM from "react-dom";
import App from "./App";
import reportWebVitals from "./reportWebVitals";
import reducer, { initialState } from "./Reducer";
import { Context } from "./Context";

ReactDOM.render(
  <React.StrictMode>
    <Context initialState={initialState} reducer={reducer}>
      <App />
    </Context>
  </React.StrictMode>,
  document.getElementById("root")
);

reportWebVitals();
