import axios from "axios";
import { BASE_URL } from "./client";

const API = axios.create({
  baseURL: BASE_URL + "/api",
});

export const fetchEvents = () => API.get("/events");
