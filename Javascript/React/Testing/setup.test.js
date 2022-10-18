import React from "react";
import { shallow, mount } from "enzyme";
import Enzyme from "enzyme";
import toJson from "enzyme-to-json";
import Adapter from "@wojtekmaj/enzyme-adapter-react-17";

Enzyme.configure({ adapter: new Adapter() });

//react 16 adapter setup
// import Adapter from "enzyme-adapter-react-16";
//import configure from "enzyme"
// configure({ adapter: new Adapter() });

import App from "./App";
import Items from "./Items";

const message = "this is the item component";
const initialValue = 0;

//handling render
describe("rendering components", () => {
  it("rendering the app component", () => {
    shallow(<App />);
  });
  it("rendering the items component", () => {
    shallow(<Items />);
  });
  it("rendering the items component in app", () => {
    const wrapper = shallow(<App />);
    const child = <Items message={message} initialValue={initialValue} />;
    expect(wrapper.contains(child)).toEqual(true);
  });
  it("rendering the header ", () => {
    const wrapper = shallow(<App />);
    const header = <span>this is my header</span>;
    expect(wrapper.contains(header)).toEqual(true);
  });
  it("renders the header ", () => {
    const wrapper = mount(<Items message={message} />);
    const buttons = wrapper.find("#header").text();
    expect(buttons).toEqual(message);
  });

  it("renders the increment buttons ", () => {
    const wrapper = mount(<Items />);
    const buttons = wrapper.find("#addButton").hostNodes().text();
    expect(buttons).toEqual("+");
  });
  it("renders the decrement buttons ", () => {
    const wrapper = mount(<Items />);
    const buttons = wrapper.find("#minusButton").hostNodes().text();
    expect(buttons).toEqual("-");
  });
});

//hendling props
describe("passing props", () => {
  const wrapper = mount(<Items message={message} />);
  it("renders props", () => {
    expect(wrapper.props().message).toEqual(message);
  });
});

//handling logic
describe("increment onclick events", () => {
  const wrapper = mount(<Items initialValue={initialValue} />);
  wrapper.find("#addButton").hostNodes().simulate("click");
  it("updates count", () => {
    const count = wrapper.find("#count").text();
    const expectedCount = initialValue + 1;
    //couldn't figure out the issue with toequal not working as default
    expect(count).toEqual(`${expectedCount}`);
  });
  it("updates value", () => {
    const value = wrapper.find("#value").text();
    const expectedValue = initialValue + 50;
    //same case as here
    expect(value).toEqual(`${expectedValue}`);
  });
});

describe("snapshots", () => {
  it("app snapshots", () => {
    const tree = shallow(<App />);
    expect(toJson(tree)).toMatchSnapshot();
  });
  it("item snapshots", () => {
    const tree = shallow(
      <Items message={message} initialValue={initialValue} />
    );
    expect(toJson(tree)).toMatchSnapshot();
  });
});
