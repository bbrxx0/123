// Small UX: validate date inputs on booking form
document.addEventListener("DOMContentLoaded", () => {
  const inEl = document.querySelector('input[name="check_in"]');
  const outEl = document.querySelector('input[name="check_out"]');

  function validateDates() {
    if (!inEl || !outEl) return;
    if (!inEl.value || !outEl.value) return;
    const a = new Date(inEl.value);
    const b = new Date(outEl.value);
    if (b <= a) {
      outEl.setCustomValidity("Check-out must be after check-in.");
    } else {
      outEl.setCustomValidity("");
    }
  }

  if (inEl && outEl) {
    inEl.addEventListener("change", validateDates);
    outEl.addEventListener("change", validateDates);
  }

  // Quick city pills in hero
  const cityInput = document.querySelector('input[name="city"]');
  document.querySelectorAll(".pill").forEach((pill) => {
    pill.style.cursor = "pointer";
    pill.addEventListener("click", () => {
      if (!cityInput) return;
      cityInput.value = pill.textContent.trim();
      cityInput.focus();
    });
  });
});
