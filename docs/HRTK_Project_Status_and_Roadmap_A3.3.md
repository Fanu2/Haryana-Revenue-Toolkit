# Haryana Revenue Toolkit (HRTK)

## Project Status

**Release:** A3.3\
**Date:** 05 July 2026

## Vision

Develop a professional desktop application for Haryana Revenue
administration with a clean layered architecture and long-term
decision-support capabilities.

## Stable (Frozen) Modules

-   Dashboard
-   Village
-   Owner
-   Khewat
-   Khasra
-   Ownership
-   Partition

> Frozen modules are modified only to fix verified bugs.

## Current Architecture

``` text
Presentation
    │
Application Services
    │
Repositories
    │
SQLite Infrastructure
    │
Domain Model
    │
Value Objects
```

## Module Status

  Module      Status
  ----------- ---------------------------------------------
  Dashboard   Complete / Frozen
  Village     Complete / Frozen
  Owner       Complete / Frozen
  Khewat      Complete / Frozen
  Khasra      Complete / Frozen
  Ownership   Complete / Frozen
  Partition   Complete / Frozen (Persistence implemented)
  Jamabandi   Functional / Stable

### Partition Module Achievements

-   Partition Case management
-   Allocation Register
-   Allocation persistence
-   Automatic reload after restart
-   Validation
-   Undo
-   Refresh
-   Basic reporting
-   Toolbar integration

### Deferred Enhancement

Implement Khewat--Parcel relationship so Partition and Jamabandi can
load only the Khasras belonging to the selected Khewat. This is a future
enhancement, not a defect in the frozen Partition module.

## Development Principles

1.  Freeze completed master modules.
2.  Add new capabilities through relationship modules.
3.  Keep business rules inside service engines.
4.  Keep widgets focused on presentation.
5.  Repositories handle persistence only.
6.  Follow command-driven development.
7.  Commit only stable milestones.

## Next Major Milestone

### Release B1 -- Khewat--Parcel Relationship Manager

Purpose:

-   Relate Khewats and Khasras without modifying frozen master modules.
-   Provide the relationship layer required by Partition and Jamabandi.

## Planned Service Engines

-   Allocation Engine
-   Ownership Engine
-   Validation Engine
-   Share Calculator
-   Simulation Engine

## Long-Term Roadmap

### Phase A

Foundation (Completed)

### Phase B

Relationship Layer

-   Ownership
-   Khewat--Parcel

### Phase C

Business Service Engines

-   Allocation
-   Ownership
-   Validation
-   Share Calculator
-   Simulation

### Phase D

Transactional Modules

-   Mutation
-   Tatima
-   Revenue Ledger

### Phase E

Professional Reports

-   Jamabandi
-   Ownership Register
-   Partition Register
-   Village Register
-   Khewat Register
-   Khasra Register

### Phase F

GIS Integration

### Phase G

Decision Support

### Phase H

AI Assistant

## Target Architecture

``` text
                    Dashboard
                         │
 ┌───────────────────────┼───────────────────────┐
 │                       │                       │
Masters            Relationships          Transactions
 │                       │                       │
Village          Ownership            Partition
Owner            KhewatParcel         Jamabandi
Khewat                                Mutation
Khasra                                Tatima
 │
 └───────────────────────┬───────────────────────┐
                         │
                  Service Engines
                         │
 Allocation • Ownership • Validation
 Share Calculator • Simulation
                         │
               Reports • GIS • AI
```
