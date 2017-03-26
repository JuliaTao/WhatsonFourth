# Partial data

`washington_hikes.csv` has the first 30 trails. It has the `description` field for trails, but the `latlong` is a single field with the latitude and longitude coordinates embedded in a URL.

`washington_hikes-pp001-015.csv` has the first 450 trails scraped from the first 15 of 113 total pages on the web site. It does _not_ have a `description` field, but it separates the latlong coordinates into two separate fields, `lat` and `long`.
