# Mini Wallet

A personal, read-only crypto portfolio widget for Android (built for Samsung Galaxy / One UI).

- **Mini Wallet: Exposure** widget: whole-portfolio exposure by coin. It counts liquid wallet balances on EVM chains plus on-chain protocol positions on Base (Aerodrome veAERO locks, 40 Acres collateral net of its USDC debt, Beefy CLM vaults, Venice staking, Bankr staking, veVIRTUAL), Optimism VELO (liquid, veVELO, 40 Acres OP collateral and debt; counted inside AERO by USD value ahead of the merger), and Derive stDRV staking on Ethereum. You can also add manual holdings in the app and Hyperliquid perps at notional, with the perps financing shown as negative stables. It shows net worth, % and $ per coin, and the 24h change.
- **Mini Wallet: Hyperliquid** widget: open (isolated) perp positions, each with its own green/amber/red health dot based on its liquidation distance (>25% / 10–25% / <10%), plus total uPnL. The header dot shows the worst position.
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
