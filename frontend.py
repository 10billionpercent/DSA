import { useState, useEffect } from "react";

function App() {
  const [field, setField] = useState("");
  const [data, setData] = useState([]);

  // GET DATA
  useEffect(() => {
    fetch("http://localhost:5000/data")
      .then(res => res.json())
      .then(d => setData(d));
  }, []);

  // ADD DATA
  const addItem = async () => {
    await fetch("http://localhost:5000/add", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ field })
    });
    window.location.reload();
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>MERN Expanded Template</h1>

      <input 
        value={field}
        onChange={(e) => setField(e.target.value)}
        placeholder="Enter something"
      />

      <button onClick={addItem}>Add</button>

      <ul>
        {data.map(item => (
          <li key={item._id}>
            {item.field}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;