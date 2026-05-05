const botones = document.querySelectorAll(".vermas");

botones.forEach(btn => {
  btn.addEventListener("click", function () {
    const article = btn.closest(".article");
    const caja = article.querySelector(".caja");

    caja.classList.toggle("visible");
  });
});
