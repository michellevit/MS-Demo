import React from "react";
import { Route, Routes } from 'react-router-dom'; 
import "./App.css";
import Main from './components/Main';

function App() {
  return (
    <div className="app">
      <div className="container">
        <Routes>
          <Route path="/" element={<Main />} /> 
        </Routes>
      </div>
    </div>
  );
}

export default App;