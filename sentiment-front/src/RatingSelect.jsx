import React from 'react'

const RatingSelect = ({ label, value, onChange, options }) => {
    return (
        <div>
            <label style={{ color: '#263238' }} className="block mb-2 text-sm text-gray-600 dark:text-gray-200">
                {label}
            </label>
            <select
                style={{ fontSize: 25, padding: 9, background: '#263238' }}
                value={value}
                onChange={(e) => onChange(e.target.value)}
                placeholder="Select color"
                className="block w-full px-5 py-3 mt-2 text-gray-700 placeholder-gray-400 bg-white border border-gray-200 rounded-lg dark:placeholder-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:border-gray-700 focus:border-blue-400 dark:focus:border-blue-400 focus:ring-blue-400 focus:outline-none focus:ring focus:ring-opacity-40"
            >
                {options.map((item, index) => (
                    <option key={index} value={item.key}>
                        {item.value}
                    </option>
                ))}
            </select>
        </div>
    );
};

export default RatingSelect