"""Plan entry (258 chars): sell a specific done-for-you speed fix to Shopify stores."""

import os

TEXT = "Sell $99 Shopify speed fixes: find sub-50 PageSpeed stores, email 50 owners/day offering a 2-hour script fix (image compression + lazy-load), invoice via Stripe, deliver in 48h. Day 1: scan 200 stores, email 50. Edge: owners see the score jump before paying."

def main():
    text = TEXT
    n = len(text)
    assert 1 <= n <= 280, f"entry must be 1-280 code points, got {n}"
    assert text.strip(), "entry must not be whitespace-only"
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod(path, 0o644)
    print(f"wrote {n} code points to {path}")

if __name__ == "__main__":
    main()
