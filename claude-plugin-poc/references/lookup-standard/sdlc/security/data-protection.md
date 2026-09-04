---
id: SEC-004
title: Data Protection Standards
phase: security
extends: null
tech: null
summary: Rules for encryption in transit and at rest, and key management.
tags: [security, encryption, data-protection, tls, at-rest, key-management]
applies_to: ["**/*"]
version: "2.0.0"
last_reviewed: "2026-07-13"
---

# Data Protection Standards (SEC-004)

## Purpose

Cryptographic failures are OWASP Top 10 A02. Improperly protected data is exposed in transit interception, storage breaches, and backup theft.

---

## MUST

- **SEC-004-01** All data in transit is encrypted using TLS 1.2 or higher, including internal service-to-service communication. HTTP without TLS is not used for any service that transmits sensitive data, credentials, or session tokens.
- **SEC-004-02** Sensitive data — including PII, credentials, financial data, and health data — is encrypted at rest at the storage layer (full-disk or database encryption) at minimum.

## MUST NOT

- **SEC-004-03** Use deprecated cryptographic algorithms for any security purpose: MD5 or SHA-1 for hashing; DES, 3DES, or RC4 for symmetric encryption; RSA keys below 2048 bits or Diffie-Hellman groups below 2048 bits for key exchange. Approved algorithms: AES-256-GCM for symmetric encryption, SHA-256 or higher for hashing, RSA-2048 or higher for asymmetric encryption.
- **SEC-004-04** Use TLS 1.0 or TLS 1.1.

## SHOULD

- **SEC-004-05** Encryption keys are managed by a dedicated KMS, stored separately from the data they protect, with automated scheduled rotation.
- **SEC-004-06** Field-level encryption is applied for the highest-sensitivity fields (national identifiers, financial account numbers, health data).
