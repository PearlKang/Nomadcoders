import express from "express";

import {
  getEdit,
  postEdit,
  logout,
  watch,
  startGithubLogin,
  finishGithubLogin,
} from "../controllers/userController";

import { protectorMiddleware } from "../middlewares";

const userRouter = express.Router();

userRouter.get("/logout", protectorMiddleware, logout);
userRouter
  .route("/edit")
  .get(protectorMiddleware, getEdit)
  .post(protectorMiddleware, postEdit);
userRouter.get("/github/start", startGithubLogin);
userRouter.get("/github/finish", finishGithubLogin);
userRouter.get("/:id(\\d+)", watch);

export default userRouter;
