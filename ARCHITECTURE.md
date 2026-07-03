# Haryana Revenue Toolkit (HRTK)

# Software Architecture

Version: 1.0

Status: Active

---

# Purpose

This document describes the software architecture of the Haryana Revenue Toolkit (HRTK).

The objective is to maintain a clean, scalable and maintainable architecture while accurately modelling Haryana Revenue Administration.

---

# Architectural Style

HRTK follows a layered architecture inspired by Clean Architecture and Domain Driven Design.

```
Presentation
      │
      ▼
Application Services
      │
      ▼
Repositories
      │
      ▼
Domain
      │
      ▼
Infrastructure
```

Each layer has a single responsibility.

---

# Layer 1 — Presentation

Responsible for:

- User Interface
- Dialogs
- Tables
- Toolbars
- Navigation
- Workspace
- Status Display

Presentation never contains business rules.

Directory

```
presentation/
```

Typical classes

```
VillageWidget

OwnerWidget

KhewatWidget

KhasraWidget

OwnershipWidget

PartitionWidget
```

---

# Layer 2 — Application

Responsible for:

- Business workflows
- Validation
- Orchestration
- Coordination

Directory

```
application/
```

Typical classes

```
VillageService

OwnerService

KhewatService

ParcelService

OwnershipService

PartitionService
```

Widgets communicate only with Services.

---

# Layer 3 — Repository

Responsible for:

- Reading data
- Writing data
- Persistence abstraction

Repositories never contain GUI code.

Repositories never know about Qt.

---

# Layer 4 — Domain

Responsible for business concepts.

Contains

Entities

Value Objects

Business Rules

Enumerations

Domain Services

Examples

```
Village

Owner

Khewat

Parcel

Ownership

Area

ParcelNumber

Fraction
```

The Domain layer contains no GUI code.

---

# Layer 5 — Infrastructure

Responsible for:

SQLite

Logging

Export

Import

Configuration

Repository implementations

Infrastructure supports every other layer.

---

# Dependency Rules

Allowed

```
Presentation

↓

Application

↓

Repository

↓

Domain

↓

Infrastructure
```

Forbidden

```
Presentation

↓

SQLite
```

Forbidden

```
Widget

↓

SQL
```

Forbidden

```
Dialog

↓

Repository
```

---

# Module Structure

Every major module follows the same structure.

Example

```
ownership/

ownership_widget.py

ownership_dialog.py

ownership_toolbar.py

ownership_table.py

ownership_model.py
```

Future modules follow exactly the same pattern.

---

# Stable Modules

The following modules are frozen.

Dashboard

Village

Owner

Khewat

Khasra

Ownership

These modules shall not receive feature work.

---

# Active Modules

Partition

Mutation

Tatima

Reports

GIS

Future work happens only inside these modules.

---

# Business Logic Rule

Business rules belong only inside Services.

Example

Correct

```
OwnershipWidget

↓

OwnershipService.register()

↓

Repository
```

Incorrect

```
OwnershipWidget

↓

SQL INSERT
```

---

# User Interface Standard

Every workspace shall contain:

Toolbar

↓

Selection Area

↓

Main Tables

↓

Summary

↓

Validation

↓

Status

Partition Workbench is the reference implementation.

---

# Naming Convention

Internal Code

Parcel

Presentation

Khasra

Internal Code

ParcelNumber

Presentation

Khasra Number

Internal Code

Ownership

Presentation

Ownership Share

Internal Code

PartitionWidget

Presentation

Partition Workbench

---

# Logging

Every important action shall be logged.

Examples

Application started

Village created

Owner updated

Partition saved

Report exported

Errors must include sufficient diagnostic information.

---

# Error Handling

Errors should never crash the application.

Errors should produce:

Status Message

Log Entry

User Friendly Message

Unexpected exceptions should always be logged.

---

# Future Expansion

The architecture must support:

Mutation

Tatima

GIS

Digital Maps

Revenue Reports

Court Cases

Registry

Audit Trail

without modification of stable modules.

---

# Architecture Goal

The architecture shall remain:

Simple

Modular

Readable

Recoverable

Scalable

Professional

for the lifetime of the project.
