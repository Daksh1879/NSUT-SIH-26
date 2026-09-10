# main.py
import argparse, json, sys
from fastapi import FastAPI
from pathlib import Path
from schemas.ocr_region import OCRRegion, BoundingBox
from classifier.classifier import classify_regions
from engine.rule_engine import run_rule_engine
from dataclasses import asdict

def load_ocr_json(path: str):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    return [
        OCRRegion(
            region_id=r["region_id"],
            raw_text=r["raw_text"],
            confidence=r["confidence"],
            bounding_box=BoundingBox(**r["bounding_box"]),
            estimated_font_size_pt=r.get("estimated_font_size_pt"),
            language=r.get("language"),
        )
        for r in data["regions"]
    ]

def main():
    parser = argparse.ArgumentParser(description="Legal Metrology Compliance Checker")
    parser.add_argument("--input", required=True, help="Path to OCR JSON file")
    parser.add_argument("--weight", type=float, default=500, help="Net weight in grams")
    parser.add_argument("--output", default=None, help="Output JSON path (optional)")
    args = parser.parse_args()

    regions = load_ocr_json(args.input)
    declarations = classify_regions(regions)
    report = run_rule_engine(declarations, product_context={"net_weight_g": args.weight})

    print("\n" + "="*60)
    print(report.summary)
    print(f"\nTotal Violations : {len(report.violations)}")
    print(f"Compliance Score : {report.compliance_score}/100")
    print(f"Status           : {'✅ COMPLIANT' if report.is_compliant else '❌ NON-COMPLIANT'}")
    print("="*60)

    if args.output:
        out = {
            "scan_id": report.scan_id,
            "compliance_score": report.compliance_score,
            "is_compliant": report.is_compliant,
            "violations": [
                {
                    "rule_id": v.rule_id,
                    "field": v.field,
                    "type": v.violation_type,
                    "penalty_class": v.penalty_class,
                    "description": v.description,
                    "suggested_correction": v.suggested_correction,
                }
                for v in report.violations
            ]
        }
        Path(args.output).write_text(json.dumps(out, indent=2), encoding="utf-8")
        print(f"\nReport saved to: {args.output}")

if __name__ == "__main__":
    main()
