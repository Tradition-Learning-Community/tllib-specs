# TLC-HC-DESCRIPTOR-ENVELOPE

Defines the common structural envelope used by declaration and descriptor features. It preserves feature identity, representation label, references, unresolved items, dependencies, provenance, and status while leaving domain-specific fields and runtime storage unconstrained.

The envelope is immutable as an observable result. It does not prescribe a programming-language type, memory layout, allocation policy, or serialization format.