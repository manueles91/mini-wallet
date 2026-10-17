# Mini Wallet — crypto research (source of truth)

This folder is the source of truth for the per-token analysis and labels that Mini Wallet displays. Structure only for now: no bot wiring and no leverage build yet.

## Plan (Manuel, 2026-10-10)
1. **Richer Liquid-card labels.** The research bot (Crypto Research) runs a daily routine using its full toolkit: RSI, USD-chart and ETH-chart supports/resistances (monthly and weekly), and bullish divergence. The bot's workflow is refined to match Manuel's thesis.
2. **This repo is the source of truth.** The bot writes a daily analysis and a label per token here, and Mini Wallet reads it. Since Mini Wallet 13.15 (2026-10-15) the app's labels come only from live price vs the per-token `thresholds` in `labels/latest.json` (24h rolling); there is no RSI fallback (older apps used RSI-only bands).
3. **Two-way flow on the Leverage page.** A section that stays hidden until needed shows proposed setups from the same analysis. Manuel decides and executes in his wallet, and the result flows back through on-chain data.

## Layout
- `labels/latest.json`: current label per token (what the app reads).
- `labels/YYYY-MM-DD.json`: daily snapshot, same schema.
- `analysis/YYYY-MM-DD.md`: the bot's daily write-up.
- `setups/latest.json`: proposed setups (empty until the bot writes one; `setups/img/` for chart images as `.png.b64`).
- `holdings/latest.json`: per-token exposure snapshot (`mw-holdings/0`) so Crypto Research labels only coins with more than $500 of exposure. Per token: `usd` (spot incl. locked/staked/collateral minus loans, VELO folded into AERO), `liquid_usd`, `lev_usd` (perp notional + option delta-notional, signed), `total_usd` = usd + |lev_usd|; `errors` lists failed sources. Built on the box by `/workspace/mini-wallet-snapshot/snapshot.sh --push` (reuses the app's Kotlin readers). Manual holdings live only on the phone and aren't included unless put in `manual.txt` next to the script.
- `schema/labels.v0.json`: label schema below.
- `schema/setups.v0.json`: setups schema (`mw-setups/0`), see below.

## Label schema v0 (thin)
Per token:
- `rsi`: 14-day Wilder RSI value plus state (`overbought` ≥70, `warm` 55–70, `neutral` 45–55, `cool` 30–45, `oversold` ≤30).
- `usd_sr`: monthly, weekly and (optional, added 2026-10-11) daily support and resistance levels on the USD chart.
- `eth_sr`: monthly, weekly and optional daily support and resistance levels on the TOKEN/ETH chart.
- `bullish_divergence`: true/false, plus the timeframe.
- `label`: the short action text shown in the app.
- `reasoning` (optional, added 2026-10-11): 1–3 sentences explaining the label, shown when the chip is tapped. Older files without it stay valid.
- `notes`: free text.

Open questions: Manuel's thesis rules for combining the signals into one label; how labels are fetched (setups already use a device-stored read token, see below); and how often the bot runs.

## Analysis rules (Manuel, 2026-10-11)
These apply to both label reasoning and trade setup proposals.
- **Long bias by default** until Manuel says otherwise.
- **Supports and resistances:** look at monthly, weekly and daily levels. Higher timeframes carry more weight.
- **RSI divergences** count as a signal.
- **TOKEN/ETH chart** is checked for confluence with the USD chart.

Defaults:
- **No research entry for a coin:** the app falls back to RSI-only reasoning.
- **Conflict:** the research label beats the app's RSI chip.
- **Today only:** research is used only if the labels file is dated today (phone's local date); otherwise RSI-only with 'last analysis: <date>'.
- Each token can carry an optional `reasoning` field (1–3 sentences) in labels v0. The app shows it when the chip is tapped.

## Setups schema v0 (`mw-setups/0`)
File: `setups/latest.json`, schema `schema/setups.v0.json`. Mini Wallet 13.8+ shows it on the Leverage page as "Proposed setups", hidden unless at least one setup is valid, unexpired and `proposed`. Read-only: proposals only; Manuel decides and executes in his wallet, and results flow back through on-chain data.

```json
{ "schema": "mw-setups/0", "date": "YYYY-MM-DD",
  "setups": [ { "id": "...", "token": "ETH", "direction": "long|short", "instrument": "perp|option|spot",
    "summary": "<=100 chars", "entry": 0, "stop": 0, "targets": [0], "risk_reward": 3.2,
    "confidence": "medium|high|very_high", "hypothesis": "markdown",
    "images": [ { "caption": "...", "path": "50-projects/mini-wallet-research/setups/img/<name>.png.b64" } ],
    "created": "ISO-8601", "expires": "ISO-8601", "status": "proposed|taken|dismissed" } ] }
```
App rules: confidence other than medium / high / very_high (e.g. low, very_low) -> ignored; past `expires` -> hidden; only `proposed` shown; missing required fields or bad direction/instrument -> ignored. Images live under `setups/img/`. **Bots must push them as `<name>.png.b64`** (base64 text of the PNG, e.g. `base64 -w0 chart.png`), because the GitHub connectors can only push text; the app (13.8.1+) decodes them on the device. Plain `.png` still works if pushed some other way. Fetched with the same token. Access: GitHub Contents API with the phone's "GitHub read token" (fine-grained, read-only, this repo), cached 1 h. `setups/` is intentionally empty (no fake trades); the app's tests use a local fixture.

## Label chart images (Manuel, 2026-10-11; app 13.13)
- Optional `images` array per token in `labels/latest.json`, same shape as setups: `{ "caption", "path" }`, path = `50-projects/mini-wallet-research/labels/img/<TOKEN>_<usd|eth>_<YYYY-MM-DD>.png.b64` (base64 PNG; bots push text only).
- **Two images per token:** `[0]` TOKEN/USD, `[1]` TOKEN/ETH. **ETH itself:** ETH/USD plus ETH/BTC. Captions say which (e.g. "USD · weekly", "vs ETH · daily").
- Chart contents: red rectangle = risk (entry → invalidation), green rectangle = upside (entry → target); monthly / weekly / daily S/R lines (higher timeframes heavier); RSI pane underneath with divergences marked; value / extension zones shaded. Long bias by default.
- App: the coin bottom sheet shows the charts stacked (each with its caption), the reasoning as the text above them, and the S/R text collapsed under a "Levels" expander. Only when the file is dated today; otherwise the text / RSI-only fallback.

## Price-threshold labels (added 2026-10-15, Mini Wallet 13.15)
Each token now carries `thresholds` = `{base, down:[{label, price}], up:[{label, price}], ref_price, valid_from, valid_until}`, plus top-level `valid_from`/`valid_until` (24h rolling).
- The app's chip comes **only** from live price vs these levels: price ≤ a `down` level → that label (deepest crossed wins, e.g. Consider adding → Deep value); price ≥ an `up` level → that label (Getting warm → Take profit); else `base` (Neutral).
- No RSI fallback. After 36h without a new file, the app keeps the last thresholds and shows the label as "… · old" (muted). Coins not in the file get no chip.
- `label` stays as the label at `ref_price` (the analysis' call at publish time) and must equal the threshold result there.
- Defaults are derived from the USD S/R by `label_thresholds()` in the box's `daily_watchlist.py`; the analyst can override per token.

### Required step for the daily labels run (runbook)
Before writing `labels/YYYY-MM-DD.json` and `labels/latest.json`, the generator must call
`sys.path.insert(0, "/workspace/mwlabels"); import thresholds_guard; thresholds_guard.ensure(out, r)` (r = raw-<DAY>.json).
It adds `thresholds` + `valid_from`/`valid_until` when missing and fails if any `label` differs from `label_for_price(ref_price)`; fix by passing `overrides={SYM: {"down": [...], "up": [...]}}` with the analysis' own levels. Copy the latest `gen-*.py` (it already contains this line) and never publish a file without `thresholds`.
