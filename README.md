# Mini Wallet

A personal, read-only crypto portfolio widget for Android (built for Samsung Galaxy / One UI).

Four home-screen widgets, each resizable. The app's main screen shows all four as a dashboard, with the detailed breakdown and settings below.
- **Mini Wallet: Exposure**: donut chart of whole-portfolio exposure by coin, with net worth in the center and a legend of %/$. Coverage: EVM wallets; Base protocols (Aerodrome veAERO, 40 Acres collateral net of debt, Beefy CLM, Venice, Bankr, veVIRTUAL); Optimism VELO (counted inside AERO); Derive stDRV; Hyperliquid perps at notional (tagged PERP); plus optional manual holdings.
- **Mini Wallet: Performance**: net worth, 24h $ and % change, change since last refresh, and a sparkline of net worth history (stored on the phone).
- **Mini Wallet: Movers**: 24h % change per coin as diverging bars, with the $ impact on the portfolio.
- **Mini Wallet: Hyperliquid**: a mini card per isolated perp position showing side and leverage, margin, uPnL $ and %, a liquidation-distance bar colored by health (green >25%, amber 10–25%, red <10%), and entry vs mark.
- Manual refresh button, plus automatic refresh about every 30 minutes. The app checks this repo daily for updates.

Read-only. You enter a **public** wallet address on first launch. No private keys, seed phrases, accounts, or analytics. Data comes only from free public sources: the Hyperliquid info API, Blockscout (Ethereum), public chain RPCs (incl. Base protocol contract reads), and DefiLlama prices.

## 13.14 — Privacy mode: all leverage cards (Overview leverage, Leverage page perps/options, section headers, per-position 24h/7d) show PnL as % — of margin for perps, premium paid for options, leverage value for totals — instead of $•••.

## 13.13 — Coin bottom sheet: when today's research label has chart images (USD + TOKEN/ETH; ETH: USD + ETH/BTC), they're shown stacked with captions under the reasoning, cached on device; S/R text collapses under a "Levels" expander. Otherwise the text / RSI-only fallback. Privacy mode: Overview Leverage card PnL and rows as %. veAERO card: removed the empty gap.

## 13.12 — Privacy mode: tap the MINI WALLET wordmark (top-left) to mask every $ amount and quantity (•••); % and prices stay; the Performance chart switches to % from range start; stay-vs-switch shows % gain; the widget eye uses the same global state. Liquid card: dedicated tappable signal-pill column + 24h/7d % per row. veAERO card: countdowns + recommended pools only (current split behind a flag). Widgets: follow the app 24h/7d setting, tap the widget title to flip it for all widgets; Exposure widget chip cycles All → Liquid → No AERO.

## 13.11 — Liquid card signal chips are tappable: a bottom sheet shows the research label, reasoning, RSI, M/W/D supports/resistances (USD and TOKEN/ETH), divergence and file date. Research labels override the RSI chip only when the file is dated today (phone's local date); otherwise (older file, coin missing, no token) → RSI-only explanation with 'last analysis: <date>'. Labels read with the same device token as setups, cached 1 h.

## 13.10.1 — Leverage page: when the setups file loads fine but has no qualifying proposals, a discreet one-liner (file's note, else 'No active proposals at the moment') takes the section's place. No token / fetch failure: unchanged.

## 13.10 — Spot page: Liquid card first (always unfiltered), then veAERO votes (collapsed by default, header shows voting power + switch gain), then Total exposure with its own 'AERO' switch (filters only that card).

## 13.9.1 — veAERO card: 'Recommended this epoch' from AeroAllocator's free /api/allocation (voter_roi) for votable power (40 Acres locks excluded); current vs recommended split, votes, expected $/epoch, stay vs switch. Hidden if the API is down (6 h cached fallback) and after Aero launch.

## 13.9 — Spot page: read-only veAERO votes card (Aerodrome Sugar via Base RPC + DefiLlama; no Zerion). Voting power, locks, vote split with $/1k votes last epoch, voted-this-epoch, epoch-flip and Aero-launch countdowns; 40 Acres locks shown as managed. After Oct 22 it switches to sAERO Predictive Allocation status (47h cooldown).

## 13.8.1 — Setup chart images can be base64 text (.png.b64), decoded on the device; plain .png still works

## 13.8 — Proposed setups on the Leverage page (read-only, from the private research repo via a device-stored GitHub read token); Spot page 'Include AERO' switch

## 13.7.3 — RSI signal chips on Liquid portfolio rows + Show all; shared 24h/7d toggle on Overview and Leverage; Spot exposure centre = spot $; leverage exposure grouped by token (at-risk share)

## 13.7.2 — Leverage page: per-position exposure bars (size = notional / Δ-notional, colour = health); Leverage and Movers widgets: names sized to content, bars take the spare width

## 13.7.1 — Leverage page: perp gauge labels (LIQ, SAFE, Entry, mark) laid out without overlaps; options cards reworked (index vs strike + days first, value vs at risk + health bar, muted greeks)

## 13.7 — Derive options fetched automatically
- For each enabled address: Derive public get_subaccounts → get_trade_history per subaccount (paginated) → net quantity and average cost per option; expired ones dropped; marked live via get_tickers. Cached 15 min.
- Manual OPTION DERIVE lines are removed once auto-fetch succeeds; if Derive is unreachable, saved manual lines are used. CASH DERIVE stays manual (not public).

## 13.6.2 — Locked VIRTUAL from Zerion
- With a Zerion key, the Virtuals Protocol VIRTUAL lock is read from Zerion; a saved manual "VIRTUAL … locked" line is migrated out once (kept if no key is set) and ignored at runtime, so it's never counted twice.
- Removed the unused veVIRTUAL stakedAmountOf reader.

## 13.6.1 — Fix 'Some sources failed' after adding the Zerion key
- Zerion calls are serialised app-wide (≥1.1 s apart) and retried on 429 with 2/4/8 s backoff; only one refresh runs at a time (app, widget ↻ and background no longer collide).
- Pasted key is cleaned (spaces, newlines, quotes); a rejected key says so.
- If Zerion or DefiLlama fails, the last good data is kept and a muted note says so; amber warnings name the failed source and reason.

## 13.6 — Any EVM address (optional Zerion API key)
- Settings: several addresses (add / remove / enable each) and an optional "Zerion API key" field, stored on the phone only. Blank key = built-in readers as before.
- With a key: Zerion wallet + DeFi positions (deposits, staking, locks, rewards; loans negative) fill the spot breakdown; built-in readers still win for Hyperliquid, Derive, 40 Acres, veAERO/veVELO, locked VIRTUAL, stDRV, Superform, Beefy, Venice, Bankr (no double counting). Dust under $1 hidden. Zerion 24h % used for Movers.
- Budget: 1 call per address per refresh, cached 15 min; pull / tap refresh bypasses the cache at most once a minute; backs off at 280 calls/day (counter in Settings).

## 13.5.6 — Exposure widget: All | Liquid chip (liquid = spot liquid holdings only, no leverage)

## 13.5.5 — exposure legend: 24h Δ = change in share of total exposure (pp); Movers card + widget: name + price (green/red by 24h), right column holding $ (±$ change); hidden mode price coloured too

## 13.5.4 — widgets: one shared eye state (Exposure included); hidden mode shows no $ except prices (Leverage %, Movers %); Movers widget: name (±$), 24h % on bars, holding $ · price on the right

## 13.5.3 — Exposure widget eye (own state, hidden by default); exposure legend: coin 24h % instead of spot %; leverage headers show 24h PnL; perp bars mark entry price

## 13.5.2 — larger widget fonts; Leverage widget header: total left, PnL right; Total exposure centre = net worth; perp mark price centred above the marker; eye button on Movers/Performance/Leverage widgets hides the big total ($•••••, hidden by default)

## 13.5.1 — pull-to-refresh easier (~150dp); Movers widget rows fill the real height; Leverage widget = concise rows (name · health · 24h · PnL); Overview Leverage card column labels, no header 24h total; perp gauges: mark price at the marker, liq price only at the LIQ end; widget picker preview images (sample data)

## 13.5 — slide animation between pages; pull-to-refresh needs a long deliberate pull; press-and-drag the Net worth chart to scrub; Overview Leverage card: 24h change per position + header, red→green health bars (perps: distance to liq, ≥50% = green; options: probability of finishing past break-even, ≥50% = green)

## 13.4 — movers: holding $ next to coin, price (% chg) column, $ change on bars (% scale, %/$ toggle removed); swipe left/right between pages; ↻ refresh button on every widget

## Install (sideload)
1. Get the APK: this repo stores it as base64 text (`mini-wallet.apk.b64`, SHA-256 in `version.json`). Decode it with `base64 -d mini-wallet.apk.b64 > mini-wallet.apk`, or use a direct APK link if you were given one, then open it on your phone.
2. If prompted, tap **Settings → Allow from this source**, then **Install** (tap "Install anyway" if Play Protect warns; Samsung Auto Blocker may need to be off).
3. Open Mini Wallet and paste your public `0x…` address. Optional: under Manual holdings, add one line per holding in the form `COIN AMOUNT label` (e.g. `ETH 1.5 cold wallet`), then tap Save & refresh. This is stored only on your phone.
4. Long-press the home screen → **Widgets** → **Mini Wallet** → add Spot and/or Hyperliquid, and resize as you like.
5. Optional: Settings → Apps → Mini Wallet → Battery → **Unrestricted** so background refresh isn't delayed.

Updates: the app checks every time you open it, and there's also a Check for updates button that shows your current version and the last result. When a new version is published here, the app shows a notification and a banner. Tap it to download and install. The app decodes the base64 file and checks its SHA-256 before installing.

Not covered: protocols other than those listed (e.g. Aave, Arcadia, Superform, Spectra, Avantis), long-tail tokens outside Ethereum, and options (Derive needs a signed API session).

## v6
- Net worth = **Spot** (holdings − loans, no perps) + **Leverage** (Hyperliquid margin + uPnL + option marks + venue cash).
- Widgets: Spot exposure, Performance, Movers (spot coins), **Leverage** (perps + options).
- Superform SuperVaults (Base) read on-chain: SPCX, TSLA.
- Manual holdings also accept:
  - `OPTION DERIVE <instrument> <qty> @<avg cost>` (live mark/delta from Derive public ticker; Black-Scholes fallback at 60% IV)
  - `CASH DERIVE <usd>`

## v7
- Option marks now come from Derive V3 public tickers (`https://api.derive.xyz/v3/public/get_tickers`, field `M`). The legacy V2 host was frozen and returned stale marks.
- New app layout: bottom navigation (Overview, Spot, Leverage, Settings), pull-to-refresh, tap a coin to expand its venues.

## v8
- Performance: 24h / 7d toggle; one snapshot per 30-min slot; until 7 days of real history exist, the older part is estimated from current holdings × DefiLlama historical prices (shown faded, labeled "est.").
- Movers: 24h / 7d, % vs $, sort by change or by weight. Choices persist; widgets use defaults (24h, %, by change).
- Liquid portfolio card (Spot page): wallet tokens, HL spot, withdrawable vaults (Beefy, Superform) + free cash (HL withdrawable, Derive cash). Excludes locks, loan collateral, staking with cooldown.
- Leverage: Perps and Options sections with subtotals; distance-to-liquidation gauge LIQ → WATCH → SAFE with marker and trend vs previous refresh.
- Auto-refresh every 30 min and on app open; pull-to-refresh. Refresh buttons removed: tap a widget to open the app (which refreshes).

## v9
- Strict separation: Spot shows only spot holdings; Liquid card is spot-only (wallet tokens, HL spot non-stable tokens, withdrawable vaults). HL USDC (margin + free) and Derive cash are Leverage only.
- Liquidation zones from one shared rule: <10% LIQ red, 10–25% WATCH amber, ≥25% SAFE green; trend arrow is neutral.
- Positions show liquidation and mark prices; options show mark vs cost, underlying spot and strike, "no liq (max loss = premium)".
- Movers: right-hand $ column removed. New bottom navigation with drawn icons.

## v10
- Pages start directly with cards (no big titles). Leverage page: Leveraged exposure above Value composition. Gauge legend matches the neutral trend arrow.

## v11
- Updater reads version.json via the GitHub contents API (`Accept: application/vnd.github.raw`), falling back to raw.githubusercontent; if the raw APK download fails or its SHA-256 mismatches (stale CDN), it re-downloads `mini-wallet.apk.b64` via the contents API.
- Overview: Performance + total Portfolio exposure (spot coins + Leverage slice). Holdings, Value composition and About are collapsible. Perps sorted by margin.

## v12
- Overview: Performance + Movers. Movers right column: in % view shows $ impact, in $ view shows % move.
- Spot donut larger (up to 9 legend rows). Options sorted by mark value. Update banner and Check-now buttons ≥56dp and below the status bar.

## v13
- Overview: net-worth header (24h/7d sparkline), Spot summary, Leverage summary (one row per position, max 6 + "+N more"). Tap a card to open its page.
- Exposure donut toggle Spot | Total (default Total, widget too): total = spot + signed perp notional + option delta × qty × underlying; stables/margin excluded; centre shows gross exposure and × net worth.
- Movers (card + widget): spot total + change header, token quantity under each coin.
- v13.1: Movers defaults (app without saved choice, and widget): sorted by weight, 24h, $ values.
- v13.2: Overview Spot card shows a labeled Liquid | Locked/staked split bar (loans netted on the locked side).
- v13.2: Overview Spot card coin line and mini donut show total exposure shares (incl. leverage); $ amounts stay spot.
- v13.2: option rows show θ $/day for the whole position (Derive V3 ticker option_pricing.t × qty; Black-Scholes fallback marked est.). Exposure card/widget is total-exposure only, legend shows total % and spot % (no $), no toggle.
- v13.2 layout: Overview = Net worth + Movers + Leverage summary; Spot page = Spot summary, Total exposure, Liquid, Holdings. Movers right column = position $ value (change $); defaults weight / % / 24h (saved movers toggles reset once on upgrade).
- v13.3: Overview option rows: break-even move at expiry, (strike + premium) / ETH index − 1. Movers header: "PnL ±$x" (24h/7d). Total exposure card: centre = spot value and gross exposure ÷ spot (no other $ on the card); Spot summary card removed from the Spot page.
- v13.3: Movers show each coin's current price next to its name; Liquid portfolio card starts with the Liquid | Locked/staked split bar.
