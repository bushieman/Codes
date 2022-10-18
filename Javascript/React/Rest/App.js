const cors = require("cors");
const express = require("express");
const Joi = require("joi");
const app = express();
const port = process.env.PORT || 4000;

//middlewares
app.use(express.json());
app.use(cors());

app.use(logger);

const courses = [
  { id: 1, name: "course1" },
  { id: 2, name: "course2" },
  { id: 3, name: "course3" },
  { id: 4, name: "course4" },
  { id: 5, name: "course5" },
];

//getting
app.get("/", (req, res) => {
  res.send("hello");
});

app.get("/courses", auth, (req, res) => {
  res.send("courses");
});

app.get("/courses/:id", (req, res) => {
  const course = courses.find(
    (course) => course.id === parseInt(req.params.id)
  );
  if (!course) return res.status(404).send("course not found");
  res.send(course);
});

//posting
app.post("/courses", (req, res) => {
  //validating
  const newCourse = {
    id: req.body.id,
    name: req.body.name,
  };
  //destructuring
  const { error } = validate(newCourse);
  if (error) return res.status(400).send(error);
  courses.push(newCourse);
  res.send(course);
});

//updating
app.put("/courses", (req, res) => {
  //look up the course
  const course = courses.find(
    (course) => course.id === parseInt(req.params.id)
  );
  if (!course) return res.status(404).send("course not found");
  //validating the course
  const updatedCourse = {
    id: req.body.id,
    name: req.body.name,
  };
  const { error } = validate(updatedCourse);
  if (error) return res.status(400).send(error);
  //updating the course
  course = updatedCourse;
  res.send(course);
});

//deleting
app.delete("/courses", (req, res) => {
  const course = courses.find(
    (course) => course.id === parseInt(req.params.id)
  );
  if (!course) return res.status(404).send("course not found");
  //deleting
  const index = courses.indexOf(course);
  courses.splice(index, 1);
  res.send(course);
});

function logger(req, res, next) {
  console.log("middleware");
  next();
}

function auth(req, res, next) {
  if (req.query.user === "true") return next();
  res.send("no user");
}

function validate(course) {
  const schema = Joi.object({
    id: Joi.number().required(),
    name: Joi.string().min(3).max(30).required(),
  });
  return schema.validate(course);
}

app.listen(port, console.log(`listening on port ${port}`));
