CORE_CSS = """
<style>
    :root {
        color-scheme: light;

        /* Light Mode Palette */
        --bg-main: #f8fafc;
        --card-bg: #ffffff;
        --text-dark: #0f172a;
        --text-muted: #64748b;
        --border-light: #e2e8f0;
        --panel-bg: #ffffff;
        --badge-bg: #f1f5f9;
        --badge-text: #475569;

        /* Accent Colors */
        --accent-orange: #f97316;

        /* Progress Meter Palette */
        --progress-empty-peach: #ffedd5;
        --progress-filled-orange: #f97316;

        /* Difficulty Classes */
        --diff-basic: #3b82f6;
        --diff-easy: #22c55e;
        --diff-medium: #eab308;
        --diff-hard: #ef4444;
    }

    /* Dark Mode Palette */
    [data-theme="dark"] {
        color-scheme: dark;

        --bg-main: #0b1120;
        --card-bg: #172033;
        --text-dark: #f8fafc;
        --text-muted: #a3b2c7;
        --border-light: #334155;
        --panel-bg: #172033;
        --badge-bg: #273449;
        --badge-text: #dbe5f1;

        /* General accent */
        --accent-orange: #fb923c;

        /* Step progress: vibrant blue */
        --progress-empty-peach: #1e293b;
        --progress-filled-orange: #60a5fa;

        /* Subtopic progress: vibrant teal */
        --subtopic-progress-empty: #1e293b;
        --subtopic-progress-filled: #2dd4bf;

        # /* Difficulty badges */
        # --diff-basic: #60a5fa;
        # --diff-easy: #4ade80;
        # --diff-medium: #facc15;
        # --diff-hard: #f87171;
        --diff-basic: #3b76c5;
        --diff-easy: #278747;
        --diff-medium: #c49a18;
        --diff-hard: #c93d48;

        --circle-progress-color: #60a5fa;
        --circle-progress-track: #273449;
    }

    * {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
    }

    html {
        min-height: 100%;
        background-color: var(--bg-main);
        overscroll-behavior: none; /* Block viewport bounce at the browser root */
    }

    body {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI",
                     Roboto, sans-serif;
        background-color: var(--bg-main);
        color: var(--text-dark);
        width: 100%;
        
        /* FIX: Use height + box-sizing to keep page sizing locked with your padding */
        height: 100%;
        box-sizing: border-box;
        
        overscroll-behavior: none; /* Block content trackpad drag bounce */
        padding: 40px 0;
        line-height: 1.5;
        transition: background-color 0.2s ease, color 0.2s ease;
    }


    button,
    input,
    textarea,
    select {
        font: inherit;
    }

    button {
        color: inherit;
    }

    .dashboard-wrapper {
        width: 82%;
        max-width: 950px;
        margin: 0 auto;
        padding: 0 32px;
    }

    /* Header */
    .header-panel {
        margin-bottom: 35px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 24px;
        background: var(--panel-bg);
        padding: 30px;
        border-radius: 16px;
        border: 1px solid var(--border-light);
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
        transition: background-color 0.2s, border-color 0.2s;
    }

    .header-left {
        flex: 1;
        min-width: 0;
    }

    .disclaimer-badge {
        display: inline-block;
        font-size: 11px;
        font-weight: 700;
        background: #feebc8;
        color: #9c4221;
        padding: 6px 14px;
        border-radius: 20px;
        text-transform: uppercase;
        margin-bottom: 12px;
        letter-spacing: 0.5px;
    }

    .header-title-row {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 16px;
        margin-bottom: 6px;
        padding-right: 10px;
    }

    h1 {
        font-size: 28px;
        font-weight: 800;
        letter-spacing: -0.5px;
        color: var(--text-dark);
    }

    .theme-toggle-btn {
        flex-shrink: 0;
        background: var(--badge-bg);
        border: 1px solid var(--border-light);
        color: var(--text-dark);
        padding: 8px 14px;
        border-radius: 8px;
        cursor: pointer;
        font-weight: 600;
        font-size: 13px;
        display: inline-flex;
        align-items: center;
        gap: 8px;
        transition: background-color 0.2s, border-color 0.2s;
    }

    .theme-toggle-btn:hover {
        background-color: var(--border-light);
    }


    /* Reset Sheet Button */
    .reset-sheet-btn {
        flex-shrink: 0;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        gap: 7px;
        padding: 8px 12px;

        background: transparent;
        color: var(--text-muted);
        border: 1px solid var(--border-light);
        border-radius: 8px;

        font-size: 13px;
        font-weight: 600;
        cursor: pointer;

        transition:
            background-color 0.2s ease,
            color 0.2s ease,
            border-color 0.2s ease;
    }

    .reset-sheet-btn:hover {
        background: var(--badge-bg);
        color: var(--text-dark);
        border-color: var(--text-muted);
    }

    .reset-sheet-btn:focus-visible {
        outline: 2px solid var(--accent-orange);
        outline-offset: 3px;
    }

    .reset-sheet-btn i {
        font-size: 12px;
    }

    @media (max-width: 600px) {
        .reset-sheet-btn {
            padding: 8px 10px;
            font-size: 12px;
        }
    }


    .theme-toggle-btn:focus-visible,
    .step-header:focus-visible,
    .subtopic-header:focus-visible {
        outline: 2px solid var(--accent-orange);
        outline-offset: 3px;
    }

    .subtitle {
        color: var(--text-muted);
        font-size: 14px;
    }


    

    /* Progress Circle */
    .progress-circle-box {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        min-width: 120px;
        width: 120px;
        height: 120px;
        box-sizing: border-box;
        border: none;
        border-radius: 50%;

        /* Dynamic circular progress */
        background: conic-gradient(
            var(--circle-progress-color, var(--progress-filled-orange))
            var(--progress-percentage, 0%),
            var(--circle-progress-track, var(--badge-bg)) 0
        );

        box-shadow: 0 4px 10px rgba(249, 115, 22, 0.08);
        text-align: center;
        transition: background 0.3s ease;
        position: relative;
        isolation: isolate;
    }

    /* Inner circle creates the ring */
    .progress-circle-box::before {
        content: "";
        position: absolute;
        inset: 7px;
        border-radius: 50%;
        background: var(--panel-bg);
        z-index: -1;
    }

    .circle-label,
    .circle-value,
    .circle-percent {
        position: relative;
        z-index: 1;
    }

    .circle-label {
        font-size: 11px;
        font-weight: 700;
        text-transform: uppercase;
        color: var(--text-muted);
        letter-spacing: 0.5px;
        margin-bottom: 2px;
    }

    .circle-value {
        font-size: 15px;
        font-weight: 800;
        color: var(--text-dark);
    }

    .circle-percent {
        font-size: 13px;
        font-weight: 700;
        color: var(--circle-progress-color, var(--progress-filled-orange));
    }

    /* Progress Bars */
    .step-progress-bar {
        width: 100%;
        height: 6px;
        background-color: var(--progress-empty-peach);
    }

    .step-progress-fill {
        height: 100%;
        width: 0%;
        background-color: var(--progress-filled-orange);
        transition: width 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }

    .subtopic-progress-bar {
        width: 100%;
        height: 4px;
        background-color: var(--progress-empty-peach);
    }

    .subtopic-progress-fill {
        height: 100%;
        width: 0%;
        background-color: var(--progress-filled-orange);
        transition: width 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }

    /* Accordion Steps */
    .step-container {
        background: var(--card-bg);
        border: 1px solid var(--border-light);
        border-radius: 12px;
        margin-bottom: 16px;
        overflow: hidden;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.02);
        transition: background-color 0.2s, border-color 0.2s;
    }

    .step-header {
        width: 100%;
        background: none;
        border: none;
        text-align: left;
        padding: 20px 24px;
        cursor: pointer;
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 20px;
    }

    .step-header:hover {
        background: var(--bg-main);
    }

    .step-title-area {
        display: flex;
        align-items: center;
        gap: 12px;
        font-size: 16px;
        font-weight: 700;
        color: var(--text-dark);
    }

    .step-title-area .chevron-icon {
        font-size: 13px;
        color: var(--text-muted);
        transition: transform 0.2s ease;
    }

    .counter-badge {
        background: var(--badge-bg);
        padding: 4px 12px;
        border-radius: 6px;
        font-size: 13px;
        font-weight: 600;
        color: var(--badge-text);
        display: inline-flex;
        align-items: center;
        gap: 4px;
        transition: background-color 0.2s;
        white-space: nowrap;
    }

    .counter-badge span {
        color: var(--progress-filled-orange);
        font-weight: 700;
    }

    .step-content {
        display: none;
        padding: 10px 24px 24px;
        border-top: 1px solid var(--border-light);
        background: var(--bg-main);
        transition: background-color 0.2s, border-color 0.2s;
    }

    /* Subtopics */
    .subtopic-container {
        background: var(--card-bg);
        border: 1px solid var(--border-light);
        border-radius: 8px;
        margin-top: 15px;
        overflow: hidden;
        transition: background-color 0.2s, border-color 0.2s;
    }

    .subtopic-header {
        width: 100%;
        background: none;
        border: none;
        text-align: left;
        padding: 14px 20px;
        cursor: pointer;
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 15px;
    }

    .subtopic-header:hover {
        background: var(--bg-main);
    }

    .subtopic-title-area {
        display: flex;
        align-items: center;
        gap: 10px;
        font-size: 14px;
        font-weight: 600;
        color: var(--text-dark);
    }

    .subtopic-content {
        display: none;
        padding: 15px 20px;
        border-top: 1px solid var(--border-light);
        background: var(--card-bg);
    }

    /* Problem Tables */
    ul {
        list-style: none;
        width: 100%;
    }

    .table-header-row,
    li {
        display: grid;
        grid-template-columns: 0.4fr 3fr 1fr 1.2fr 0.8fr 0.8fr 1.8fr;
        gap: 15px;
    }

    .table-header-row {
        padding: 12px 10px;
        border-bottom: 2px solid var(--border-light);
        font-weight: 700;
        font-size: 12px;
        color: var(--text-muted);
        text-transform: uppercase;
    }

    li {
        padding: 14px 10px;
        border-bottom: 1px solid var(--border-light);
        align-items: center;
        transition: background-color 0.15s;
    }

    li:hover {
        background-color: var(--bg-main);
    }

    li:last-child {
        border-bottom: none;
    }

    .prob-main {
        display: flex;
        align-items: center;
        gap: 10px;
        min-width: 0;
    }

    .prob-name {
        font-weight: 550;
        font-size: 14px;
        color: var(--text-dark);
    }

    .badge {
        font-size: 11px;
        padding: 3px 10px;
        border-radius: 4px;
        font-weight: 700;
        width: 75px;
        text-transform: uppercase;
        color: #fff;
        text-align: center;
    }

    .badge.basic {
        background-color: var(--diff-basic);
    }

    .badge.easy {
        background-color: var(--diff-easy);
    }

    .badge.medium {
        background-color: var(--diff-medium);
        color: #0f172a;
    }

    .badge.hard {
        background-color: var(--diff-hard);
    }

    /* Platform Links */
    .platform-links {
        display: flex;
        gap: 8px;
        align-items: center;
        flex-wrap: wrap;
    }

    /* Shared styles for platform links */
    .platform-links a,
    .platform-links .platform-disabled,
    .platform-links a.disabled {
        text-decoration: none;
        font-size: 12px;
        font-weight: 700;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        gap: 5px;
        padding: 4px 8px;
        border-radius: 6px;
        background: var(--card-bg);
        border: 1px solid var(--border-light);
        transition: background-color 0.2s, border-color 0.2s;
        white-space: nowrap;
    }

    /* LeetCode */
    .platform-links a.lc-logo {
        color: #b45309;
        border-color: #fde68a;
        background: #fffbeb;
    }

    [data-theme="dark"] .platform-links a.lc-logo {
        color: #fbbf24;
        background: #451a03;
        border-color: #78350f;
    }

    /* GeeksforGeeks */
    .platform-links a.gfg-logo {
        color: #2f8d46;
        border-color: #bbf7d0;
        background: #f0fdf4;
    }

    [data-theme="dark"] .platform-links a.gfg-logo {
        color: #86efac;
        background: #022c22;
        border-color: #064e3b;
    }

    /* Missing platform links */
    .platform-links .platform-disabled,
    .platform-links a.disabled {
        color: var(--text-muted);
        cursor: not-allowed;
        background: var(--bg-main);
        border-color: var(--border-light);
        pointer-events: none;
        opacity: 0.7;
    }

    /* Icon alignment */
    .platform-links i {
        display: inline-block;
        line-height: 1;
        font-size: 12px;
    }

    /* Action Icons */
    .icon-btn {
        background: none;
        border: none;
        cursor: pointer;
        font-size: 16px;
        color: var(--text-muted);
        padding: 4px;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        transition: all 0.2s;
    }

    .icon-btn:hover {
        color: var(--accent-orange);
        background: var(--badge-bg);
        border-radius: 4px;
    }

    .note-active-btn {
        color: #3b82f6 !important;
    }

    .revision-symbol {
        font-size: 16px;
        text-align: center;
        color: #94a3b8; /* Visible muted gray in light mode */
        cursor: pointer;
        transition: color 0.2s, transform 0.2s;
    }

    .revision-symbol:hover {
        color: #ca8a04;
        transform: scale(1.12);
    }

    .revision-symbol.active {
        color: #eab308;
    }

    /* Dark mode */
    [data-theme="dark"] .revision-symbol {
        color: #cbd5e1;
    }

    [data-theme="dark"] .revision-symbol:hover {
        color: #facc15;
    }

    [data-theme="dark"] .revision-symbol.active {
        color: #facc15;
    }

    # .remark-text {
    #     font-size: 12px;
    #     color: var(--text-muted);
    #     font-style: italic;
    #     max-width: 180px;
    #     overflow: hidden;
    #     text-overflow: ellipsis;
    #     white-space: nowrap;
    # }


    /* Editable problem remarks */
    .remark-input {
        width: 100%;
        min-width: 100px;
        max-width: 220px;
        box-sizing: border-box;
        padding: 7px 9px;
        border: 1px solid var(--border-light);
        border-radius: 7px;
        background: var(--card-bg);
        color: var(--text-dark);
        font-family: inherit;
        font-size: 12px;
        outline: none;
        transition: border-color 0.2s, box-shadow 0.2s;
    }

    .remark-input::placeholder {
        color: var(--text-muted);
        opacity: 0.8;
    }

    .remark-input:focus {
        border-color: var(--accent-orange);
        box-shadow: 0 0 0 2px rgba(251, 146, 60, 0.15);
    }

    .remark-input:hover {
        border-color: var(--accent-orange);
    }
    3. Add the JavaScript in templates.py
    Inside the <script> section, add this function near your existing saveProgress() function:

    javascript

    function saveRemark(probId, input) {
        if (!input) {
            return;
        }

        const storageKey = 'remark_' + probId;
        const value = input.value.trim();

        if (value) {
            writeStorage(storageKey, value);
        } else {
            try {
                localStorage.removeItem(storageKey);
            } catch (error) {
                console.warn('Unable to remove saved remark.');
            }
        }
    }

    /* Utility States */
    .expanded {
        display: block !important;
    }

    .rotated {
        transform: rotate(90deg);
        color: var(--accent-orange) !important;
    }

    /* Notes Modal */
    .modal-overlay {
        display: none;
        position: fixed;
        inset: 0;
        width: 100%;
        height: 100%;
        background: rgba(15, 23, 42, 0.7);
        justify-content: center;
        align-items: center;
        z-index: 1000;
        backdrop-filter: blur(2px);
        padding: 20px;
    }

    .modal-window {
        background: var(--card-bg);
        padding: 25px;
        border-radius: 12px;
        width: 90%;
        max-width: 450px;
        max-height: 85vh;
        overflow-y: auto;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
        border: 1px solid var(--border-light);
        text-align: center;
        color: var(--text-dark);
        transition: background-color 0.2s, border-color 0.2s;
    }

    .modal-title {
        font-size: 16px;
        font-weight: 700;
        margin-bottom: 12px;
        color: var(--text-dark);
    }

    .modal-body {
        font-size: 14px;
        color: var(--text-muted);
        margin-bottom: 20px;
        line-height: 1.6;
        overflow-wrap: anywhere;
    }

    .modal-body a {
        color: #3b82f6;
    }

    .modal-close-btn {
        background: var(--badge-bg);
        color: var(--text-dark);
        border: 1px solid var(--border-light);
        padding: 8px 20px;
        border-radius: 6px;
        cursor: pointer;
        font-weight: 600;
        font-size: 13px;
        transition: all 0.2s;
    }

    .modal-close-btn:hover {
        background-color: var(--border-light);
    }

    input[type="checkbox"] {
        width: 17px;
        height: 17px;
        cursor: pointer;
        accent-color: var(--accent-orange);
    }

    
    /* Custom Reset Confirmation Card */
    .reset-modal-overlay {
        position: fixed;
        inset: 0;
        z-index: 10000;
        display: none;
        align-items: center;
        justify-content: center;
        padding: 20px;
        background: rgba(15, 23, 42, 0.60);
        backdrop-filter: blur(6px);
        -webkit-backdrop-filter: blur(6px);
    }

    .reset-modal-window {
        width: 100%;
        max-width: 430px;
        padding: 30px 26px;
        text-align: center;
        border-radius: 22px;
        animation: resetCardIn 0.22s ease-out;
    }

    .reset-icon-wrapper {
        width: 66px;
        height: 66px;
        margin: 0 auto 18px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 20px;
        background: rgba(239, 68, 68, 0.12);
        color: #ef4444;
        font-size: 28px;
    }

    .reset-modal-title {
        margin: 0 0 12px;
        font-size: 23px;
        font-weight: 750;
        color: var(--text-primary, inherit);
    }

    .reset-modal-description {
        margin: 0 auto 18px;
        max-width: 340px;
        font-size: 14px;
        line-height: 1.7;
        color: var(--text-secondary, #64748b);
    }

    .reset-warning {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 9px;
        padding: 12px;
        margin-bottom: 24px;
        border-radius: 12px;
        background: rgba(245, 158, 11, 0.10);
        color: #d97706;
        font-size: 12px;
        font-weight: 600;
    }

    .reset-modal-actions {
        display: flex;
        gap: 12px;
    }

    .reset-modal-actions button {
        flex: 1;
        min-height: 46px;
        padding: 11px 14px;
        border: none;
        border-radius: 12px;
        font: inherit;
        font-size: 13px;
        font-weight: 700;
        cursor: pointer;
        transition: transform 0.15s ease, opacity 0.15s ease;
    }

    .reset-modal-actions button:hover {
        transform: translateY(-2px);
    }

    .reset-cancel-btn {
        background: var(--surface-secondary, #e2e8f0);
        color: var(--text-primary, #1e293b);
    }

    .reset-confirm-btn {
        background: #dc2626;
        color: #fff;
    }

    .reset-confirm-btn:hover {
        background: #b91c1c;
    }

    .reset-modal-actions button:focus-visible {
        outline: 3px solid #60a5fa;
        outline-offset: 3px;
    }


    //footer css
    .sheet-header {
        text-align: center;
        margin-bottom: 2rem;
    }

    .subheader {
        font-size: 1.1rem;
        font-style: italic;
        color: #555; /* Medium gray */
        margin-bottom: 1rem;
    }

    .sheet-footer {
        display: flex;
        flex-direction: column;   /* Stacks lines vertically */
        align-items: center;      /* Centers components horizontally */
        justify-content: center;  /* Centers components vertically */
        text-align: center;
        
        margin-top: 5rem;
        padding: 2rem 1.5rem;
        border-top: 1px solid var(--border-color, #e2e8f0);
        gap: 0.25rem;             /* Tightly stacks the copyright directly below the note */
    }

    .footer-note {
        font-size: 0.8rem;
        color: var(--text-muted, #64748b);
        opacity: 0.9;
        margin: 0;                /* Resets default browser text margins */
    }

    .copyright {
        font-size: 0.75rem;
        color: var(--text-muted, #94a3b8);
        margin: 0;                /* Perfectly aligns baseline to the gap threshold above */
        display: inline-flex;
        align-items: center;      /* Vertically aligns the target icon with text string */
    }



    
    @keyframes resetCardIn {
        from {
            opacity: 0;
            transform: translateY(12px) scale(0.97);
        }

        to {
            opacity: 1;
            transform: translateY(0) scale(1);
        }
    }

    @media (max-width: 420px) {
        .reset-modal-window {
            padding: 25px 18px;
        }

        .reset-modal-actions {
            flex-direction: column-reverse;
        }
    }

    @media (prefers-reduced-motion: reduce) {
        .reset-modal-window {
            animation: none;
        }

        .reset-modal-actions button {
            transition: none;
        }
    }



    /* Responsive Layout */
    @media (max-width: 900px) {
        .dashboard-wrapper {
            width: 100%;
            padding: 0 16px;
        }

        .header-panel {
            padding: 22px;
        }

        .header-title-row {
            flex-wrap: wrap;
        }

        .table-header-row,
        li {
            grid-template-columns: 35px minmax(150px, 2fr) 80px
                                 minmax(100px, 1fr);
            gap: 10px;
        }

        .table-header-row > :nth-child(n+5),
        li > :nth-child(n+5) {
            display: none;
        }
    }

    @media (max-width: 600px) {
        body {
            padding: 16px 0;
        }

        .dashboard-wrapper {
            padding: 0 10px;
        }

        .header-panel {
            flex-direction: column;
            align-items: stretch;
            padding: 18px;
            gap: 20px;
        }

        .header-title-row {
            padding-right: 0;
            align-items: flex-start;
        }

        h1 {
            font-size: 22px;
        }

        .progress-circle-box {
            align-self: center;
        }

        .step-header {
            padding: 16px;
            gap: 10px;
        }

        .step-title-area {
            font-size: 14px;
            gap: 8px;
        }

        .counter-badge {
            font-size: 11px;
            padding: 4px 8px;
        }

        .step-content {
            padding: 10px 12px 18px;
        }

        .subtopic-header {
            padding: 12px;
        }

        .subtopic-content {
            padding: 10px;
            overflow-x: auto;
        }

        .table-header-row,
        li {
            grid-template-columns: 25px minmax(120px, 1fr) 65px;
            gap: 8px;
            padding: 10px 4px;
            font-size: 11px;
        }

        .table-header-row > :nth-child(n+4),
        li > :nth-child(n+4) {
            display: none;
        }

        .badge {
            width: auto;
            padding: 3px 6px;
            font-size: 10px;
        }
    }

    @media (prefers-reduced-motion: reduce) {
        *,
        *::before,
        *::after {
            transition-duration: 0.01ms !important;
            animation-duration: 0.01ms !important;
        }
    }
</style>
"""