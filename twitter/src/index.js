import React from "react";
import ReactDOM from "react-dom";
import App from "./components/App";
import firebase from "./firebase";
console.log("app");

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);