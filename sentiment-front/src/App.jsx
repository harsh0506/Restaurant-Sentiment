import React from 'react';
import './App.css'
import HistogramChart from './Charthistogram'
import TextualHeighlights from './TextData';
import MoveGround from './DinoLoadingScree';

const ResNames = [
  { id: 1, name: "Pizza Paradise" },
  { id: 2, name: "shushi Heaven" },
  { id: 3, name: "Burger Joint" },
  { id: 4, name: "Taco Delight" },
  { id: 5, name: "Indian Spice" },
]

function App() {

  const [BarPlotData, setBarPlotData] = React.useState([{ key: [{ count: "", value: "" }] }])
  const [Labels, setLabels] = React.useState()
  const [ResName, setResName] = React.useState(1)
  const [isLoading, setIsLoading] = React.useState(true);

  const result = async () => {
    try {
      const res = await (await fetch(`https://sentimentrestauharshv1.onrender.com/api/getResSpecificData/${ResName}`)).json()
      if (res) {
        setBarPlotData(res[0]);
        setLabels([res[1]]);
        setIsLoading(false);
      } else {
        setIsLoading(true);
      }

    } catch (error) {
      console.log(error)
      setIsLoading(true);
    }
  }

  React.useEffect(() => {
    result()
  }, [ResName])

  return (
    <>

      <div style={{
        display: "flex",
        width: "98vw",
        flexDirection: "row",
        alignItems: "center",
        justifyContent: "center",
        padding: 10,
        margin: 10
      }} className="sm:col-span-3">
        
        <div className="mt-2">
          <select
            style={{
              "fontSize": 25 ,padding:20
            }}
            onChange={(e) => setResName(e.target.value)}
            id="country"
            name="country"
            autoComplete="country-name"
            className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:max-w-xs sm:text-sm sm:leading-6"
          >
            {
              ResNames.map((item) => <option key={item.id} value={item.id}>{item.name}</option>)
            }

          </select>
        </div>
      </div>

      {isLoading ? (
        <MoveGround />
      ) : (
        <>
          <TextualHeighlights data={Labels} />
          <div style={{ width: "98vw" }} className="bg-white">
            <div style={{ paddingTop: 30 }} className="mx-auto max-w-2xl px-4 py-16 sm:px-6 sm:py-24 lg:max-w-7xl lg:px-8">
              <h2 className="sr-only">Products</h2>
              <div className="grid grid-cols-1 gap-x-6 gap-y-10 sm:grid-cols-1 lg:grid-cols-2 xl:grid-cols-2 xl:gap-x-8">
                <HistogramChart data={BarPlotData.ambience} />
                <HistogramChart data={BarPlotData.service} />
                <HistogramChart data={BarPlotData.hygiene} />
                <HistogramChart data={BarPlotData.food} />
              </div>
            </div>
          </div>
        </>
      )}

    </>
  )
}

export default App
