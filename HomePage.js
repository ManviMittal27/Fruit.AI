import React from 'react';
import { Link } from 'react-router-dom';

const HomePage = () => {
  return (
    <div>
      <h1>Home Page</h1>
      <ul>
        <li>
          <Link to="/chat">Chat</Link>
        </li>
        <li>
          <Link to="/translator">Translator</Link>
        </li>
        <li>
          <Link to="/faq">FAQ</Link>
        </li>
        <li>
          <Link to="/about">About</Link>
        </li>
      </ul>
    </div>
  );
};

export default HomePage;