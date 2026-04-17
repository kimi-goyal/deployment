import {useEffect, useState} from 'react'

const App = () => {
  const[items, setItems] = useState([])
  useEffect(() => {
    fetch(`${import.meta.env.VITE_API_BASE_URL}/items`)
      .then(res => res.json())
      .then(data => setItems(data))
      .catch(err => console.error(err))
  }, [])
  return (
    
    <div style={{padding:"20px"}}>
      <h1>Items from backend</h1>
      <ul>
        {items.map(item => (
          <li key={item.id}>{item.name}</li>
        ))}
      </ul>
    </div>
  )
}

export default App