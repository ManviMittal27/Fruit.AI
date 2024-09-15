import React, { useState, useEffect } from 'react';
import axios from 'axios';

const FaQ = () => {
  const [faqs, setFaqs] = useState([]);
  const [newFaQ, setNewFaQ] = useState('');
  const [error, setError] = useState(null);

  useEffect(() => {
    axios.get('/api/faqs')
      .then((response) => {
        setFaqs(response.data);
      })
      .catch((error) => {
        setError(error.message);
      });
  }, []);

  const handleCreateFaQ = async () => {
    try {
      const response = await axios.post('/api/faqs', { faq: newFaQ });
      setFaqs([...faqs, response.data]);
      setNewFaQ('');
    } catch (error) {
      setError(error.message);
    }
  };

  return (
    <div>
      <h1>FAQ</h1>
      <ul>
        {faqs.map((faq) => (
          <li key={faq.id}>
            <h2>{faq.question}</h2>
            <p>{faq.answer}</p>
          </li>
        ))}
      </ul>
      <input type="text" value={newFaQ} onChange={(event) => setNewFaQ(event.target.value)} />
      <button onClick={handleCreateFaQ}>Create FAQ</button>
      {error && <div style={{ color: 'red' }}>{error}</div>}
    </div>
  );
};

export default FaQ;