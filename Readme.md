A standalone local-only dashboard for Linz Netz CSV file exports.

# Usage

* Login into your Linz Netz account, goto `Verbrauchsdaten` and select any range of data in either quarter-hourly or daily aggregation.
* Choose to export the data as CSV file.
* Open the linz-netz-analyse.html (or it's CDN variant) html file in your browser.
* Choose the previously exported CSV file.

# Monthly peaks

For quarter-hourly and hourly files the dashboard lists the peak of each month. Export quarter-hourly values for whole months to get complete results.

* Power files: the highest quarter hour in kW.
* Energy files: the highest clock hour in kWh.

Only files of the same kind (power or energy) and resolution can be loaded together.

# Development

Features, Fixes and other changes go into the [linz-netz-analyse_cdn.html](linz-netz-analyse_cdn.html) file.

To generate a fully standalone variant, use the provided script, that will replace the necessary `<script ...>` tags with the pre-downloaded content.

```sh
python -m venv .venv
. .venv/bin/activate
python make-standalone.py linz-netz-analyse_cdn.html linz-netz-analyse.html
```
