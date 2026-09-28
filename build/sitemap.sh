#!/bin/sh
set -eu

dir=${1:-book/html}
base=https://$(cat CNAME)

find "$dir" -name '*.html' ! -name 404.html ! -name print.html ! -name toc.html |
    sed -e "s|^$dir/||" -e 's|^index\.html$||' |
    sort |
    {
        echo '<?xml version="1.0" encoding="UTF-8"?>'
        echo '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        while read -r page; do
            echo "  <url><loc>$base/$page</loc></url>"
        done
        echo '</urlset>'
    } > "$dir/sitemap.xml"
