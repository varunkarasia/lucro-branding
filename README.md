# lucro_branding

Tiny Frappe app that white-labels the ERPNext desk and portal with the Lucro
brand (palette + font in [../../docs/branding.md](../../docs/branding.md)).

What it brands:
- Navbar (teal), primary buttons, links, login page, browser favicon, splash
- Font: Plus Jakarta Sans everywhere
- App logo (drop the real files in `lucro_branding/public/images/`:
  `lucro-logo.png` — get a transparent-background original from marketing —
  and `favicon.png` 32×32)

What it does NOT cover (configure in the UI instead):
- Letter Head + invoice print formats → docs/customization.md §2
- Email footer branding → Settings → Email Template

## Install

Push this folder to a git repo (e.g. `github.com/lucro/lucro_branding`), add it
to `docker/apps.json`:

```json
{ "url": "https://github.com/lucro/lucro_branding", "branch": "main" }
```

and rebuild the image (`docker/build.sh`). For a quick trial without a rebuild:

```bash
docker compose exec backend bench get-app /path/to/lucro_branding
docker compose exec backend bench --site $SITE_NAME install-app lucro_branding
```

Also set in the UI after install: Settings → Navbar Settings → upload logo,
and Website Settings → App Name "Lucro ERP".
