document.addEventListener("DOMContentLoaded", () => {

    /*
    ========================================
    Reveal animations
    ========================================
    */

    const elements = document.querySelectorAll(".reveal");

    if ("IntersectionObserver" in window) {

        const observer = new IntersectionObserver(
            (entries, currentObserver) => {

                entries.forEach((entry) => {

                    if (entry.isIntersecting) {

                        entry.target.classList.add("reveal--visible");

                        currentObserver.unobserve(entry.target);

                    }

                });

            },
            {
                threshold: 0.15,
            }
        );

        elements.forEach((element) => observer.observe(element));

    } else {

        elements.forEach((element) => {
            element.classList.add("reveal--visible");
        });

    }


    /*
    ========================================
    Copy email to clipboard
    ========================================
    */

    const emailButton = document.querySelector(".footer__email-copy");

    const copyToast = document.querySelector(".copy-toast");

    let toastTimeout;


    const showToast = (message) => {

        if (!copyToast) {
            return;
        }

        window.clearTimeout(toastTimeout);

        copyToast.textContent = message;

        copyToast.classList.add("copy-toast--visible");

        toastTimeout = window.setTimeout(() => {

            copyToast.classList.remove("copy-toast--visible");

        }, 2600);

    };


    const fallbackCopy = (text) => {

        const textarea = document.createElement("textarea");

        textarea.value = text;

        textarea.setAttribute("readonly", "");

        textarea.style.position = "fixed";

        textarea.style.opacity = "0";

        document.body.appendChild(textarea);

        textarea.select();

        const copied = document.execCommand("copy");

        textarea.remove();

        if (!copied) {
            throw new Error("Clipboard copy failed.");
        }

    };


    const copyText = async (text) => {

        if (navigator.clipboard && window.isSecureContext) {

            await navigator.clipboard.writeText(text);

            return;

        }

        fallbackCopy(text);

    };


    if (emailButton) {

        emailButton.addEventListener("click", async () => {

            const email = emailButton.dataset.email;

            if (!email) {
                return;
            }

            try {

                await copyText(email);

                showToast("Email copied to clipboard");

                const originalText = emailButton.textContent;

                emailButton.textContent = "Copied!";

                window.setTimeout(() => {

                    emailButton.textContent = originalText;

                }, 1800);

            } catch (error) {

                console.error("Unable to copy email:", error);

                showToast("Could not copy the email");

            }

        });

    }

});