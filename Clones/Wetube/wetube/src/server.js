import express from "express";

const PORT = 4000;

const app = express();
/*
app.listen(4000, () => console.log("Server listening on port 4000 🚀"));
*/
const handleListening = () =>
  console.log(`✔ Server listening on port http://localhost:${PORT} 🚀`);

app.listen(PORT, handleListening);
