// navbar.js

const navItems = [
  { text: "Strona Główna", href: "index.html" },
  { text: "Wiadomości", href: "wiadomosci.html" },
  { text: "Artykuły", href: "artykuly.html" },
  { text: "Poradniki", href: "poradniki.html" },
  { text: "Kursy", href: "kursy.html" },
  { text: "Facebook", href: "https://www.facebook.com/danetykpl" },
  { text: "Discord", href: "https://discord.gg/gvXWhek3S4" },
  { text: "GitHub", href: "https://github.com/danetykpl" }
];

const navList = document.getElementById("navbar-list");

navItems.forEach(item => {
  const listItem = document.createElement("li");
  listItem.className = "nav-item";

  const anchor = document.createElement("a");
  anchor.className = "nav-link";
  anchor.href = item.href;
  anchor.textContent = item.text;

  listItem.appendChild(anchor);
  navList.appendChild(listItem);
});
