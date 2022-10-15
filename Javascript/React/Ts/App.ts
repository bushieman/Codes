// enum
enum Color {
  black = "000",
  white = "#FFFFFF",
}
let backgroundColor = Color.white;

// type assertions
let word: string;
let points: number;
let choice: boolean;
let summary: any;

// dynamic type assertions
let message;
message = "hi";
let sentMessage = (<string>message).endsWith("hi");

// class instances
class Point {
  constructor(private _x?: number, private _y?: number) {}

  getDistance() {
    console.log(this._y - this._x);
  }

  // getter
  get x() {
    return this._x;
  }

  // setter
  set x(value) {
    this._x = value;
  }

  get y() {
    return this._y;
  }

  set y(value) {
    this._y = value;
  }
}

let point = new Point(10);
point.y = 20;
let pointX = point.x;
let pointY = point.y;
console.log(pointX, pointY);
point.getDistance();
