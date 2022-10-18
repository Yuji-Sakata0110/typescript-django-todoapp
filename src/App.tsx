import React, { useEffect, useState } from 'react';
import './App.css';

import axios from 'axios';
import { API_URL } from "./API.js"

function App() {

  const [text, settext] = useState("");
  const [todos, setTodos] = useState<Todo[]>([]);

  type Todo = {
    id: number;
    text: string;
    completed: boolean;
  };

  //  DB内に保存されている全ての値を表示させる。
  useEffect(() => {
    axios.get(API_URL + "todo_list/")
      .then(res => setTodos(res.data));
  }, []);


  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    settext(e.target.value)
  };

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    // todo  作成
    const newTodo: Todo = {
      id: todos.length,
      text: text,
      completed: false,
    };

    axios.post(API_URL + "create/", newTodo)
      .then(() => {
        console.log("todo created");
      });

    setTodos([newTodo, ...todos]);
    settext("");
  };

  const handleEdit = (id: number, text: string) => {

    const newTodos = todos.map((todo) => {
      if (todo.id === id) {
        todo.text = text;
        // todo の内容を更新。todoはobject型でid, text, compleatedを更新させる。
        axios.post(API_URL + "update/" + todo.id + "/", todo)
          .then(() => {
            console.log("todo Edit updated")
          })
      }
      return todo;
    });

    setTodos(newTodos);
  };

  const handleCheckd = (id: number, completed: boolean) => {

    const newTodos = todos.map((todo) => {
      if (todo.id === id) {
        todo.completed = !completed;
        axios.post(API_URL + "update/" + todo.id + "/", todo)
          .then(() => {
            console.log("todo cheackd updated")
          })
      }
      return todo;
    });

    setTodos(newTodos);

  };

  const handleDelete = (id: number) => {

    // バックグラウンドだけ消す。
    const DelTodos = todos.filter((todo) => {
      if (todo.id === id) {
        axios.delete(API_URL + "delete/" + todo.id + "/")
          .then(() => {
            console.log("todo deleted")
          })
      }
      return todo;
    });

    // 消した結果のtodoリストを読み込む
    const newTodos = todos.filter((todo) => todo.id !== id);
    setTodos(newTodos);
  };


  return (
    <div className="App">
      <h2>Todolist with TypeScript</h2>
      <form action="" onSubmit={(e) => { handleSubmit(e) }}>
        <input type="text" onChange={(e) => { handleChange(e) }} className="inputText" value={text} />
        <input type="submit" value="作成" className="submitButton" />
      </form>
      <ul>
        {todos.map((todo) => (
          <li key={todo.id}>
            <input type="text"
              onChange={(e) => { handleEdit(todo.id, e.target.value) }}
              className="EditText"
              value={todo.text}
              disabled={todo.completed} />
            <input type="checkbox"
              onChange={(e) => { handleCheckd(todo.id, todo.completed) }}
              className="CheckBox" />
            <button onClick={(e) => handleDelete(todo.id)}
              className="DeleteButton">Delete</button>
          </li>
        ))}
      </ul>
    </div>
  )
}

export default App;
