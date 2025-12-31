(function () {
  let uiInitialized = false;

  const backdrop = () => document.getElementById("aj-search-backdrop");
  const open = () => {
    const b = backdrop();
    if (!b) return;

    b.hidden = false;

    if (!uiInitialized) {
      uiInitialized = true;
      new PagefindUI({
        element: "#pagefind-ui",
        showSubResults: true,
      });
    }

    // Focus the generated input once it exists
    window.setTimeout(() => {
      const input =
        document.querySelector("#pagefind-ui input[type='text']") ||
        document.querySelector("#pagefind-ui input");
      if (input) input.focus();
    }, 50);
  };

  const close = () => {
    const b = backdrop();
    if (!b) return;
    b.hidden = true;
  };

  document.addEventListener("keydown", (e) => {
    const isMac = navigator.platform.toUpperCase().includes("MAC");
    const k = e.key.toLowerCase() === "k";
    const combo = k && ((isMac && e.metaKey) || (!isMac && e.ctrlKey));

    if (combo) {
      e.preventDefault();
      open();
    }

    if (e.key === "Escape") close();
  });

  document.addEventListener("click", (e) => {
    const b = backdrop();
    if (!b || b.hidden) return;
    if (e.target === b) close();
  });

  // Optional: expose a function if you want a visible search button too
  window.ajOpenSearch = open;
})();
