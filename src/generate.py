import hashlib
import html
import json
import os
import webbrowser
from urllib.parse import urlparse

import pandas as pd
import templates


def clean_value(value, default=""):
    """Convert Excel values to clean strings, handling NaN safely."""
    if pd.isna(value):
        return default

    value = str(value).strip()

    if value.lower() in ("nan", "none", "null"):
        return default

    return value


def make_id(prefix, value, length=8):
    """Generate a stable HTML-safe ID."""
    digest = hashlib.md5(
        value.encode("utf-8")
    ).hexdigest()[:length]

    return f"{prefix}_{digest}"


def escape_html(value):
    """Escape text before inserting it into HTML."""
    return html.escape(str(value), quote=True)


def safe_url(value):
    """Allow only HTTP and HTTPS links from spreadsheet data."""
    value = clean_value(value)

    if not value:
        return ""

    parsed = urlparse(value)

    if parsed.scheme.lower() not in ("http", "https"):
        return ""

    if not parsed.netloc:
        return ""

    return value


def make_platform_link(url, css_class, title, icon_class, label):
    """Build a platform link or a readable fallback."""
    if not url:
        return f"""
            <span
                class="platform-disabled"
                title="No {escape_html(title)} link available"
            >—</span>
        """

    icon_html = (
        f'<i class="{escape_html(icon_class)}" '
        'aria-hidden="true"></i>'
        if icon_class
        else ""
    )

    return f"""
        <a
            href="{escape_html(url)}"
            target="_blank"
            rel="noopener noreferrer"
            class="{escape_html(css_class)}"
            title="{escape_html(title)}"
        >
            {icon_html}
            <span>{escape_html(label)}</span>
        </a>
    """


def main():
    excel_file = "data/striver_dsa_sheet.xlsx"
    output_file = "index.html"

    # 1. Read Excel
    try:
        df = pd.read_excel(excel_file)
    except Exception as error:
        print(
            f"Error: Could not read '{excel_file}'. "
            f"Reason: {error}"
        )
        return

    df.columns = df.columns.astype(str).str.strip()

    required_columns = {"Step", "Subtopic"}
    missing_columns = required_columns - set(df.columns)

    if missing_columns:
        print(
            "Missing required Excel columns: "
            + ", ".join(sorted(missing_columns))
        )
        return

    prob_col = (
        "Problem "
        if "Problem " in df.columns
        else "Problem"
    )

    if prob_col not in df.columns:
        print(
            "Excel must contain a 'Problem' "
            "or 'Problem ' column."
        )
        return

    # 2. Build accordion HTML and progress schema
    body_content = []
    js_schema = []
    total_problems = 0

    for idx, (step_name, step_group) in enumerate(
        df.groupby("Step", sort=False),
        start=1,
    ):
        raw_step_str = clean_value(step_name)

        if not raw_step_str:
            continue

        if raw_step_str.lower().startswith("step"):
            step_str = raw_step_str
        else:
            step_str = f"Step {idx}: {raw_step_str}"

        step_id = make_id("step", step_str)

        step_entry = {
            "id": step_id,
            "name": step_str,
            "subtopics": [],
        }

        body_content.append(f"""
        <div class="step-container">

            <div class="step-progress-bar">
                <div
                    id="fill_{step_id}"
                    class="step-progress-fill"
                ></div>
            </div>

            <button
                type="button"
                class="step-header"
                aria-expanded="false"
                aria-controls="{step_id}"
                onclick="toggleSection('{step_id}', this)"
            >
                <div class="step-title-area">
                    <span class="chevron-icon">
                        <i class="fa-solid fa-chevron-right"></i>
                    </span>

                    <span>{escape_html(step_str)}</span>
                </div>

                <div class="step-meta-stats">
                    <div
                        id="text_{step_id}"
                        class="counter-badge"
                    >
                        <span>0</span> / 0 Solved
                    </div>
                </div>
            </button>

            <div id="{step_id}" class="step-content">
        """)

        for sub_name, sub_group in step_group.groupby(
            "Subtopic",
            sort=False,
        ):
            sub_str = clean_value(sub_name)

            if not sub_str:
                continue

            sub_id = make_id(
                "sub",
                step_str + sub_str,
            )

            sub_entry = {
                "id": sub_id,
                "name": sub_str,
                "keys": [],
            }

            body_content.append(f"""
                <div class="subtopic-container">

                    <div class="subtopic-progress-bar">
                        <div
                            id="fill_{sub_id}"
                            class="subtopic-progress-fill"
                        ></div>
                    </div>

                    <button
                        type="button"
                        class="subtopic-header"
                        aria-expanded="false"
                        aria-controls="{sub_id}"
                        onclick="toggleSection('{sub_id}', this)"
                    >
                        <div class="subtopic-title-area">
                            <span class="chevron-icon">
                                <i class="fa-solid fa-chevron-right"></i>
                            </span>

                            <span>{escape_html(sub_str)}</span>
                        </div>

                        <div class="subtopic-meta-stats">
                            <div
                                id="text_{sub_id}"
                                class="counter-badge"
                            >
                                <span>0</span> / 0 Solved
                            </div>
                        </div>
                    </button>

                    <div id="{sub_id}" class="subtopic-content">

                        <div class="table-header-row">
                            <div></div>
                            <div>Problem Name</div>
                            <div>Difficulty</div>
                            <div>Platform Links</div>
                            <div>Notes</div>
                            <div>Revision</div>
                            <div>Remarks</div>
                        </div>

                        <ul>
            """)

            for _, row in sub_group.iterrows():
                prob_raw = clean_value(row.get(prob_col))

                if not prob_raw:
                    continue

                diff_raw = clean_value(
                    row.get("Difficulty"),
                    "medium",
                ).lower()

                allowed_difficulties = {
                    "basic",
                    "easy",
                    "medium",
                    "hard",
                }

                if diff_raw not in allowed_difficulties:
                    diff_raw = "medium"

                lc_url = safe_url(row.get("LeetcodeLink"))
                gfg_url = safe_url(row.get("GFGLink"))
                note_url = safe_url(row.get("NoteLink"))

                remark_val = clean_value(row.get("Remarks"))

                # Stable problem ID
                prob_hash = make_id(
                    "id",
                    prob_raw,
                    length=12,
                )

                sub_entry["keys"].append(prob_hash)
                total_problems += 1

                # Platform links
                lc_html = make_platform_link(
                url=lc_url,
                css_class="lc-logo",
                title="LeetCode",
                icon_class="",
                label="LC",
                )

                gfg_html = make_platform_link(
                    url=gfg_url,
                    css_class="gfg-logo",
                    title="GeeksforGeeks",
                    icon_class="",
                    label="GFG",
                )

                # Notes button
                note_class = (
                    "icon-btn note-active-btn"
                    if note_url
                    else "icon-btn"
                )

                # json.dumps safely quotes the URL for JS.
                # html.escape protects the HTML attribute.
                note_argument = escape_html(
                    json.dumps(note_url)
                )

                note_html = f"""
                    <button
                        type="button"
                        class="{note_class}"
                        onclick="openNotesModal({note_argument})"
                        title="View Explanation"
                        aria-label="View explanation for {escape_html(prob_raw)}"
                    >
                        <i
                            class="fa-solid fa-note-sticky"
                            aria-hidden="true"
                        ></i>
                    </button>
                """

                # Revision button
                revision_html = f"""
                    <button
                        type="button"
                        class="revision-symbol"
                        data-prob-id="{prob_hash}"
                        onclick="toggleRevisionFlag('{prob_hash}', this)"
                        title="Toggle Revision Bookmark"
                        aria-label="Toggle revision bookmark"
                        aria-pressed="false"
                    >
                        <i
                            class="fa-regular fa-star"
                            aria-hidden="true"
                        ></i>
                    </button>
                """

                # Remarks
                remark_html = f"""
                    <input
                        type="text"
                        class="remark-input"
                        id="remark_{prob_hash}"
                        data-prob-id="{prob_hash}"
                        placeholder="Add remark..."
                        value="{escape_html(remark_val[:50])}"
                        maxlength="50"
                        aria-label="Remark for {escape_html(prob_raw)}"
                        oninput="saveRemark('{prob_hash}', this)"
                        onchange="saveRemark('{prob_hash}', this)"
                    >
                """

                # Problem row
                body_content.append(f"""
                            <li>
                                <div>
                                    <input
                                        type="checkbox"
                                        id="{prob_hash}"
                                        onchange="saveProgress('{prob_hash}')"
                                        aria-label="Mark {escape_html(prob_raw)} as solved"
                                    >
                                </div>

                                <div>
                                    <span class="prob-name">
                                        {escape_html(prob_raw)}
                                    </span>
                                </div>

                                <div>
                                    <span class="badge {diff_raw}">
                                        {escape_html(diff_raw)}
                                    </span>
                                </div>

                                <div>
                                    <div class="platform-links">
                                        {lc_html}
                                        {gfg_html}
                                    </div>
                                </div>

                                <div>{note_html}</div>

                                <div>{revision_html}</div>

                                <div>{remark_html}</div>
                            </li>
                """)

            body_content.append("""
                        </ul>
                    </div>
                </div>
            """)

            # Remove duplicate IDs while preserving order.
            sub_entry["keys"] = list(
                dict.fromkeys(sub_entry["keys"])
            )

            step_entry["subtopics"].append(sub_entry)

        body_content.append("""
            </div>
        </div>
        """)

        js_schema.append(step_entry)

    # 3. Generate final HTML
    try:
        final_output = (
            templates.get_page_header()
            + "".join(body_content)
            + templates.get_page_footer(js_schema)
        )
    except Exception as error:
        print(f"Error generating HTML: {error}")
        return

    # 4. Save HTML
    try:
        with open(
            output_file,
            "w",
            encoding="utf-8",
        ) as file:
            file.write(final_output)

    except OSError as error:
        print(
            f"Could not write '{output_file}': {error}"
        )
        return

    print(f"Success! Generated '{output_file}'.")
    print(f"Total problems included: {total_problems}")
    print(f"Steps included: {len(js_schema)}")

    # --------------------------------------------------
    # 5. Open browser preview
    # --------------------------------------------------
    local_url = "file://" + os.path.abspath(output_file)

    print(f"🌐 Opening preview: {local_url}")

    try:
        webbrowser.open(local_url)
    except Exception as error:
        print(
            f"Could not open browser automatically: {error}"
        )


if __name__ == "__main__":
    main()