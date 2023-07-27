/** @type {import('tailwindcss').Config} */
export default {
  content: [
    'node_modules/preline/dist/*.js',
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('tailwindcss'),
    require('preline/plugin'),
    require('autoprefixer'),
  ],
}

