import { v4 as uuidv4 } from "uuid";
import { connect } from "react-redux";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faEllipsisV, faUser, faCog } from "@fortawesome/free-solid-svg-icons";
import { faCalendarAlt } from "@fortawesome/free-regular-svg-icons";
import React, { useState } from "react";

import "./App.css";
import "./css/all.css";
import * as actions from "./ActionTypes";
import TodoItem from "./TodoItem";

function App({ myTodos, addTodo }) {
  const [newTodo, setNewTodo] = useState("");

  const addTodoItem = (e) => {
    e.preventDefault();
    addTodo(newTodo);
    setNewTodo("");
  };

  const deleteItem = () => {
    console.log("deleting items");
  };

  return (
    <div>
      <div className="app">
        <div className="main">
          <div className="main__left">
            <div className="header">Todo List</div>
            <div className="todolist">
              {myTodos?.map((todo) => (
                <TodoItem todo={todo} key={todo.id} id={todo.id} />
              ))}
            </div>
            <div className="textarea">
              <form onSubmit={addTodoItem}>
                <input
                  type="text"
                  placeholder="gimme something..."
                  value={newTodo}
                  onChange={(e) => setNewTodo(e.target.value)}
                />
              </form>
              <button className="input__button" onClick={addTodoItem}>
                add
              </button>
            </div>
          </div>
          <div className="main__right">
            <div className="sub__menu">
              <FontAwesomeIcon icon={faUser} style={{ marginRight: "20px" }} />
              <FontAwesomeIcon icon={faCog} style={{ marginRight: "20px" }} />
              <FontAwesomeIcon
                icon={faCalendarAlt}
                style={{ marginRight: "20px" }}
              />
              <FontAwesomeIcon
                icon={faEllipsisV}
                style={{ marginRight: "20px" }}
              />
            </div>
            <div className="calendar">some app</div>
          </div>
        </div>
      </div>
    </div>
  );
}

const mapStateToProps = (state) => {
  return {
    myTodos: state.todos,
  };
};

const mapDispatchToProps = (dispatch) => {
  return {
    addTodo: (description) =>
      dispatch({
        type: actions.addTodo,
        todo: {
          id: uuidv4(),
          description,
          isCompleted: false,
        },
      }),
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(App);
