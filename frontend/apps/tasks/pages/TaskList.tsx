import React, { useEffect, useState } from 'react';
import { getTasks, createTask, updateTask, deleteTask } from '../services/api';

type Task = {
  id: number;
  title: string;
  completed: boolean;
};

export const TaskList = () => {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [newTitle, setNewTitle] = useState('');

  const loadTasks = () => {
    getTasks().then(setTasks);
  };

  useEffect(() => {
    loadTasks();
  }, []);

  const handleAdd = async () => {
    if (newTitle.trim()) {
      await createTask(newTitle);
      setNewTitle('');
      loadTasks();
    }
  };

  const handleToggle = async (task: Task) => {
    await updateTask(task.id, { completed: !task.completed });
    loadTasks();
  };

  const handleDelete = async (id: number) => {
    await deleteTask(id);
    loadTasks();
  };

  return (
    <div>
      <h1>Task List</h1>
      <input
        type="text"
        value={newTitle}
        onChange={(e) => setNewTitle(e.target.value)}
        placeholder="New task title"
      />
      <button onClick={handleAdd}>Add Task</button>
      <ul>
        {tasks.map((task) => (
          <li key={task.id}>
            <span
              style={{ textDecoration: task.completed ? 'line-through' : 'none', cursor: 'pointer' }}
              onClick={() => handleToggle(task)}
            >
              {task.title}
            </span>
            <button onClick={() => handleDelete(task.id)} style={{ marginLeft: '10px' }}>
              Delete
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
};