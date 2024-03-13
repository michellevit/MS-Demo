import React from "react";
import { Route, Routes } from 'react-router-dom';
import Main from "./components/Main";
import "./App.css";

function App() {
  return (
    <div className="app">
      <div className="container">
        <Routes>
          <Route path="/*" element={<Main />} /> 
        </Routes>
      </div>
    </div>
  );
}

export default App;