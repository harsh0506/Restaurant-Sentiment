import React from 'react'

const ResNames = [
    { id: 1, name: "Pizza Paradise" },
    { id: 2, name: "shushi Heaven" },
    { id: 3, name: "Burger Joint" },
    { id: 4, name: "Taco Delight" },
    { id: 5, name: "Indian Spice" },
]

function SelcetRestoraunt({setResName , width ,justifyContent ,color }) {
  return (
   <>
   <div style={{
        display: "flex",
        flexDirection: "row",
        alignItems: "center",
        width:width,
        justifyContent:justifyContent,
        padding:0,margin:0
      }} className="sm:col-span-3">
        
        <div className="mt-2">
          <select
            style={{
              "fontSize": 25 ,padding:20,background: {color}
            }}
            onChange={(e) => setResName(e.target.value)}
            class="block w-full px-5 py-3 mt-2 text-gray-700 placeholder-gray-400 bg-white border border-gray-200 rounded-lg dark:placeholder-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:border-gray-700 focus:border-blue-400 dark:focus:border-blue-400 focus:ring-blue-400 focus:outline-none focus:ring focus:ring-opacity-40" 
          >
            {
              ResNames.map((item) => <option key={item.id} value={item.id}>{item.name}</option>)
            }

          </select>
        </div>
      </div>
   </>
  )
}

export default SelcetRestoraunt