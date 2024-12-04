<template>
  <div>
    <h1>Ma To-Do List</h1>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      todos: [],
      newTask: '',
    };
  },
  methods: {
    async fetchTodos() {
      const response = await axios.get('http://localhost:3000/api/todos');
      this.todos = response.data;
    },
    async addTodo() {
      if (this.newTask.trim()) {
        const response = await axios.post('http://localhost:3000/api/todos', {
          task: this.newTask,
        });
        this.todos.push(response.data);
        this.newTask = '';
      }
    },
  },
  mounted() {
    this.fetchTodos();
  },
};
</script>
