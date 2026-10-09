# Mini Wallet

A personal, read-only crypto portfolio widget for Android (built for Samsung Galaxy / One UI).

Four home-screen widgets, each resizable. The app's main screen shows all four as a dashboard, with the detailed breakdown and settings below.
- **Mini Wallet: Exposure**: donut chart of whole-portfolio exposure by coin, with net worth in the center and a legend of %/$. Coverage: EVM wallets; Base protocols (Aerodrome veAERO, 40 Acres collateral net of debt, Beefy CLM, Venice, Bankr, veVIRTUAL); Optimism VELO (counted inside AERO); Derive stDRV; Hyperliquid perps at notional (tagged PERP); plus optional manual holdings.
- **Mini Wallet: Performance**: net worth, 24h $ and % change, change since last refresh, and a sparkline of net worth history (stored on the phone).
- **Mini Wallet: Movers**: 24h % change per coin as diverging bars, with the $ impact on the portfolio.
- **Mini Wallet: Hyperliquid**: a mini card per isolated perp position showing side and leverage, margin, uPnL $ and %, a liquidation-distance bar colored by health (green >25%, amber 10–25%, red <10%), and entry vs mark.
- Manual refresh button, plus automatic refresh about every 30 minutes. The app checks this repo daily for updates.

Read-only. You enter a **public** wallet address on first launch. No private keys, seed phrases, accounts, or analytics. Data comes only from free public sources: the Hyperliquid info API, Blockscout (Ethereum), public chain RPCs (incl. Base protocol contract reads), and DefiLlama prices.

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
