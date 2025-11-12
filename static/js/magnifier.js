(function () {
    function initMagnifier(img, zoom) {
        if (img.dataset.magnifierInit) return;
        img.dataset.magnifierInit = true;

        const container = img.parentElement;

        const lens = document.createElement("div");
        lens.className = "img-magnifier-lens";
        img.parentElement.insertBefore(lens, img);

        const imgSrc = img.currentSrc || img.src;
        lens.style.backgroundImage = `url('${imgSrc}')`;

        function setup() {
            const rect = img.getBoundingClientRect();
            if (rect.width === 0 || rect.height === 0) return; // hidden image, skip

            const cx = (img.naturalWidth / rect.width) * zoom;
            const cy = (img.naturalHeight / rect.height) * zoom;
            lens.style.backgroundSize = rect.width * cx + "px " + rect.height * cy + "px";

            function moveLens(e) {
                e.preventDefault();
                const pos = getCursorPos(e);
                let x = pos.x;
                let y = pos.y;
                const lw = lens.offsetWidth / 2;
                const lh = lens.offsetHeight / 2;

                // x = Math.max(lw, Math.min(x, rect.width - lw));
                // y = Math.max(lh, Math.min(y, rect.height - lh));

                lens.style.left = (x - lw) + "px";
                lens.style.top = (y - lh) + "px";

                lens.style.backgroundPosition = -(x * cx - lw) + "px " + -(y * cy - lh) + "px";
            }

            function getCursorPos(e) {
                const rect = img.getBoundingClientRect();
                let clientX = e.clientX, clientY = e.clientY;
                if (e.touches && e.touches.length) {
                    clientX = e.touches[0].clientX;
                    clientY = e.touches[0].clientY;
                }
                return {x: clientX - rect.left, y: clientY - rect.top};
            }

            function show() {
                lens.style.display = "block";
            }

            function hide() {
                lens.style.display = "none";
            }

            container.addEventListener("mousemove", moveLens);
            container.addEventListener("touchmove", moveLens, {passive: false});
            container.addEventListener("mouseenter", show);
            container.addEventListener("mouseleave", hide);
            container.addEventListener("touchstart", show);
            container.addEventListener("touchend", hide);

            window.addEventListener("resize", function () {
                const newRect = img.getBoundingClientRect();
                lens.style.backgroundSize = newRect.width * cx + "px " + newRect.height * cy + "px";
            });
        }


        if (img.complete) {
            setup();
        } else {
            img.addEventListener('load', () => {
                setup();
            });
        }
    }

    document.addEventListener("DOMContentLoaded", function () {
        document.querySelectorAll(".tab-pane.active .magnifiable").forEach(img => initMagnifier(img, 2.0));

        const tabButtons = document.querySelectorAll('a[data-bs-toggle="tab"]');
        tabButtons.forEach(btn => {
            btn.addEventListener('shown.bs.tab', function (event) {
                const targetId = event.target.getAttribute('href').substring(1); // remove #
                const targetTab = document.getElementById(targetId);
                targetTab.querySelectorAll(".magnifiable").forEach(img => initMagnifier(img, 2.0));
            });
        });

    });

})();
