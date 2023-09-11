import React from 'react';
import './App.css'
import FormComp from './Form';
import DataAnalytics from './DataAnalytics';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Error from './Error';

function App() {

  return (
    <>
       <BrowserRouter>
        <Routes>
          <Route path="/" element={<DataAnalytics />} />
          <Route path="/form" element={<FormComp />} />
          <Route path="/Error" element={<Error/>} />
         
        </Routes>
      </BrowserRouter>
      
    </>
  )
}

export default App
