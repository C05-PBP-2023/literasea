/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/*.html",
    "./**/templates/*.html",
    "./**/static/js/*.js",
  ],
  theme: {
    backgroundSize: {
      sm: "1.5em",
    },
    extend: {
      fontFamily: {
        gabarito: ["Gabarito", "sans-serif"],
        raleway: ["Raleway", "sans-serif"],
        inter: ["Inter", "sans-serif"],
      },
    },
  },
  plugins: [],
};
