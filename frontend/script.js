// Micro-interactions for gender buttons
const genderButtons = document.querySelectorAll(".gender-btn");
genderButtons.forEach((btn) => {
  btn.addEventListener("click", () => {
    genderButtons.forEach((b) => {
      b.classList.remove(
        "bg-primary-container",
        "text-on-primary-container",
        "border-primary-container",
      );
      b.classList.add("border-surface-variant", "text-on-surface");
    });
    btn.classList.add(
      "bg-primary-container",
      "text-on-primary-container",
      "border-primary-container",
    );
    btn.classList.remove("border-surface-variant", "text-on-surface");
  });
});

document.querySelector("form").addEventListener("submit", (e) => {
  e.preventDefault();
  const btn = e.target.querySelector('button[type="submit"]');
  const originalHtml = btn.innerHTML;
  btn.innerHTML =
    '<span class="material-symbols-outlined animate-spin">refresh</span> Lädt...';
  setTimeout(() => {
    btn.innerHTML =
      '<span class="material-symbols-outlined">check_circle</span> Erfolgreich!';
    btn.classList.replace("bg-primary-fixed", "bg-secondary-container");
    setTimeout(() => {
      window.location.href = "main.html";
    }, 1000);
  }, 1500);
});
