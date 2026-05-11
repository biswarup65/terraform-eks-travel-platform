window.addEventListener("scroll", () => {

    const navbar = document.querySelector(".navbar");

    if (window.scrollY > 50) {
        navbar.style.background = "rgba(15, 23, 42, 0.95)";
    } else {
        navbar.style.background = "rgba(0,0,0,0.4)";
    }

});