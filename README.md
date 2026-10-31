# Famti.com

A lightweight, responsive domain sale landing page for **Famti.com**.

- Public site: https://brucin.github.io/famti-domain/
- Purchase listing: https://www.godaddy.com/forsale/famti.com?locale=en-US
- Contact: w@brucin.com
- Asking price: USD 9,000, verified on the GoDaddy listing on October 31, 2026. The live marketplace listing governs the final price and terms.

## GitHub Pages

Publish the `main` branch, `/ (root)` folder in **Settings → Pages**. No build step, packages, external fonts, analytics, or API credentials are required.

## Local preview

Run `python3 -m http.server 4173 --bind 127.0.0.1` from this directory and open http://127.0.0.1:4173/.

The page is hosted separately from famti.com and does not require changes to the domain’s Afternic nameservers.

## Search and sharing

The page includes a self-referencing canonical URL, explicit index/follow metadata, an XML sitemap with an accurate last-modified date, Product/Offer and WebPage JSON-LD, visible purchase information, and a 1200×630 social preview image. The asking price must be updated in the visible page, metadata, image, and structured data together if it changes. No reviews, ratings, traffic claims, or expiry dates are invented.

Only `https://brucin.github.io/robots.txt` is authoritative for crawler rules on this hostname. The project-level `robots.txt` is informational and does not override host-level rules. Do not modify another repository to change host-level rules. Submit `https://brucin.github.io/famti-domain/sitemap.xml` through a verified URL-prefix property in Google Search Console and Bing Webmaster Tools. Do not use retired anonymous sitemap-ping endpoints. Submission and structured markup do not guarantee indexing, ranking, or rich results.

After a content change has deployed, run `python3 tools/notify-indexnow.py` to notify IndexNow participants (including Bing). The 32-character `.txt` proof in this repository is intentionally public and authorizes only URLs in `/famti-domain/`. Google submission is handled separately through Search Console. Avoid repeated submissions when the content has not changed.
