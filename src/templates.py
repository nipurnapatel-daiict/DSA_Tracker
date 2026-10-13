import json

from theme import CORE_CSS


def get_page_header():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="color-scheme" content="light dark">

    <title>My Personal DSA Journey Space</title>

    <!-- Initialize theme before rendering the page -->
    <script>
        (function () {{
            let theme = 'light';

            try {{
                const savedTheme = localStorage.getItem('theme');

                if (savedTheme === 'dark' || savedTheme === 'light') {{
                    theme = savedTheme;
                }}
            }} catch (error) {{
                console.warn('Theme preference could not be loaded.');
            }}

            document.documentElement.setAttribute('data-theme', theme);
        }})();
    </script>

    <link
        rel="stylesheet"
        href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css"
    >

    {CORE_CSS}
</head>

<body>
    <div class="dashboard-wrapper">

        <div class="header-panel">
            <div class="header-left">
                <div>
                    <span class="disclaimer-badge">
                        <i class="fa-solid fa-graduation-cap"></i>
                        Striver's A2Z DSA Sheet Curriculum
                    </span>

                    <div class="header-title-row">
                        <h1>My Personal DSA Workspace</h1>

                        <!-- Grouped Buttons Container -->
                        <div class="header-actions">
                            <button
                                type="button"
                                class="theme-toggle-btn"
                                id="theme-toggle-btn"
                                onclick="toggleDarkMode()"
                                aria-label="Switch to dark mode"
                                title="Toggle light and dark mode"
                            >
                                <i id="theme-toggle-icon" class="fa-solid fa-moon" aria-hidden="true"></i>
                                <span id="theme-toggle-label">Dark Mode</span>
                            </button>

                            <button
                                type="button"
                                class="reset-sheet-btn"
                                id="reset-sheet-btn"
                                onclick="resetSheet()"
                                aria-label="Reset all sheet progress"
                                title="Reset sheet progress"
                            >
                                <i class="fa-solid fa-rotate-left" aria-hidden="true"></i>
                                <span>Reset Sheet</span>
                            </button>
                        </div>
                    </div>

                    <p class="subheader">
                        <strong>450+</strong> curated problems from basics to advanced. 
                        Expand any topic, take notes, and track your metrics.
                    </p>

                </div> 

            </div>

            <div class="progress-circle-box">
                <div class="circle-label">Progress</div>
                <div id="master-percent-label" class="circle-value">0 / 0</div>
                <div id="master-percentage" class="circle-percent">0%</div>
            </div>
        </div>

        <div id="accordion-root">
"""


def get_page_footer(schema=None):
    # Pass the actual schema when generating the page.
    # Default to an empty schema to keep this function valid on its own.
    if schema is None:
        schema = []

    schema_json = json.dumps(
        schema,
        ensure_ascii=False
    ).replace("<", "\\u003c")

    html_template = """
    </div> <!-- End of accordion-root -->
    
        <footer class="sheet-footer">
            <p class="footer-note">All progress is stored locally on your device via browser LocalStorage.</p>
            
            <p class="copyright">
                &copy; 2026 Workspace &bull; Build with Intent 
                <i class="fa-solid fa-bullseye" style="margin-left: 4px; color: #f59e0b; font-size: 0.8rem; vertical-align: middle;"></i>
            </p>
        </footer> 

    </div> <!-- End of dashboard-wrapper -->
    
    
    <!-- Custom Reset Confirmation Modal -->
    <div
        id="reset-modal"
        class="modal-overlay reset-modal-overlay"
        role="dialog"
        aria-modal="true"
        aria-labelledby="reset-modal-title"
        aria-describedby="reset-modal-description"
        onclick="if (event.target === this) closeResetModal()"
        style="display: none;"
    >
        <div class="modal-window reset-modal-window">

            <div class="reset-icon-wrapper">
                <i class="fa-solid fa-triangle-exclamation"></i>
            </div>

            <h2 id="reset-modal-title" class="reset-modal-title">
                Reset Your DSA Sheet?
            </h2>

            <p id="reset-modal-description" class="reset-modal-description">
                Are you sure you want to start fresh?
                This action will permanently clear your saved progress,
                revision stars, and remarks.
            </p>

            <div class="reset-warning">
                <i class="fa-solid fa-circle-info"></i>
                <span>This action cannot be undone.</span>
            </div>

            <div class="reset-modal-actions">
                <button
                    type="button"
                    class="reset-cancel-btn"
                    onclick="closeResetModal()"
                >
                    Cancel
                </button>

                <button
                    type="button"
                    class="reset-confirm-btn"
                    id="confirm-reset-btn"
                    onclick="confirmResetSheet()"
                >
                    <i class="fa-solid fa-rotate-left"></i>
                    Reset Everything
                </button>
            </div>

        </div>
    </div>


    <div
        id="notes-modal"
        class="modal-overlay"
        role="dialog"
        aria-modal="true"
        aria-labelledby="notes-modal-title"
        onclick="if (event.target === this) closeNotesModal()"
    >
        <div class="modal-window">
            <div id="notes-modal-title" class="modal-title">
                <i
                    class="fa-solid fa-sticky-note"
                    style="color:#f97316;"
                ></i>
                Notes
                
            </div>

            <div id="modal-content-area" class="modal-body">
                Currently Unavailable
            </div>

            <button
                type="button"
                class="modal-close-btn"
                onclick="closeNotesModal()"
            >
                Close Workspace
            </button>
        </div>
    </div>

    <script>
        // The Python generator replaces this marker with valid JSON.
        let masterSchema = SCHEMA_PLACEHOLDER;

        // Safe localStorage wrappers.
        function readStorage(key) {
            try {
                return localStorage.getItem(key);
            } catch (error) {
                return null;
            }
        }

        function writeStorage(key, value) {
            try {
                localStorage.setItem(key, value);
                return true;
            } catch (error) {
                console.warn('Unable to save browser preference:', key);
                return false;
            }
        }

        // Dark Mode
        function toggleDarkMode() {
            const root = document.documentElement;

            const currentTheme =
                root.getAttribute('data-theme') || 'light';

            const newTheme =
                currentTheme === 'dark' ? 'light' : 'dark';

            root.setAttribute('data-theme', newTheme);

            writeStorage('theme', newTheme);

            updateThemeButton(newTheme);
        }

        function updateThemeButton(theme) {
            const icon = document.getElementById('theme-toggle-icon');
            const label = document.getElementById('theme-toggle-label');
            const button = document.getElementById('theme-toggle-btn');

            if (!icon || !label || !button) {
                return;
            }

            if (theme === 'dark') {
                icon.className = 'fa-solid fa-sun';
                label.textContent = 'Light Mode';
                button.setAttribute('aria-label', 'Switch to light mode');
            } else {
                icon.className = 'fa-solid fa-moon';
                label.textContent = 'Dark Mode';
                button.setAttribute('aria-label', 'Switch to dark mode');
            }
        }

        // Accordion Controls
        function toggleSection(id, btn) {
            const element = document.getElementById(id);

            if (!element || !btn) {
                return;
            }

            element.classList.toggle('expanded');

            const arrow = btn.querySelector('.chevron-icon');

            if (arrow) {
                arrow.classList.toggle('rotated');
            }

            btn.setAttribute(
                'aria-expanded',
                element.classList.contains('expanded') ? 'true' : 'false'
            );
        }

        // Save Solved State
        function saveProgress(hashKey) {
            const checkbox = document.getElementById(hashKey);

            if (!checkbox) {
                return;
            }

            writeStorage(hashKey, checkbox.checked ? 'true' : 'false');

            recalculateAllProgressTrackers();
        }

        //reset sheet
        let resetPreviousFocus = null;

        // Open the custom confirmation card.
        function resetSheet() {
            const modal = document.getElementById('reset-modal');
            const confirmButton = document.getElementById('confirm-reset-btn');

            if (!modal) {
                return;
            }

            resetPreviousFocus = document.activeElement;

            modal.style.display = 'flex';
            document.body.style.overflow = 'hidden';

            if (confirmButton) {
                confirmButton.focus();
            }
        }

        // Close the card without changing any saved data.
        function closeResetModal() {
            const modal = document.getElementById('reset-modal');

            if (!modal) {
                return;
            }

            modal.style.display = 'none';
            document.body.style.overflow = '';

            if (resetPreviousFocus && resetPreviousFocus.isConnected) {
                resetPreviousFocus.focus();
            }

            resetPreviousFocus = null;
        }

        // Execute the reset only after explicit confirmation.
        function confirmResetSheet() {
            const modal = document.getElementById('reset-modal');

            if (!Array.isArray(masterSchema)) {
                closeResetModal();
                return;
            }

            // Clear solved progress stored under schema keys.
            masterSchema.forEach(step => {
                (step.subtopics || []).forEach(sub => {
                    (sub.keys || []).forEach(key => {
                        try {
                            localStorage.removeItem(key);
                        } catch (error) {
                            console.warn('Unable to reset progress.');
                        }
                    });
                });
            });

            // Clear revision stars and remarks.
            document.querySelectorAll(
                '.revision-symbol, .remark-input'
            ).forEach(element => {
                const probId = element.getAttribute('data-prob-id');

                if (!probId) {
                    return;
                }

                const prefix = element.classList.contains('revision-symbol')
                    ? 'rev_'
                    : 'remark_';

                try {
                    localStorage.removeItem(prefix + probId);
                } catch (error) {
                    console.warn('Unable to reset saved sheet data.');
                }
            });

            // Reset checkboxes.
            document.querySelectorAll('input[type="checkbox"]').forEach(cb => {
                cb.checked = false;
            });

            // Reset remarks.
            document.querySelectorAll('.remark-input').forEach(input => {
                input.value = '';
            });

            // Reset revision stars.
            document.querySelectorAll('.revision-symbol').forEach(star => {
                star.classList.remove('active');
                star.setAttribute('aria-pressed', 'false');

                const icon = star.querySelector('i');

                if (icon) {
                    icon.className = 'fa-regular fa-star';
                }
            });
            
            // Close the card and refresh progress.
            closeResetModal();
            recalculateAllProgressTrackers();
        } // <-- confirmResetSheet function closes safely here

        // ==========================================
        // GLOBAL EVENT LISTENERS (Placed Outside)
        // ==========================================

        // Listens for the Escape key to close the modal anywhere on the page
        document.addEventListener('keydown', function (event) {
            if (event.key === 'Escape') {
                const modal = document.getElementById('reset-modal');

                if (modal && modal.style.display === 'flex') {
                    closeResetModal();
                }
            }
        });

        // Save remarks
        function saveRemark(probId, input) {
            if (!input || !probId) {
                return;
            }

            const storageKey = 'remark_' + probId;
            const value = input.value.slice(0, 50).trim();

            // Reflect trimming in the input.
            if (input.value !== value) {
                input.value = value;
            }

            if (value.length === 0) {
                try {
                    localStorage.removeItem(storageKey);
                } catch (error) {
                    console.warn('Unable to remove saved remark.');
                }
                return;
            }

            writeStorage(storageKey, value);
        }

        // Revision Star
        function toggleRevisionFlag(hashKey, element) {
            if (!element) {
                return;
            }

            const storageKey = 'rev_' + hashKey;
            const currentStatus = readStorage(storageKey) === 'true';
            const newStatus = !currentStatus;

            writeStorage(storageKey, newStatus ? 'true' : 'false');

            element.classList.toggle('active', newStatus);

            const icon = element.querySelector('i');

            if (icon) {
                icon.className = newStatus
                    ? 'fa-solid fa-star'
                    : 'fa-regular fa-star';
            }

            element.setAttribute(
                'aria-pressed',
                newStatus ? 'true' : 'false'
            );
        }

        // Notes Modal
        function openNotesModal(noteUrl) {
            const modal = document.getElementById('notes-modal');
            const content = document.getElementById('modal-content-area');

            if (!modal || !content) {
                return;
            }

            content.replaceChildren();

            const unavailable =
                !noteUrl ||
                !String(noteUrl).trim() ||
                ['nan', 'none', 'null'].includes(
                    String(noteUrl).trim().toLowerCase()
                );

            if (unavailable) {
                const message = document.createElement('div');
                message.style.padding = '15px 0';

                const icon = document.createElement('i');
                icon.className = 'fa-solid fa-triangle-exclamation';
                icon.style.cssText =
                    'font-size:28px;color:#ef4444;display:block;margin-bottom:12px;';

                const text = document.createElement('strong');
                text.textContent = 'Currently Unavailable';

                message.append(icon, text);
                content.appendChild(message);
            } else {
                // Allow only HTTP(S) note links.
                let url;

                try {
                    url = new URL(String(noteUrl), window.location.href);
                } catch (error) {
                    url = null;
                }

                if (!url || !['http:', 'https:'].includes(url.protocol)) {
                    content.textContent = 'This note link is invalid.';
                } else {
                    const description = document.createElement('p');
                    description.textContent =
                        'Your custom document link is ready:';

                    const link = document.createElement('a');
                    link.href = url.href;
                    link.target = '_blank';
                    link.rel = 'noopener noreferrer';
                    link.style.cssText =
                        'font-weight:600;text-decoration:none;display:inline-flex;align-items:center;gap:6px;margin-top:12px;';

                    const icon = document.createElement('i');
                    icon.className = 'fa-solid fa-arrow-up-right-from-square';

                    link.append(icon, document.createTextNode(
                        ' Launch Shared Note Workspace'
                    ));

                    content.append(description, link);
                }
            }

            modal.style.display = 'flex';
        }

        function closeNotesModal() {
            const modal = document.getElementById('notes-modal');

            if (modal) {
                modal.style.display = 'none';
            }
        }

        // Progress Calculations
        function recalculateAllProgressTrackers() {
            let globalTotal = 0;
            let globalSolved = 0;

            if (!Array.isArray(masterSchema)) {
                console.error('The DSA schema must be an array.');
                return;
            }

            masterSchema.forEach(step => {
                let stepTotal = 0;
                let stepSolved = 0;

                (step.subtopics || []).forEach(sub => {
                    let subTotal = 0;
                    let subSolved = 0;

                    (sub.keys || []).forEach(key => {
                        subTotal++;

                        if (readStorage(key) === 'true') {
                            subSolved++;
                        }
                    });

                    const subFillElement =
                        document.getElementById('fill_' + sub.id);

                    const subText =
                        document.getElementById('text_' + sub.id);

                    const subPercent = subTotal > 0
                        ? Math.round((subSolved / subTotal) * 100)
                        : 0;

                    if (subFillElement) {
                        subFillElement.style.width = subPercent + '%';
                    }

                    if (subText) {
                        subText.textContent =
                            subSolved + ' / ' + subTotal + ' Solved';
                    }

                    stepTotal += subTotal;
                    stepSolved += subSolved;
                });

                const stepFillElement =
                    document.getElementById('fill_' + step.id);

                const stepText =
                    document.getElementById('text_' + step.id);

                const stepPercent = stepTotal > 0
                    ? Math.round((stepSolved / stepTotal) * 100)
                    : 0;

                if (stepFillElement) {
                    stepFillElement.style.width = stepPercent + '%';
                }

                if (stepText) {
                    stepText.textContent =
                        stepSolved + ' / ' + stepTotal + ' Solved';
                }

                globalTotal += stepTotal;
                globalSolved += stepSolved;
            });

            // Calculate overall progress percentage.
            const globalPercent = globalTotal > 0
                ? Math.round((globalSolved / globalTotal) * 100)
                : 0;

            // Update the overall circular progress ring.
            const progressCircle = document.querySelector(
                '.progress-circle-box'
            );

            if (progressCircle) {
                progressCircle.style.setProperty(
                    '--progress-percentage',
                    globalPercent + '%'
                );
            }

            // Update the overall solved count.
            const masterLabel =
                document.getElementById('master-percent-label');

            if (masterLabel) {
                masterLabel.textContent =
                    globalSolved + ' / ' + globalTotal;
            }

            // Update the overall percentage text.
            const masterPercentage =
                document.getElementById('master-percentage');

            if (masterPercentage) {
                masterPercentage.textContent = globalPercent + '%';
            }
        }

        // Initialize after the document is ready.
        function initializeDashboard() {
            updateThemeButton(
                document.documentElement.getAttribute('data-theme') || 'light'
            );

            // Restore solved progress
            document.querySelectorAll('input[type="checkbox"]').forEach(cb => {
                cb.checked = readStorage(cb.id) === 'true';
            });

            // Restore saved remarks
            document.querySelectorAll('.remark-input').forEach(input => {
                const probId = input.getAttribute('data-prob-id');
                const savedRemark = readStorage('remark_' + probId);

                if (savedRemark !== null) {
                    input.value = savedRemark;
                }
            });

            // Restore revision stars
            document.querySelectorAll('.revision-symbol').forEach(star => {
                const probId = star.getAttribute('data-prob-id');
                const icon = star.querySelector('i');

                const active = readStorage('rev_' + probId) === 'true';

                star.classList.toggle('active', active);
                star.setAttribute('aria-pressed', active ? 'true' : 'false');

                if (icon) {
                    icon.className = active
                        ? 'fa-solid fa-star'
                        : 'fa-regular fa-star';
                }
            });

            // Update all progress indicators
            recalculateAllProgressTrackers();
        }

        if (document.readyState === 'loading') {
            document.addEventListener(
                'DOMContentLoaded',
                initializeDashboard
            );
        } else {
            initializeDashboard();
        }
    </script>
</body>
</html>
"""
    return html_template.replace("SCHEMA_PLACEHOLDER", schema_json)



