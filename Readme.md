A standalone local-only dashboard for Linz Netz CSV file exports.

# Usage

* Login into your Linz Netz account, goto `Verbrauchsdaten` and select any range of data in either quarter-hourly or daily aggregation.
* Choose to export the data as CSV file.
* Open the linz-netz-analyse.html (or it's CDN variant) html file in your browser.
* Choose the previously exported CSV file.

# Development

Features, Fixes and other changes go into the [](linz-netz-analyse_cdn.html) file.

To generate a fully standalone variant, use the provided script, that will replace the necessary `<script ...>` tags with the pre-downloaded content.

```sh
python -m venv .venv
. .venv/bin/activate
python make-standalone.py linz-netz-analyse_cdn.html linz-netz-analyse.html
```
