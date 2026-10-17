(() => {
  const root = document.documentElement;
  const themeButton = document.querySelector(".theme-toggle");
  const menuButton = document.querySelector(".menu-toggle");
  const navigation = document.querySelector("#primary-navigation");
  const year = document.querySelector("[data-current-year]");

  const setTheme = (theme) => {
    root.dataset.theme = theme;
    if (themeButton) {
      const nextTheme = theme === "dark" ? "clair" : "sombre";
      themeButton.setAttribute("aria-label", `Activer le thème ${nextTheme}`);
      themeButton.querySelector(".theme-icon").textContent =
        theme === "dark" ? "☼" : "☾";
    }
  };

  setTheme("dark");

  themeButton?.addEventListener("click", () => {
    const nextTheme = root.dataset.theme === "dark" ? "light" : "dark";
    setTheme(nextTheme);
  });

  menuButton?.addEventListener("click", () => {
    const isExpanded = menuButton.getAttribute("aria-expanded") === "true";
    menuButton.setAttribute("aria-expanded", String(!isExpanded));
    menuButton.querySelector(".sr-only").textContent = isExpanded
      ? "Ouvrir le menu"
      : "Fermer le menu";
    navigation?.classList.toggle("is-open", !isExpanded);
  });

  navigation?.querySelectorAll("a[href*='#']").forEach((link) => {
    link.addEventListener("click", () => {
      menuButton?.setAttribute("aria-expanded", "false");
      if (menuButton) {
        menuButton.querySelector(".sr-only").textContent = "Ouvrir le menu";
      }
      navigation.classList.remove("is-open");
    });
  });

  if (year) {
    year.textContent = String(new Date().getFullYear());
  }
})();
