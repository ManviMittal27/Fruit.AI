import React from 'react';
import { BrowserRouter as Router, Route,  Routes } from 'react-router-dom';
import HomePage from './components/HomePage';
import LoginPage from './components/LoginPage';
import Chat from './components/Chat';
import Translator from './components/Translator';
import FAQ from './components/FAQ';
import AboutPage from './components/About';
import Navbar from './components/Navbar1';

function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" exact component={LoginPage} />
        <Route path="/home" component={HomePage} />
        <Route path="/chat" component={Chat} />
        <Route path="/translator" component={Translator} />
        <Route path="/faq" component={FAQ} />
        <Route path="/about" component={AboutPage} />
      </Routes>
    </Router>
  );
}

export default App;
