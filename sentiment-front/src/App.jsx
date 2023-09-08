import React from 'react';
import './App.css'
import HistogramChart from './Charthistogram'
import TextualHeighlights from './TextData';

const data = [
  { rating: 'Rating 1', count: 5 },
  { rating: 'Rating 2', count: 8 },
  { rating: 'Rating 3', count: 15 },
  { rating: 'Rating 4', count: 10 },
  { rating: 'Rating 5', count: 20 },
];

function App() {

  const [BarPlotData, setBarPlotData] = React.useState([{ key: [{ count: "", value: "" }] }])

  const result = async () => {
    try {
      const res = await (await fetch("http://localhost:5000/api/getResSpecificData/1")).json()
      setBarPlotData(res[0])
      console.log(res)
    } catch (error) {
      console.log(error)
    }
  }

  React.useEffect(() => {
    result()
  }, [])

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
        <label htmlFor="country" className="block text-sm font-medium leading-6 text-gray-900">

        </label>
        <div className="mt-2">
          <select
            id="country"
            name="country"
            autoComplete="country-name"
            className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:max-w-xs sm:text-sm sm:leading-6"
          >
            <option>United States</option>
            <option>Canada</option>
            <option>Mexico</option>
          </select>
        </div>
      </div>

      <TextualHeighlights />

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
  )
}

export default App
