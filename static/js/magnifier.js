(function () {
  // Example sensor data (pixel coords relative to original image natural size)
  // Replace with your real data from DB or inline attributes.
  const sensors = [
    { id: 1, name: "Sensor A", x: 2510, y: 1175 },
    { id: 2, name: "Sensor B", x: 1200, y: 340 },
    { id: 3, name: "Sensor C", x: 900, y: 760 }
  ];

  function createHotspots(img, container, sensors) {
    // remove existing sensors
    container.querySelectorAll('.sensor').forEach(n => n.remove());

    const naturalW = img.naturalWidth;
    const naturalH = img.naturalHeight;
    if (!naturalW || !naturalH) return;

    sensors.forEach(s => {
      const leftPercent = (s.x / naturalW) * 100;
      const topPercent  = (s.y / naturalH) * 100;

      const btn = document.createElement('button');
      btn.className = 'sensor';
      btn.setAttribute('data-id', s.id);
      btn.setAttribute('aria-label', s.name);
      btn.style.left = leftPercent + '%';
      btn.style.top  = topPercent  + '%';
      btn.title = s.name;

      btn.addEventListener('click', (ev) => {
        ev.stopPropagation();
        openSensorModal(s);
      });

      container.appendChild(btn);
    });
  }

  function openSensorModal(sensor) {
    const modal = document.getElementById('sensorModal');
    document.getElementById('modalBody').textContent = `${sensor.name} (id ${sensor.id}) — details here.`;
    modal.setAttribute('aria-hidden', 'false');
  }

  function closeModal() {
    document.getElementById('sensorModal').setAttribute('aria-hidden', 'true');
  }
  document.getElementById('closeModal').addEventListener('click', closeModal);

//
//   /* ---- existing magnifier initialization (slightly adapted) ---- */
//   function initMagnifier(imgID, zoom) {
//     const img = document.getElementById(imgID);
//     const container = img.parentElement;
//     if (!img) return;
//
//     // create lens (if not exists)
//     let lens = container.querySelector('.img-magnifier-lens');
//     if (!lens) {
//       lens = document.createElement("div");
//       lens.className = "img-magnifier-lens";
//       container.insertBefore(lens, img);
//     }
//     lens.style.backgroundImage = `url('${img.currentSrc || img.src}')`;
//     lens.style.display = "none"; // hidden until hover
//
//     function setup() {
//       const rect = img.getBoundingClientRect();
//       const naturalW = img.naturalWidth;
//       const naturalH = img.naturalHeight;
//       const cx = (naturalW / rect.width) * zoom;
//       const cy = (naturalH / rect.height) * zoom;
//
//       lens.style.backgroundSize = (rect.width * cx) + "px " + (rect.height * cy) + "px";
//
//       function getCursorPos(e) {
//         const r = img.getBoundingClientRect();
//         let clientX, clientY;
//         if (e.touches && e.touches.length) {
//           clientX = e.touches[0].clientX;
//           clientY = e.touches[0].clientY;
//         } else {
//           clientX = e.clientX;
//           clientY = e.clientY;
//         }
//         return { x: clientX - r.left, y: clientY - r.top, rect: r };
//       }
//
//       function moveLens(e) {
//         e.preventDefault();
//         const pos = getCursorPos(e);
//         const r = pos.rect;
//         let x = pos.x;
//         let y = pos.y;
//
//         const lw = lens.offsetWidth / 2;
//         const lh = lens.offsetHeight / 2;
//         if (x < lw) x = lw;
//         if (x > r.width - lw) x = r.width - lw;
//         if (y < lh) y = lh;
//         if (y > r.height - lh) y = r.height - lh;
//
//         lens.style.left = (x - lw) + "px";
//         lens.style.top = (y - lh) + "px";
//
//         const bgX = -((x * cx) - lw);
//         const bgY = -((y * cy) - lh);
//         lens.style.backgroundPosition = bgX + "px " + bgY + "px";
//       }
//
//       function show() { lens.style.display = "block"; }
//       function hide() { lens.style.display = "none"; }
//
//       container.addEventListener("mousemove", moveLens);
//       container.addEventListener("touchmove", moveLens, { passive: false });
//       container.addEventListener("mouseenter", show);
//       container.addEventListener("mouseleave", hide);
//       container.addEventListener("touchstart", show);
//       container.addEventListener("touchend", hide);
//
//       // reposition hotspots on resize
//       window.addEventListener('resize', () => createHotspots(img, container, sensors));
//     }
//
//     if (img.complete) {
//       setup();
//       createHotspots(img, container, sensors);
//     } else {
//       img.addEventListener('load', () => {
//         setup();
//         createHotspots(img, container, sensors);
//       });
//     }
//   }
//
//   document.addEventListener('DOMContentLoaded', function () {
//     initMagnifier("firstLevelMap", 1.0);
//   });
//   document.addEventListener('DOMContentLoaded', function () {
//     initMagnifier("secondLevelMap", 1.0);
//   });
//   document.addEventListener('DOMContentLoaded', function () {
//     initMagnifier("roofMap", 1.0);
//   });
//
// })();


// (function () {
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

                x = Math.max(lw, Math.min(x, rect.width - lw));
                y = Math.max(lh, Math.min(y, rect.height - lh));

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
            createHotspots(img, container, sensors);
        } else {
            img.addEventListener('load', () => {
                setup();
                createHotspots(img, container, sensors);
            });
        }
    }

    document.addEventListener("DOMContentLoaded", function () {
        document.querySelectorAll(".tab-pane.active .magnifiable").forEach(img => initMagnifier(img, 1.0));

        const tabButtons = document.querySelectorAll('a[data-bs-toggle="tab"]');
        tabButtons.forEach(btn => {
            btn.addEventListener('shown.bs.tab', function (event) {
                const targetId = event.target.getAttribute('href').substring(1); // remove #
                const targetTab = document.getElementById(targetId);
                targetTab.querySelectorAll(".magnifiable").forEach(img => initMagnifier(img, 1.0));
            });
        });

    });

})();
