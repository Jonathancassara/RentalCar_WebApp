module.exports = {
  content: [
    "./templates/**/*.html",        // Templates racines
    "./Frontend/templates/**/*.html", // Templates dans l'app Frontend
    "./Frontend/static/**/*.css",   // CSS statique
    "./**/*.html",                  // Parcourt tous les fichiers HTML
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};
