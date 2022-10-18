// interfaces
var Point = /** @class */ (function () {
    function Point(_x, _y) {
        this._x = _x;
        this._y = _y;
    }
    Point.prototype.getDistance = function () {
        console.log(this._y - this._x);
    };
    Object.defineProperty(Point.prototype, "x", {
        // getter
        get: function () {
            return this._x;
        },
        // setter
        set: function (value) {
            this._x = value;
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(Point.prototype, "y", {
        get: function () {
            return this._y;
        },
        set: function (value) {
            this._y = value;
        },
        enumerable: false,
        configurable: true
    });
    return Point;
}());
var point = new Point(10);
point.y = 20;
var pointX = point.x;
var pointY = point.y;
console.log(pointX, pointY);
point.getDistance();
