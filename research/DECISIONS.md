# Mini Wallet — product decisions

Decided features not yet built. Mini Wallet app source: `/workspace/portfolio-widget` (Kotlin). Releases go out through `manueles91/mini-wallet`.

## 2026-10-11 — Global privacy mode (decided, built in 13.12)
- One global toggle hides **dollar amounts** and any **quantities that reveal position size**. **Percentages stay** wherever they still mean something. Prices of public assets can stay.
- **Trigger:** a discreet tap on the top-left logo (no eye icon). Use case: demoing the app with amounts hidden while it still looks polished.
- **Options:** quantity is hidden when the option "hasn't been bought". *Open question:* proposed setups (research repo) have no quantity at all, so this probably means held options (Derive) vs proposals. Needs confirming.
- **Scope:** every app page plus the home-screen widgets. Widgets already have a separate eye (`w_hide_total`), and how the two relate is still open.

## 2026-10-11 — 24h / 7d toggle on home-screen widgets (decided, built in 13.12)
- Home-screen widgets get a 24h ↔ 7d switch, like the app's existing shared 24h/7d toggle (`ui_pr`).
- *Open question:* is it one state for all widgets or per widget, and should it follow the app setting?

## 2026-10-11 — Exclude-AERO switch on the Exposure home-screen widget (decided, built in 13.12)
- Matches the in-app Total exposure card's "AERO" switch (13.10, pref `ui_xa`). It only filters the Exposure widget's totals and breakdown.
- *Open question:* is it independent of the in-app switch or shared with it?

## 2026-10-11 — Tappable signal chips on the Liquid card (decided, built in 13.11)
- Tapping a chip (Take profit / Getting warm / Neutral / Consider adding / Add on dip) opens a sheet with the reasoning behind that coin's label.
- Today the chips come from RSI computed in the app (DefiLlama daily prices). The app doesn't read labels/latest.json yet.
- Data: labels v0 already has rsi, usd_sr/eth_sr (S/R levels), bullish_divergence, label and free-text `notes`. A dedicated `reasoning` field (1–3 sentences written by Crypto Research) is a candidate v0 addition.
- *Open question:* what to show when the research file has no entry for a coin (RSI-only explanation?), and which label wins when the app's RSI and the research label disagree.

## 2026-10-11 — Analysis rules for labels and setups (decided) (Manuel, 2026-10-11)
These apply to both label reasoning and trade setup proposals.
- **Long bias by default** until Manuel says otherwise.
- **Supports and resistances:** look at monthly, weekly and daily levels. Higher timeframes carry more weight.
- **RSI divergences** count as a signal.
- **TOKEN/ETH chart** is checked for confluence with the USD chart.

Defaults:
- **No research entry for a coin:** the app falls back to RSI-only reasoning.
- **Conflict:** the research label beats the app's RSI chip.
- **Today only** (2026-10-11, replaces the 48 h stale rule): research labels and reasoning are used only if the labels file is dated today (the phone's local date). An older file or a missing coin falls back to RSI-only, with a small 'last analysis: <date>' line.
- Each token can carry an optional `reasoning` field (1–3 sentences) in labels v0. The app shows it when the chip is tapped.

## Label chart images (Manuel, 2026-10-11; app 13.13)
- Optional `images` array per token in `labels/latest.json`, same shape as setups: `{ "caption", "path" }`, path = `50-projects/mini-wallet-research/labels/img/<TOKEN>_<usd|eth>_<YYYY-MM-DD>.png.b64` (base64 PNG; bots push text only).
- **Two images per token:** `[0]` TOKEN/USD, `[1]` TOKEN/ETH. **ETH itself:** ETH/USD plus ETH/BTC. Captions say which (e.g. "USD · weekly", "vs ETH · daily").
- Chart contents: red rectangle = risk (entry → invalidation), green rectangle = upside (entry → target); monthly / weekly / daily S/R lines (higher timeframes heavier); RSI pane underneath with divergences marked; value / extension zones shaded. Long bias by default.
- App: the coin bottom sheet shows the charts stacked (each with its caption), the reasoning as the text above them, and the S/R text collapsed under a "Levels" expander. Only when the file is dated today; otherwise the text / RSI-only fallback.
