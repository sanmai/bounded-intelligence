# A Field Guide to Bounded Intelligence

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18786332.svg)](https://doi.org/10.5281/zenodo.18786332)

Source for [boundedintelligence.com](https://www.boundedintelligence.com)

Built with [mdBook](https://rust-lang.github.io/mdBook/).

## File Structure Convention

The book uses zero-padded hyphenated numbered part directories with zero-padded hyphenated numbered section files:

```
src/
  SUMMARY.md              # Table of contents (source of truth for order)
  01-introduction/
    01-life-within-bounds.md
    02-ground-rules.md
  02-interactions/        # 4 interactions
    01-*.md
  03-functions/           # 8 functions
    01-*.md ...
  04-cascades/            # 16 cascades
    01-overview.md
    02-list.md
    03-attributes/        # 15 cascade attributes
      01-*.md ...
  05-supervisory/         # Supervisory cascades
    01-overview.md
    02-list.md
    03-attributes/        # 31 supervisory attributes
      01-*.md ...
```

### Conventions

- **Parts**: `NN-part-name/` (zero-padded, lowercase, hyphenated)
- **Sections**: `NN-section-name.md` (zero-padded to 2 digits)
- **Subdirectories**: For grouping related content (e.g., attributes)
- **Zero-padding**: I use `01-` through `31-` for consistent sorting

The numbering is for filesystem navigation convenience, where SUMMARY.md defines the actual reading order.

### Accessibility

Links should be full sentences or at least two long words for easier navigation.

## Build Commands

```bash
make build
make serve
```

