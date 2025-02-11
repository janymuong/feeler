import axios from "axios";

const BASE_URL = "http://127.0.0.1:8000/api";

const api = axios.create({
  baseURL: BASE_URL,
});

export const login = (data) => api.post("/token/", data);
export const register = (data) => api.post("/register/", data);
export const predict = (data, token) =>
  api.post("/predict/", data, {
    headers: { Authorization: `Bearer ${token}` },
  });
export const getHistory = (token) =>
  api.get("/history/", {
    headers: { Authorization: `Bearer ${token}` },
  });
export const getVisualization = (token) =>
  api.get("/visualization/", {
    headers: { Authorization: `Bearer ${token}` },
  });
export const logout = (refreshToken, token) =>
api.post(
    "/logout/",
    { refresh_token: refreshToken },
    {
    headers: { Authorization: `Bearer ${token}` },
    }
);
export default api;