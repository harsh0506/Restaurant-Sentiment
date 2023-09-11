import React, { useState } from 'react'
import SelcetRestoraunt from './SelcetRestoraunt';
import RatingSelect from './RatingSelect';

const options = [
    { key: 1, value: "Best" },
    { key: 2, value: "Good" },
    { key: 3, value: "Average" },
    { key: 4, value: "Edible" },
    { key: 5, value: "Worst" },
]

const handleReset = () => {
    // Reset all state values to their initial state (e.g., empty string or default value)
    setFoodRating('');
    setHygieneRating('');
    setServiceRating('');
    setAmbienceRating('');
};

function FormComp() {

    const [foodRating, setFoodRating] = useState(0);
    const [ambienceRating, setAmbienceRating] = useState(0);
    const [serviceRating, setServiceRating] = useState(0);
    const [hygieneRating, setHygieneRating] = useState(0);
    const [reviewText, setReviewText] = useState('');
    const [ResName, setResName] = React.useState(1)
    const [Error, setErr] = useState(false)

    async function PostData(e) {
        e.preventDefault()
        try {
            // Perform validation checks
            if (!foodRating || !ambienceRating || !serviceRating || !hygieneRating || !reviewText) {
                // Display an error message or handle the validation error
                alert('Please fill in all fields.');
                return;
            }

            const currentDate = new Date();

            // Get the year, month, and day components from the date
            const year = currentDate.getFullYear();
            const month = (currentDate.getMonth() + 1).toString().padStart(2, '0'); // Month is zero-indexed
            const day = currentDate.getDate().toString().padStart(2, '0');

            // Format the date as 'YYYY-MM-DD'
            const sqlFormattedDate = `${year}-${month}-${day}`;

            const m = {
                "food": parseInt(foodRating),
                "ambience": parseInt(ambienceRating),
                "hygiene": parseInt(serviceRating),
                "service": parseInt(hygieneRating),
                "Cid": parseInt(Math.floor(Math.random() * 100) + 1),
                "review": reviewText.toString(), // Convert to string if needed
                "RId": ResName.toString(), // Convert to string if needed
                "Date": sqlFormattedDate
            }

            const info = await fetch('http://localhost:5000/api/reviews', {
                method: 'POST',
                body: JSON.stringify(m),
                headers: {
                    'Content-Type': 'application/json',
                },
            })

            const data = await info.json()

            data.sentiment === "1" ? alert("sentiment was positive") : alert("Sentiment was Negative")
            handleReset()

        } catch (err) {
            console.log(err)
            setErr(true)
        }
    }


    return (
        <>
            {Error ? <Error /> : (
                <section id="Classify" style={{ width: "99.8vw", textAlign: "left", background: '#92E3A9' }} class="bg-white dark:bg-gray-900">
                    <div class="flex justify-center min-h-screen">
                        <div class="hidden bg-cover lg:block lg:w-2/5" style={{ backgroundImage: "url(../Public/Pasta-bro.png)" }}>
                        </div>

                        <div class="flex items-center w-full max-w-3xl p-8 mx-auto lg:px-12 lg:w-3/5">
                            <div class="w-full">
                                <h2 style={{ fontWeight: 800, color: '#263238' }} class="text-2xl font-semibold tracking-wider text-gray-800 capitalize dark:text-white">
                                    Please let us know your Review,<u><a href='/'>Check out analytics</a></u>
                                </h2>

                                <p style={{ color: '#263238' }} class="mt-4 text-gray-500 dark:text-gray-400">
                                    Please Choose the restaurant you ish to review from dropdown menu
                                </p>

                                <SelcetRestoraunt setResName={setResName} />

                                <form class="grid grid-cols-1 gap-6 mt-8 md:grid-cols-2">
                                    <RatingSelect label="Food" value={foodRating} onChange={setFoodRating} options={options} />
                                    <RatingSelect label="Hygiene" value={hygieneRating} onChange={setHygieneRating} options={options} />
                                    <RatingSelect label="Service" value={serviceRating} onChange={setServiceRating} options={options} />
                                    <RatingSelect label="Ambience" value={ambienceRating} onChange={setAmbienceRating} options={options} />
                                    <div>
                                        <input style={{ "fontSize": 25, padding: 9, background: "#263238" }} type="text" value={reviewText} onChange={(e) => setReviewText(e.target.value)} placeholder="Review" class="block w-full px-5 py-3 mt-2 text-gray-700 placeholder-gray-400 bg-white border border-gray-200 rounded-lg dark:placeholder-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:border-gray-700 focus:border-blue-400 dark:focus:border-blue-400 focus:ring-blue-400 focus:outline-none focus:ring focus:ring-opacity-40" />
                                    </div>

                                    <button onClick={PostData} style={{ background: "#def6e5", color: '#263238', borderColor: "#263238", fontSize: 25 }}
                                        class="flex items-center justify-between w-full px-6 py-3 text-sm tracking-wide text-white capitalize transition-colors duration-300 transform bg-blue-500 rounded-lg hover:bg-blue-400 focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-50">
                                        <span>Send </span>

                                        <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5 rtl:-scale-x-100" viewBox="0 0 20 20" fill="currentColor">
                                            <path fill-rule="evenodd"
                                                d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z"
                                                clip-rule="evenodd" />
                                        </svg>
                                    </button>
                                </form>

                            </div>
                        </div>
                    </div>
                </section>)}
        </>
    )
}

export default FormComp