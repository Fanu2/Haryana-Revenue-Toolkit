\# Haryana Revenue Toolkit (HRTK)



\*\*Architecture Guide\*\*



| Item | Value |

|------|-------|

| Project | Haryana Revenue Toolkit (HRTK) |

| Version | 0.5.0 |

| Status | Foundation Freeze |

| Document Type | Engineering Architecture |

| Audience | Developers, Contributors, Maintainers |

| License | Same as Project |



\---



\# Mission Statement



The Haryana Revenue Toolkit (HRTK) is a professional desktop application for the management of land revenue records, ownership, partition proceedings, survey information, and related administrative workflows.



The project is designed with long-term maintainability, extensibility, correctness, and usability as its primary architectural goals.



HRTK is intended to evolve into a complete digital land revenue platform while maintaining a clean, modular, and well-documented codebase.



\---



\# Vision



The long-term vision of HRTK is to become a modern desktop platform for managing the complete lifecycle of land administration.



The platform will eventually include:



\- Village Management

\- Owner Management

\- Khewat Management

\- Khasra Management

\- Mutation Management

\- Partition Management

\- Jamabandi Management

\- Survey Tools

\- GIS Integration

\- Reporting

\- Printing

\- Data Import/Export

\- Backup and Restore

\- Analytics



Every new subsystem should integrate naturally into the existing architecture without requiring major redesign.



\---



\# Architectural Philosophy



The architecture of HRTK is based on several core principles.



\## Separation of Concerns



Each layer of the application has one clearly defined responsibility.



Business rules must remain independent from presentation.



Presentation must remain independent from persistence.



Infrastructure must remain independent from business logic.



\---



\## Single Responsibility Principle



Each class should have one primary responsibility.



Examples:



\- Widget → User interface

\- Service → Business logic

\- Repository → Data access

\- Exporter → File generation

\- Model → Qt data model



\---



\## Reuse Before Duplication



Reusable functionality belongs in shared framework classes.



Examples include:



\- BaseDialog

\- BaseToolbar

\- BaseTable

\- MessageService

\- SaveFileService

\- SearchProxyModel



Module-specific code should remain inside the corresponding module.



\---



\## Architecture Before Features



Every new subsystem follows the same development lifecycle.



Architecture



↓



Folder Structure



↓



Interfaces



↓



Implementation



↓



Testing



↓



Documentation



↓



Release



\---



\# Layered Architecture



HRTK follows a layered architecture.



```

Presentation

&#x20;       │

&#x20;       ▼

Application Services

&#x20;       │

&#x20;       ▼

Repositories

&#x20;       │

&#x20;       ▼

Domain

&#x20;       │

&#x20;       ▼

Infrastructure

```



Dependencies always flow downward.



Lower layers never depend on higher layers.



\---



\# Package Structure



```

src/

└── hrtk/

&#x20;   ├── application/

&#x20;   ├── domain/

&#x20;   ├── repositories/

&#x20;   ├── services/

&#x20;   ├── presentation/

&#x20;   ├── export/

&#x20;   ├── infrastructure/

&#x20;   └── utils/

```



Each package has a clearly defined responsibility.



\---



\# Layer Responsibilities



\## Domain Layer



Contains business entities.



Examples:



\- Village

\- Owner

\- Khewat

\- Khasra

\- Mutation



The Domain Layer contains no Qt code.



The Domain Layer contains no SQL code.



\---



\## Repository Layer



Responsible for persistence.



Responsibilities include:



\- Create

\- Read

\- Update

\- Delete

\- Queries



Repositories never display dialogs.



Repositories never contain presentation logic.



\---



\## Service Layer



Coordinates business workflows.



Examples:



\- VillageService

\- OwnerService

\- KhewatService

\- ExportService



Services coordinate repositories.



Services coordinate validation.



Services coordinate business rules.



\---



\## Presentation Layer



Responsible for user interaction.



Contains:



\- Widgets

\- Dialogs

\- Models

\- Tables

\- Toolbars



Presentation never performs business calculations.



Presentation never accesses SQL directly.



\---



\## Infrastructure Layer



Provides external integrations.



Examples:



\- Excel

\- PDF

\- CSV

\- File System

\- Logging



Infrastructure is replaceable without affecting business logic.



\---

