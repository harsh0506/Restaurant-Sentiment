import React from 'react';

export default function TextualHeighlights({ data }) {

  const [Labels, setLabels] = React.useState([{}])

  const result = (input) => {
    try {
      if (data && data.length > 0) {
        const output = Object.keys(input[0]).map((key, index) => ({
          id: index + 1,
          name: key.replace(/_/g, ' '),
          value: input[0][key].slice(0, 3)
        }));
        console.log(output)
        setLabels(output)
      }
    } catch (error) {
      console.log(error)
    }
  }

  React.useEffect(() => {
    result(data)
  }, [data])


  return (
    <div style={{ width: "98vw", paddingBottom: 20, paddingTop: 20 }} className="bg-white py-24 sm:py-32">
      <div className="mx-auto max-w-7xl px-6 lg:px-8">
        <dl className="grid grid-cols-1 gap-x-8 gap-y-16 text-center lg:grid-cols-4">
          {Labels.map((stat) => (
            <div key={stat.id} className="mx-auto flex max-w-xs flex-col gap-y-4">
              <dt className="text-base leading-7 text-gray-600">{stat.name}</dt>
              <dd className="order-first text-3xl font-semibold tracking-tight text-gray-900 sm:text-5xl">
                {stat.value}
              </dd>
            </div>
          ))}
        </dl>
      </div>
    </div>
  )
}
