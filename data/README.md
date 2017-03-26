# Partial data

Data was scraped from HTML on the [Washington Trails Association](http://www.wta.org/go-outside/hikes?b_start:int=0) web site, which has 113 pages of trailheads, showing 30 trails per page.

`washington_hikes.csv` has the first 30 trails. It has the `description` field for trails, but the `latlong` is a single field with the latitude and longitude coordinates embedded in a URL.

`washington_hikes-pp001-015.csv` has the first 450 trails scraped from the first 15 of 113 total pages on the web site. It does _not_ have a `description` field, but it separates the latlong coordinates into two separate fields, `lat` and `long`. The value `NR` appears in the `lat` or `long` field when the trail page did not have latitude and longitude coordinates on its web page. I verified that those cases were working correctly in the data that we have.
