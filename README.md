# Lab: Web Scraping
[click here to see the code](web_scraper/scraper.py)

[click here to see the tester](tests/test_web_scraper.py)
## Overview
It’s wonderful when someone has gone to the effort to expose their site’s data through an API.

But not everyone can (or wants to) do that.

No problem. Let’s code up a web scraper that can automate the process of manually using the site.

## Feature Tasks and Requirements
- Scrape a Wikipedia page and record which passages need citations.
    - E.g. Battle of the Bulge has 9 “citation needed” cases, as of this writing.
- Your web scraper should report the number of citations needed.
- Your web scraper should identify those ten cases AND include the relevant passage.
    - E.g. Citation needed for “lorem spam and impsum eggs”
    - Consider the “relevant passage” to be the paragraph where it is found.

## Implementation Notes
- Count function must be named get_citations_needed_count
    - get_citations_needed takes in a url and returns an integer
- Report function must be named get_citations_needed_report
    - get_citations_needed_report takes in a url and returns a string
    - the string should be formatted with each citation needed on own line, in order found.
- Module must be named scraper.py

