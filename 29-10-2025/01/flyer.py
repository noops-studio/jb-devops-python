#!/usr/bin/env python3
# plan_outline.py
# Draws ONLY the outer outline (perimeter) of a plan in your bash shell.
# No external libs. Supports arbitrary polygon points, scaling, and margin.

import sys
import math
import argparse

def parse_points(s: str):
    pts = []
    for token in s.strip().split():
        x, y = token.split(",")
        pts.append((float(x), float(y)))
    if len(pts) < 3:
        raise ValueError("Need at least 3 points for a polygon.")
    return pts

def bounds(points):
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    return min(xs), min(ys), max(xs), max(ys)

def bresenham_line(x0, y0, x1, y1):
    """Integer Bresenham from (x0,y0) to (x1,y1). Returns list of (x,y)."""
    points = []
    dx = abs(x1 - x0); dy = -abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx + dy
    x, y = x0, y0
    while True:
        points.append((x, y))
        if x == x1 and y == y1:
            break
        e2 = 2 * err
        if e2 >= dy:
            err += dy
            x += sx
        if e2 <= dx:
            err += dx
            y += sy
    return points

def rasterize_polygon_outline(points, scale=2, margin=2, ch="█"):
    # normalize & scale to grid
    xmin, ymin, xmax, ymax = bounds(points)
    # avoid negative – shift to zero
    shifted = [((p[0]-xmin), (p[1]-ymin)) for p in points]
    # scale to integer grid
    scaled = [(int(round(px*scale)), int(round(py*scale))) for px, py in shifted]

    # canvas size
    w = max(p[0] for p in scaled) + 1 + margin*2
    h = max(p[1] for p in scaled) + 1 + margin*2
    # build blank canvas
    cvs = [[" " for _ in range(w)] for _ in range(h)]

    def put(x, y, c):
        if 0 <= x < w and 0 <= y < h:
            cvs[y][x] = c

    # draw each edge (including last->first)
    for i in range(len(scaled)):
        x0, y0 = scaled[i]
        x1, y1 = scaled[(i+1) % len(scaled)]
        # offset by margin
        pts = bresenham_line(x0+margin, y0+margin, x1+margin, y1+margin)
        for (x, y) in pts:
            put(x, y, ch)

    return "\n".join("".join(row) for row in cvs)

def main():
    ap = argparse.ArgumentParser(
        description="Draw only the OUTER OUTLINE of a plan (polygon) in the terminal."
    )
    ap.add_argument("--poly", required=True,
        help='Space-separated "x,y" points. Example: "0,0 12,0 12,4 16,4 16,12 0,12"')
    ap.add_argument("--scale", type=float, default=2.0,
        help="Scale factor (pixels per unit). Default 2.0")
    ap.add_argument("--margin", type=int, default=2,
        help="Margin around drawing in characters. Default 2")
    ap.add_argument("--char", default="█",
        help="Character for outline. Good options: █ # * ▓. Default █")
    args = ap.parse_args()

    pts = parse_points(args.poly)
    art = rasterize_polygon_outline(pts, scale=args.scale, margin=args.margin, ch=args.char)
    print(art)

if __name__ == "__main__":
    main()