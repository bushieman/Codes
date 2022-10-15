import * as actions from "./ActionTypes";

export const initialState = {
  user: [],
};
const reducer = (state, action) => {
  switch (action.type) {
    case actions.setUser:
      return {
        ...state,
        user: [...state.user, action.user],
      };
    default:
      return state;
  }
};

export default reducer;
