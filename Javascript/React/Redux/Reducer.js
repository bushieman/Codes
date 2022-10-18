import { v4 as uuidv4 } from "uuid";

import * as actions from "./ActionTypes";

const initialState = {
  todos: [
    { id: uuidv4(), description: "take out trash", isCompleted: false },
    { id: uuidv4(), description: "visit grandma", isCompleted: false },
    { id: uuidv4(), description: "finish assignment", isCompleted: true },
    { id: uuidv4(), description: "do laundry", isCompleted: false },
    {
      id: uuidv4(),
      description: "research on trending stocks",
      isCompleted: true,
    },
  ],
};

export default function reducer(state = initialState, action) {
  switch (action.type) {
    case actions.addTodo: {
      return {
        ...state,
        todos: [...state.todos, action.todo],
      };
    }

    case actions.deleteTodo: {
      const newTodos = state.todos.filter((todo) => {
        return todo.id !== action.id;
      });
      return {
        ...state,
        todos: newTodos,
      };
    }

    default:
      return state;
  }
}
