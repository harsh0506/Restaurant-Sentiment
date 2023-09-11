import React from 'react';
import './App.css'
import HistogramChart from './Charthistogram'
import TextualHeighlights from './TextData';
import MoveGround from './DinoLoadingScree';
import SelcetRestoraunt from './SelcetRestoraunt';

function DataAnalytics() {

    const [BarPlotData, setBarPlotData] = React.useState([{ key: [{ count: "", value: "" }] }])
    const [Labels, setLabels] = React.useState()
    const [ResName, setResName] = React.useState(1)
    const [isLoading, setIsLoading] = React.useState(true);

    const result = async () => {
        try {
            const res = await (await fetch(`http://localhost:5000/api/getResSpecificData/${ResName}`)).json()
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
            <SelcetRestoraunt
                setResName={setResName}
                justifyContent={"center"}
                color="white"
                width={"98vw"} />

            {isLoading ? (
                <MoveGround />
            ) : (
                <>
                    <blockquote style={{width:"98vw"}} className="text-center text-xl font-semibold leading-8 text-gray-900 sm:text-2xl sm:leading-9">
                        <p>
                            This is an anlytics page for restaurant ,choose your required restaurant name, <u><a href='/form'>Add a review here</a></u>
                        </p>
                    </blockquote>
                    <TextualHeighlights data={Labels} />
                    <div style={{ width: "98vw" }} className="bg-white">
                        <div style={{ paddingTop: 30 }} className="mx-auto max-w-2xl px-4 py-16 sm:px-6 sm:py-24 lg:max-w-7xl lg:px-8">
                            <h2 className="sr-only">Products</h2>
                            <div className="grid grid-cols-1 gap-x-6 gap-y-10 sm:grid-cols-1 lg:grid-cols-2 xl:grid-cols-2 xl:gap-x-8">
                                <HistogramChart text={"Ambience"} data={BarPlotData.ambience} />
                                <HistogramChart text={"Service"} data={BarPlotData.service} />
                                <HistogramChart text={"Hygiene"} data={BarPlotData.hygiene} />
                                <HistogramChart text={"Food"} data={BarPlotData.food} />
                            </div>
                        </div>
                    </div>
                </>
            )}

        </>
    )
}

export default DataAnalytics
