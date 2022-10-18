import React from "react";
import styled from "styled-components";

import { useStateValue } from "./Context";
import * as actions from "./ActionTypes";

const Button = styled.button`
  padding: 30px;
  background-color: crimson;
  border: none;
  border-radius: 5px;
`;

const Summary = styled.p`
  color: tomato;
  font-size: 12px;
  font-weight: bold;
`;

function App() {
  const [{ user }, dispatch] = useStateValue();

  const handleClick = () => {
    dispatch({
      type: actions.setUser,
      user: "bushie",
    });
  };

  return (
    <div>
      <h1>{user}</h1>
      <Summary>This is a tutorial on the use of git and github</Summary>
      <Button onClick={handleClick}>add item</Button>
    </div>
  );
}

export default App;
