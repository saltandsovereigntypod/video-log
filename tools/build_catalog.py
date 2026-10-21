#!/usr/bin/env python3
"""Write src/oracle-catalog.json from tools/catalog_films.py.

The catalogue is reference data for the Oracle, never library data. The model
block holds the shipped weights: a starting guess on a 0-5 scale, to be
re-fitted in the app against the viewer's own ratings (Settings, Recalibrate).

    python3 tools/build_catalog.py
"""

import datetime
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from catalog_films import FILMS  # noqa: E402

PACE = {"S": "slowburn", "T": "steady", "F": "fast", "R": "relentless"}
LEAD = {"f": "female", "m": "male", "e": "ensemble"}
GENRES = {"horror", "thriller", "mystery", "crime", "scifi", "fantasy", "action",
          "comedy", "drama", "romance", "animation"}
FLAGS = {"animal-harm", "sexual-assault", "child-harm", "self-harm"}
# Not every genre tag in the source is one the filter offers; these fold in.
FOLD = {"adventure": "action", "musical": None}


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def record(f):
    genres = []
    for g in f["genres"]:
        g = FOLD.get(g, g)
        if g and g not in genres:
            assert g in GENRES, (f["title"], g)
            genres.append(g)
    for fl in f["flags"]:
        assert fl in FLAGS, (f["title"], fl)
    for k in ("impact", "craft", "fun", "darkness", "scare", "gore", "spice"):
        assert 0 <= f[k] <= 5, (f["title"], k)
    rec = {
        "id": slug(f["title"]) + "-" + str(f["year"]),
        "title": f["title"],
        "director": f["director"],
        "series": f.get("series"),
        "part": f.get("part"),
        "year": f["year"],
        "runtime": f["runtime"],
        "seriesStatus": "franchise" if f.get("series") else "standalone",
        "genres": genres,
        "lead": LEAD[f["lead"]],
        "impact": f["impact"],
        "craft": f["craft"],
        "fun": f["fun"],
        "pace": PACE[f["pace"]],
        "darkness": f["darkness"],
        "scare": f["scare"],
        "gore": f["gore"],
        "spice": f["spice"],
        "hook": f["hook"],
        "caution": f["caution"],
        "comps": f["comps"],
        "contentWarnings": [w.strip() for w in f["warnings"].split(";") if w.strip()],
        "flags": f["flags"],
        "tagConfidence": f.get("tagConfidence", "high"),
    }
    if f.get("leadNote"):
        rec["leadNote"] = f["leadNote"]
    if f.get("needs"):
        rec["prerequisite"] = {"needs": True, "needsTitle": f["needs"]}
    return rec


def main():
    catalog = [record(f) for f in FILMS]
    ids = [r["id"] for r in catalog]
    assert len(ids) == len(set(ids)), "duplicate ids"
    titles = {r["title"] for r in catalog}
    for r in catalog:
        pre = r.get("prerequisite")
        assert not pre or pre["needsTitle"] in titles, (r["title"], pre)
    out = {
        "version": 1,
        "generated": datetime.date.today().isoformat(),
        "builtFor": "Midnight Rewind: the Oracle",
        "model": {
            "dimensions": ["impact", "craft", "fun", "pace"],
            "weights": {"impact": 1.2, "craft": 1.3, "fun": 1.1, "pace": 0.8},
            "intercept": 0.6,
            "paceScale": {"relentless": 1.0, "fast": 0.85, "steady": 0.55, "slowburn": 0.25},
            "note": ("Shipped weights are a starting guess, not a fit: nobody's movie ratings were "
                     "available when the catalogue was built. Rate eight films the Oracle knows and "
                     "use Recalibrate in Settings to fit them to your own taste."),
        },
        "anchors": [],
        "catalog": catalog,
    }
    path = ROOT / "src" / "oracle-catalog.json"
    path.write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {path.relative_to(ROOT)}  ({len(catalog)} films)")


if __name__ == "__main__":
    main()
