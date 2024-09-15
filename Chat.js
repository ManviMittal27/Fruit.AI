import React from 'react';
import { useState } from 'react';

const Chat = () => {
  const [fruits, setFruits] = useState([
    { id: 1, name: 'Apple' },
    { id: 2, name: 'Banana' },
    { id: 3, name: 'Cherry' },
  ]);

  return (
    <div>
      <h1>Chat</h1>
      <ul>
        {fruits.map((fruit) => (
          <li key={fruit.id}>
            <h2>{fruit.name}</h2>
            <p>Fruit details here</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Chat;