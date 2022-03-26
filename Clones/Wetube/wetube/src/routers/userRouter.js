import express from "express";

import { edit, remove, logout, watch } from "../controllers/userController";

const userRouter = express.Router();

userRouter.get("/logout", logout);
userRouter.get("/edit", edit);
userRouter.get("/remove", remove);
userRouter.get("/:id(\\d+)", watch);

export default userRouter;
