"""Global design system for the MarketMind Sim web interface.

Single source of truth for the visual language ("Aurora" light theme):

* Design tokens — CSS custom properties for colour, typography, spacing,
  radius, shadow and motion, declared once on ``:root``.
* Component styling — buttons, form inputs, metric cards, expanders,
  containers, tabs, sidebar, dialogs, alerts, progress bars, scrollbars.
* Motion — shared keyframes plus subtle entrance/hover effects, with a
  ``prefers-reduced-motion`` escape hatch.
* Responsive rules — breakpoints that tighten padding and type scale on
  small viewports.

``inject_global_styles()`` is called once per script run from the entry
page module, right after ``st.set_page_config``.  Because the stylesheet
is injected at the very start of the render, later page-level CSS (e.g.
``agent_market._inject_market_styles``) can still override it with equal
specificity — the cascade order keeps page-scoped tweaks winning.
"""

import streamlit as st

_CSS = """
<style>
/* ============================================================
   MarketMind Sim — "Aurora" design tokens
   ============================================================ */
:root {
    /* Surfaces */
    --mm-bg: #f6f8fb;             /* app canvas */
    --mm-surface: #ffffff;        /* cards, sidebar, widgets */
    --mm-surface-2: #f1f5f9;      /* subtle fills */
    --mm-border: #e4eaf1;
    --mm-border-strong: #d3dce6;

    /* Text */
    --mm-text: #17212b;
    --mm-text-2: #46535f;
    --mm-text-3: #7b8794;

    /* Brand */
    --mm-brand: #287a6d;
    --mm-brand-deep: #1f6157;
    --mm-brand-soft: #e7f3f0;
    --mm-brand-border: #b6d8d0;
    --mm-brand-ring: rgba(40, 122, 109, 0.22);
    --mm-accent: #2a5fa6;
    --mm-accent-soft: #e8f0fb;

    /* Semantic */
    --mm-success: #1f9d55;
    --mm-danger: #e05252;
    --mm-warning: #f0b429;

    /* Dark data panels (agent cards, notices, KPI tiles) */
    --mm-panel: #1d2739;
    --mm-panel-2: #16202f;
    --mm-panel-border: #2c3a52;
    --mm-panel-text: #e7ecf6;
    --mm-panel-text-2: #9aa8bf;

    /* Radius */
    --mm-radius-sm: 8px;
    --mm-radius: 12px;
    --mm-radius-lg: 16px;

    /* Elevation */
    --mm-shadow-sm: 0 1px 2px rgba(23, 33, 43, 0.06);
    --mm-shadow-md: 0 4px 14px rgba(23, 33, 43, 0.10);
    --mm-shadow-lg: 0 12px 34px rgba(23, 33, 43, 0.16);

    /* Motion */
    --mm-ease: cubic-bezier(0.2, 0.7, 0.3, 1);
    --mm-speed: 180ms;

    /* Type */
    --mm-font: "Source Sans Pro", -apple-system, BlinkMacSystemFont,
        "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    --mm-mono: "Source Code Pro", ui-monospace, SFMono-Regular, Menlo,
        Consolas, monospace;
}

/* ============================================================
   Base & typography
   ============================================================ */
.stApp {
    color: var(--mm-text);
    font-family: var(--mm-font);
}
.stApp h1, .stApp h2, .stApp h3 {
    font-family: var(--mm-font);
}
.stApp h1 {
    letter-spacing: -0.02em;
    font-weight: 800;
}
.stApp h2 {
    letter-spacing: -0.01em;
    font-weight: 750;
}
.stApp h3 { font-weight: 700; }
.stApp p, .stApp li { line-height: 1.6; }
.stApp code, .stApp pre {
    font-family: var(--mm-mono);
}
.stApp hr {
    border-color: var(--mm-border);
    opacity: 1;
    margin: 1.15rem 0;
}
.stApp ::selection { background: rgba(40, 122, 109, 0.18); }
.block-container { padding-top: 4rem; max-width: 1240px; }

/* ============================================================
   Buttons
   ============================================================ */
.stApp button {
    border-radius: 10px;
    font-weight: 600;
    transition:
        transform var(--mm-speed) var(--mm-ease),
        box-shadow var(--mm-speed) var(--mm-ease),
        background-color var(--mm-speed) ease,
        border-color var(--mm-speed) ease,
        color var(--mm-speed) ease;
}
.stApp button[kind="primary"] {
    background-image: linear-gradient(180deg, #2f8577, #287a6d);
    border: 1px solid var(--mm-brand-deep);
    box-shadow: 0 1px 2px rgba(23, 33, 43, 0.10);
}
.stApp button[kind="primary"]:hover {
    background-image: linear-gradient(180deg, #29796c, #1f6157);
    transform: translateY(-1px);
    box-shadow: 0 6px 16px rgba(40, 122, 109, 0.28);
}
.stApp button[kind="primary"]:active {
    transform: translateY(0);
    box-shadow: 0 1px 2px rgba(23, 33, 43, 0.12);
}
.stApp button[kind="secondary"]:hover {
    border-color: var(--mm-brand);
    color: var(--mm-brand-deep);
    background: var(--mm-brand-soft);
}
.stApp button:focus-visible {
    outline: none;
    box-shadow: 0 0 0 3px var(--mm-brand-ring) !important;
}

/* ============================================================
   Form inputs
   ============================================================ */
.stApp [data-baseweb="input"],
.stApp [data-baseweb="select"] > div,
.stApp [data-baseweb="textarea"] {
    border-radius: 10px !important;
    transition: border-color var(--mm-speed) ease,
        box-shadow var(--mm-speed) ease;
}
.stApp [data-baseweb="input"]:focus-within,
.stApp [data-baseweb="select"] > div:focus-within,
.stApp [data-baseweb="textarea"]:focus-within {
    border-color: var(--mm-brand) !important;
    box-shadow: 0 0 0 3px var(--mm-brand-ring) !important;
}

/* ============================================================
   Metric cards
   ============================================================ */
.stApp [data-testid="stMetric"] {
    background: var(--mm-surface);
    border: 1px solid var(--mm-border);
    border-radius: var(--mm-radius);
    padding: 12px 16px 10px;
    box-shadow: var(--mm-shadow-sm);
    transition: transform var(--mm-speed) var(--mm-ease),
        box-shadow var(--mm-speed) var(--mm-ease),
        border-color var(--mm-speed) ease;
    animation: mm-fade-up 0.32s var(--mm-ease) both;
}
.stApp [data-testid="stMetric"]:hover {
    transform: translateY(-2px);
    box-shadow: var(--mm-shadow-md);
    border-color: var(--mm-brand-border);
}
.stApp [data-testid="stMetricValue"] {
    font-variant-numeric: tabular-nums;
    letter-spacing: -0.01em;
}

/* ============================================================
   Cards, expanders, containers
   ============================================================ */
.stApp [data-testid="stVerticalBlockBorderWrapper"] {
    border-radius: var(--mm-radius);
    border-color: var(--mm-border);
    box-shadow: var(--mm-shadow-sm);
}
.stApp details[data-testid="stExpander"] {
    border-radius: var(--mm-radius);
    border-color: var(--mm-border);
    box-shadow: var(--mm-shadow-sm);
    overflow: hidden;
    transition: box-shadow var(--mm-speed) var(--mm-ease),
        border-color var(--mm-speed) ease;
}
.stApp details[data-testid="stExpander"]:hover {
    box-shadow: var(--mm-shadow-md);
    border-color: var(--mm-border-strong);
}
.stApp details[data-testid="stExpander"] summary:hover {
    color: var(--mm-brand-deep);
}

/* ============================================================
   Tabs
   ============================================================ */
.stApp [data-baseweb="tab-list"] { gap: 2px; }
.stApp button[data-baseweb="tab"] {
    font-weight: 600;
    color: var(--mm-text-3);
    border-radius: 8px 8px 0 0;
    transition: color var(--mm-speed) ease,
        background-color var(--mm-speed) ease;
}
.stApp button[data-baseweb="tab"]:hover { color: var(--mm-brand-deep); }
.stApp button[data-baseweb="tab"][aria-selected="true"] {
    color: var(--mm-brand-deep);
}

/* ============================================================
   Sidebar
   ============================================================ */
.stApp [data-testid="stSidebar"] {
    background: var(--mm-surface);
    border-right: 1px solid var(--mm-border);
}
.stApp [data-testid="stSidebar"] hr {
    border-color: var(--mm-border);
    margin: 0.9rem 0;
}
.stApp [data-testid="stSidebar"] h1,
.stApp [data-testid="stSidebar"] h2,
.stApp [data-testid="stSidebar"] h3 {
    letter-spacing: -0.01em;
}

/* ============================================================
   Dialogs, alerts, progress
   ============================================================ */
[data-testid="stDialog"] > div > div {
    border-radius: var(--mm-radius-lg) !important;
    border: 1px solid var(--mm-border);
    box-shadow: var(--mm-shadow-lg) !important;
    animation: mm-pop 0.24s var(--mm-ease) both;
}
.stApp [data-testid="stAlert"] {
    border-radius: 10px;
    animation: mm-fade-in 0.25s var(--mm-ease) both;
}
.stApp [data-testid="stProgress"] > div {
    border-radius: 99px;
    background: var(--mm-surface-2);
}
.stApp [data-testid="stProgress"] > div > div {
    border-radius: 99px;
    transition: width 0.4s var(--mm-ease);
}

/* ============================================================
   Scrollbars
   ============================================================ */
.stApp ::-webkit-scrollbar { width: 8px; height: 8px; }
.stApp ::-webkit-scrollbar-track { background: transparent; }
.stApp ::-webkit-scrollbar-thumb {
    background: #c9d4de;
    border-radius: 99px;
}
.stApp ::-webkit-scrollbar-thumb:hover { background: var(--mm-brand-border); }

/* ============================================================
   Shared dynamic-UI classes (simulation page)
   ============================================================ */
/* Agent action card — dark data panel with semantic accent border. */
.mm-action-card {
    background: var(--mm-panel);
    border: 1px solid var(--mm-panel-border);
    border-left: 4px solid var(--mm-accent-color, var(--mm-text-3));
    border-radius: 10px;
    padding: 10px 14px;
    margin-bottom: 8px;
    animation: mm-fade-up 0.3s var(--mm-ease) both;
    transition: transform var(--mm-speed) var(--mm-ease),
        box-shadow var(--mm-speed) var(--mm-ease);
}
.mm-action-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 22px rgba(16, 24, 40, 0.20);
}
.mm-action-head {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 8px;
}
.mm-action-name {
    font-weight: 700;
    font-size: 13px;
    color: var(--mm-panel-text);
}
.mm-action-badge {
    flex-shrink: 0;
    padding: 2px 10px;
    border-radius: 99px;
    font-size: 11px;
    font-weight: 700;
    color: #ffffff;
    letter-spacing: 0.05em;
}
.mm-action-meta {
    margin-top: 6px;
    font-size: 12px;
    color: var(--mm-panel-text-2);
}
.mm-action-meta b { color: var(--mm-panel-text); }
.mm-action-strategy {
    font-size: 11px;
    color: var(--mm-panel-text-2);
    margin-top: 3px;
}

/* System notice banner — dark, severity-tinted. */
.mm-notice {
    border-left: 4px solid var(--mm-accent-color, var(--mm-accent));
    border-radius: 10px;
    padding: 8px 14px;
    margin: 4px 0;
    font-size: 13px;
    box-shadow: var(--mm-shadow-sm);
    animation: mm-fade-up 0.28s var(--mm-ease) both;
}
.mm-notice--info {
    background: #16233d;
    border-color: #4a90d9;
    color: #dbe7f5;
}
.mm-notice--success {
    background: #132b1d;
    border-color: #34c26b;
    color: #d9f2e3;
}
.mm-notice--warning {
    background: #2d2410;
    border-color: var(--mm-warning);
    color: #f7ecd4;
}
.mm-notice--error {
    background: #331414;
    border-color: var(--mm-danger);
    color: #f6dcdc;
}
.mm-notice-time {
    float: right;
    font-size: 11px;
    opacity: 0.65;
}

/* ============================================================
   Keyframes
   ============================================================ */
@keyframes mm-fade-up {
    from { opacity: 0; transform: translateY(6px); }
    to   { opacity: 1; transform: none; }
}
@keyframes mm-fade-in {
    from { opacity: 0; }
    to   { opacity: 1; }
}
@keyframes mm-pop {
    from { opacity: 0; transform: scale(0.97); }
    to   { opacity: 1; transform: none; }
}

/* ============================================================
   Responsive
   ============================================================ */
@media (max-width: 820px) {
    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
        padding-top: 3.4rem;
    }
    .stApp h1 { font-size: 1.7rem; }
    .stApp [data-testid="stMetric"] { padding: 10px 12px; }
}
@media (max-width: 640px) {
    .stApp h1 { font-size: 1.5rem; }
    .stApp [data-testid="stMetric"] {
        border-radius: 10px;
    }
    .mm-action-card { padding: 9px 11px; }
}
@media (prefers-reduced-motion: reduce) {
    .stApp *,
    [data-testid="stDialog"] * {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
    }
}
</style>
"""


def inject_global_styles() -> None:
    """Inject the design-system stylesheet.

    Called once per script run from the entry module.  Re-injecting on
    every run is intentional and idempotent: Streamlit rebuilds the
    element tree on websocket reconnects, so a once-per-session guard
    could leave the UI unstyled after a reconnect.
    """
    st.markdown(_CSS, unsafe_allow_html=True)
