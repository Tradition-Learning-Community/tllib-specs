# TLC-FC-13-PRACTICE-003 — Dynamics candidate representation

## What is this feature?
A deterministic structural package for four cited Practice dynamics candidates. The equations remain independent, source-addressable statements and are never numerically integrated by this package.

## What must be implemented?
Validate the exact feature identity, the four keyed opaque inputs, the ordered object population, and canonical provenance; preserve every opaque payload; construct the declarative representation; support deterministic serialization, deserialization, structural comparison, and trace inspection.

## Valid inputs and required output
The required inputs are `INPUT-PRACTICE-003-1` through `INPUT-PRACTICE-003-4`. The output preserves objects `070`, `077`, `084`, and `092` in that documentary order and exposes the corresponding unresolved output references `003-1` through `003-4`.

## Mandatory and forbidden behavior
Exact identity, complete cardinality, documentary order, opacity, round-trip preservation, deterministic canonical serialization, and atomic failure are mandatory. Numerical integration, stochastic simulation, solver selection, executable repetition, transitions, sequences, durations, progressions, or effects are forbidden.

## Implementation freedom
Language, API spelling, storage, ownership, allocation, serialization format, concurrency policy, and internal decomposition remain free when observable obligations are preserved.

## Errors and conformance
A missing input, duplicate or foreign identity, non-opaque carrier, provenance mismatch, structural failure, unsupported operation, or absent external provider must produce a stable error without a partial result. Every test in `acceptance.json` is mandatory.

## Unresolved science
Scientific execution requires an external executor and evaluation requires an external evaluator. No integration method, stochastic law, trajectory, or exact result is authorized.