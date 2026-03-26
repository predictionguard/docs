#!/usr/bin/env python3
"""Merge multiple OpenAPI 3.1.0 YAML specs into a single unified spec.

Reads all YAML files from fern/openapi/ and combines their paths, components,
and security schemes into one spec suitable for Stainless SDK generation.
"""

import glob
import sys
from pathlib import Path

import yaml


def merge_specs(input_dir: str, output_path: str) -> None:
    spec_files = sorted(glob.glob(f"{input_dir}/*.yaml"))
    if not spec_files:
        print(f"No YAML files found in {input_dir}", file=sys.stderr)
        sys.exit(1)

    merged = {
        "openapi": "3.1.0",
        "info": {
            "title": "Prediction Guard API",
            "description": "The Prediction Guard API provides AI-powered language services including chat completions, embeddings, reranking, tokenization, safety checks, document extraction, audio transcription, and MCP server integration.",
            "version": "1.2",
        },
        "servers": [
            {"url": "https://api.predictionguard.com", "description": "Production"},
        ],
        "security": [{"bearerAuth": []}],
        "paths": {},
        "components": {
            "securitySchemes": {
                "bearerAuth": {
                    "type": "http",
                    "scheme": "bearer",
                    "bearerFormat": "JWT",
                }
            },
            "schemas": {
                "Error": {
                    "type": "object",
                    "properties": {
                        "error": {
                            "type": "string",
                            "description": "Description of the error.",
                        }
                    },
                }
            },
        },
    }

    for spec_file in spec_files:
        print(f"Merging: {Path(spec_file).name}")
        with open(spec_file) as f:
            spec = yaml.safe_load(f)

        if not spec or "paths" not in spec:
            print(f"  Skipping (no paths found)")
            continue

        # Merge paths
        for path, methods in spec["paths"].items():
            if path in merged["paths"]:
                merged["paths"][path].update(methods)
            else:
                merged["paths"][path] = methods

            # Add operationId to each method if missing
            for method, operation in methods.items():
                if isinstance(operation, dict) and "operationId" not in operation:
                    # Generate operationId from path and method
                    parts = path.strip("/").replace("{", "").replace("}", "").split("/")
                    op_id = "_".join(parts)
                    if method != "get" and method != "post":
                        op_id = f"{method}_{op_id}"
                    elif method == "get":
                        op_id = f"list_{op_id}" if "{" not in path else f"get_{op_id}"
                    else:
                        op_id = f"create_{op_id}"
                    operation["operationId"] = op_id

        # Merge component schemas
        if "components" in spec and "schemas" in spec["components"]:
            schemas = spec["components"]["schemas"]
            if schemas:
                for name, schema in schemas.items():
                    if schema:
                        merged["components"]["schemas"][name] = schema

    # Fix common spec issues before writing
    _fix_spec(merged)

    with open(output_path, "w") as f:
        yaml.dump(merged, f, default_flow_style=False, sort_keys=False, allow_unicode=True)

    path_count = len(merged["paths"])
    print(f"\nMerged {len(spec_files)} specs into {output_path}")
    print(f"Total paths: {path_count}")


def _fix_spec(spec: dict) -> None:
    """Walk the spec tree and fix common OpenAPI issues."""
    _walk_fix(spec)


def _walk_fix(obj, parent=None, key=None):
    if isinstance(obj, dict):
        # Fix `items` that is a list instead of an object (invalid OpenAPI).
        # e.g. items: [{ type: string }] -> items: { type: string }
        if "items" in obj and isinstance(obj["items"], list) and len(obj["items"]) > 0:
            obj["items"] = obj["items"][0]

        # Fix bare property values like `name: string` that should be
        # `name: { type: string }` when they appear inside a `properties` block.
        if key == "properties" and parent and isinstance(parent, dict):
            for k, v in list(obj.items()):
                if isinstance(v, str) and v in ("string", "integer", "boolean", "number"):
                    obj[k] = {"type": v}

        for k, v in obj.items():
            _walk_fix(v, obj, k)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            _walk_fix(v, obj, i)


if __name__ == "__main__":
    repo_root = Path(__file__).resolve().parent.parent
    input_dir = repo_root / "fern" / "openapi"
    output_path = Path(__file__).resolve().parent / "openapi.yaml"
    merge_specs(str(input_dir), str(output_path))
