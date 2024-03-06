module.exports = {
  theme: {
    screens: {
      sm: "375px",
      md: "768px",
      lg: "1024px",
      xl: "1440px",
    },
    fontFamily: {
      sans: ["Helmholtz", "sans-serif"]
    },
    extend: {
      colors: {
        "hmc-blue": {
          light: "#14c8ff",
          DEFAULT: "#005aa0",
          dark: "#002864",
        },
        "hmc-black": {
          DEFAULT: "#161616"
        },
        "hmc-grey": {
          light: "#f7f7f7",
          DEFAULT: "#c2c5cc"
        },
        "hmc-green": "#05e5ba"
      },
    }
  }
};
