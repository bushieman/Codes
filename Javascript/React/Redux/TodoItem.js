import React, { useState } from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faTrash } from "@fortawesome/free-solid-svg-icons";
import { connect } from "react-redux";

import "./TodoItem.css";
import * as actions from "./ActionTypes";

function TodoItem({ deleteTodo, todo, id }) {
  const [completed, setCompleted] = useState(false);

  const markComplete = (e) => {
    setCompleted(!completed);
  };

  return (
    <div className="todo__item">
      <div>
        <input type="checkbox" className="myinput" onChange={markComplete} />
      </div>
      <div>
        <h2 className={`${completed ? "new__style" : ""}`}>
          {todo.description}
        </h2>
      </div>
      <FontAwesomeIcon
        icon={faTrash}
        style={{ fontSize: "16px" }}
        onClick={() => deleteTodo(id)}
        value={id}
      />
    </div>
  );
}

const mapDispatchToProps = (dispatch) => {
  return {
    deleteTodo: (id) => dispatch({ type: actions.deleteTodo, id }),
  };
};

// when there's no dispatch action, no need to use null. you can just use mapStateToProps alone
export default connect(null, mapDispatchToProps)(TodoItem);
