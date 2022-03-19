import express from "express";

const PORT = 4000;

const app = express();

const logger = (req, res, next) => {
  console.log(`${req.method} ${req.url}`);
  next();
};

//cosnt handelHome = (req, res) => res.end();
const handleHome = (req, res) => {
  return res.send("I love middlewares");
};

app.use(logger);
app.get("/", handleHome);

const handleListening = () =>
  console.log(`✔ Server listening on port http://localhost:${PORT} 🚀`);

app.listen(PORT, handleListening);
