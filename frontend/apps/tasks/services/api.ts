import axios from 'axios';

const API_URL = 'http://localhost:8000/tasks';

export const getTasks = async () => {
  const response = await axios.get(API_URL);
  return response.data;
};

export const createTask = async (title: string) => {
  const response = await axios.post(API_URL, { title });
  return response.data;
};

export const updateTask = async (id: number, data: { title?: string; completed?: boolean }) => {
  const response = await axios.put(`${API_URL}/${id}`, data);
  return response.data;
};

export const deleteTask = async (id: number) => {
  await axios.delete(`${API_URL}/${id}`);
};