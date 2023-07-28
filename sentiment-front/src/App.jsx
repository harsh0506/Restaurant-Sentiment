import { useState, useEffect } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [food, setFood] = useState(1);
  const [ambience, setAmbience] = useState(1);
  const [hygiene, setHygiene] = useState(1);
  const [service, setService] = useState(1);
  const [comment, setComment] = useState('');
  const [sentiment, setSentiment] = useState(null);
  const [isFetching, setIsFetching] = useState(false);
  const [formError, setFormError] = useState(null);

  useEffect(() => {
    if (food && ambience && hygiene && service && comment) {
      setFormError(null);
    }
  }, [food, ambience, hygiene, service, comment]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (food && ambience && hygiene && service && comment) {
      setIsFetching(true);
      try {
        const response = await fetch('/api/sentiment', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            food,
            ambience,
            hygiene,
            service,
            comment,
          }),
        });
        const data = await response.json();
        setSentiment(data.sentiment);
        setIsFetching(false);
      } catch (error) {
        console.error('Error fetching data:', error);
        setFormError('Error occurred while fetching data. Please try again.');
        setIsFetching(false);
      }
    } else {
      setFormError('Please fill in all the fields.');
    }
  };

  return (
    <div style={{
      display: "flex",
      alignItems: "center",
      width:"100vw",height:"100vh",
      justifyContent: "center"
    }} className="flex  items-center justify-center min-h-screen bg-gray-100">


      {/* Left */}
      <div style={{width:"50%"}} className="flex w-full max-w-md">
        <h2 className="text-2xl font-bold mb-4">Give Feedback</h2>
        <form onSubmit={handleSubmit} className="space-y-4">
          <div className="grid grid-cols-2 gap-4">

            <div style={{
              display: "grid",
              gridTemplateColumns: "repeat(2, 1fr)",
              gridTemplateRows: "repeat(2, 1fr)",
              margin: 0,
              padding: 0,
            }}>
              <div style={{padding: 20}}>
                <label className="block">Food:</label>
                <select
                  value={food}
                  onChange={(e) => setFood(e.target.value)}
                  className="w-full bg-white border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-300"
                >
                  {Array.from({ length: 5 }, (_, i) => i + 1).map((num) => (
                    <option key={num} value={num}>
                      {num}
                    </option>
                  ))}
                </select>
              </div>
              <div style={{padding: 20}}>
                <label className="block">Ambience:</label>
                <select
                  value={ambience}
                  onChange={(e) => setAmbience(e.target.value)}
                  className="w-full bg-white border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-300"
                >
                  {Array.from({ length: 5 }, (_, i) => i + 1).map((num) => (
                    <option key={num} value={num}>
                      {num}
                    </option>
                  ))}
                </select>
              </div>
              <div style={{padding: 20}}>
                <label className="block">Hygiene:</label>
                <select
                  value={hygiene}
                  onChange={(e) => setHygiene(e.target.value)}
                  className="w-full bg-white border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-300"
                >
                  {Array.from({ length: 5 }, (_, i) => i + 1).map((num) => (
                    <option key={num} value={num}>
                      {num}
                    </option>
                  ))}
                </select>
              </div>
              <div style={{padding: 20}}>
                <label className="block">Service:</label>
                <select
                  value={service}
                  onChange={(e) => setService(e.target.value)}
                  className="w-full bg-white border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-300"
                >
                  {Array.from({ length: 5 }, (_, i) => i + 1).map((num) => (
                    <option key={num} value={num}>
                      {num}
                    </option>
                  ))}
                </select>
              </div>
            </div>

            <div>
              <label className="block">Comment:</label>
              <input
                type="text"
                value={comment}
                onChange={(e) => setComment(e.target.value)}
                className="w-full bg-white border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-300"
              />
            </div>

          </div>
          {formError && <p className="text-red-500">{formError}</p>}
          <button
            type="submit"
            disabled={isFetching}
            className="w-full bg-blue-500 text-white rounded-md py-2 px-4 hover:bg-blue-600 focus:outline-none focus:ring focus:ring-blue-300"
          >
            {isFetching ? 'Sending...' : 'Submit'}
          </button>
        </form>

      </div>


      { /* Right */}
      <div style={{width:"50%"}} >
        <h3 className="text-2xl font-bold mt-4">Sentiment Analysis:</h3>
        {isFetching ? (
          <p>Loading sentiment...</p>
        ) : sentiment === null ? (
          <p>Please fill in all the fields to get the sentiment.</p>
        ) : sentiment === 1 ? (
          <p>Positive Sentiment</p>
        ) : (
          <p>Negative Sentiment</p>
        )}
      </div>
    </div>

  );
}

export default App
