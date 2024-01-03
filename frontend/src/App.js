// Filename - App.js

// Importing modules
import React, { useState, useEffect } from "react";
import "./App.css";

function App() {
  const [isValid, setIsValid] = useState("unknown");

  const cw = "111111111";

  useEffect(() => {
    fetch("http://127.0.0.1:8000/validcw", {
      method: "POST",
      "headers": {"Content-Type": "application/json"},
      body: JSON.stringify({ cw: cw }),
    }).then((res) =>
      res.json().then((data) => {
        console.log(data);
        setIsValid(data.isValid);
      })
    );
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>React and flask</h1>
        {/* Calling a data from setdata for showing */}
        <p>{isValid.toString()}</p>
        <p>{cw}</p>
      </header>
    </div>
  );
}

export default App;
