\# Haryana Revenue Toolkit (HRTK)



\# Module Audit

Version: 1.0



Status: APPROVED



Release: A4.2



\---



\# Purpose



This document defines the responsibility of every major module in the

Haryana Revenue Toolkit (HRTK).



Every module shall have one clearly defined responsibility.



Business logic shall never be duplicated between modules.



Every future module shall be checked against this document before

implementation.



\---



\# Audit Rules



Each module shall answer:



\- What does this module own?

\- What does this module NOT own?

\- Which services does it expose?

\- Which modules depend on it?

\- Is it Frozen?

\- Can it be extended?

\- What are the known gaps?



\---



\# Dashboard Module



\## Purpose



Application entry point.



Provides navigation and status information.



\## Owns



\- Navigation

\- Dashboard widgets

\- Application overview



\## Does NOT Own



\- Revenue logic

\- Business rules

\- Database operations



\## Status



Frozen



\## Extension



No



\---



\# Village Module



\## Purpose



Manage Revenue Villages.



\## Owns



\- Village Master

\- Hadbast Number

\- Administrative information



\## Depends On



None



\## Used By



\- Khewat

\- Jamabandi

\- Partition

\- Reports



\## Status



Frozen



\## Known Gaps



None



\---



\# Owner Module



\## Purpose



Manage land owners.



\## Owns



\- Owner identity

\- Personal information



\## Does NOT Own



\- Shares

\- Land

\- Khewats



\## Depends On



None



\## Used By



\- Ownership

\- Partition

\- Reports



\## Status



Frozen



\## Known Gaps



None



\---



\# Khewat Module



\## Purpose



Manage ownership accounts.



\## Owns



\- Khewat Number



\## Does NOT Own



\- Owners

\- Parcels

\- Shares



\## Depends On



Village



\## Used By



\- Ownership

\- Partition

\- Jamabandi



\## Status



Frozen



\## Known Gaps



Relationship with Parcels is not yet implemented.



\---



\# Parcel (Khasra) Module



\## Purpose



Manage physical land parcels.



\## Owns



\- Rectangle Number

\- Killa Number

\- Area

\- Remarks



\## Does NOT Own



\- Owner

\- Khewat

\- Jamabandi



\## Depends On



Village



\## Used By



\- Partition

\- Reports

\- Future GIS



\## Status



Frozen



\## Known Gaps



No historical relationship layer.



\---



\# Ownership Module



\## Purpose



Connect Owners with Khewats.



\## Owns



\- Share

\- Ownership Type

\- Owner–Khewat relationship



\## Does NOT Own



\- Parcels

\- Partition

\- Mutation



\## Depends On



Owner



Khewat



\## Used By



\- Partition

\- Jamabandi

\- Reports



\## Status



Frozen



\## Known Gaps



Does not relate ownership to individual parcels.



\---



\# Jamabandi Module



\## Purpose



Represent one Record of Rights.



\## Owns



\- Revenue Year

\- Jamabandi identity



\## Does NOT Own



\- Partition

\- Mutation



\## Depends On



Village



\## Used By



\- Partition

\- Reports

\- Future Mutation



\## Status



Frozen



\## Known Gaps



Future historical relationships will be added without modifying the core module.



\---



\# Partition Module



\## Purpose



Conduct partition proceedings.



\## Owns



\- Allocation workflow

\- Validation

\- Allocation register



\## Consumes



Village



Jamabandi



Khewat



Ownership



Parcel



\## Does NOT Own



Master data



\## Status



Active Development



\## Known Gaps



Needs a historical relationship layer to determine which parcels belong to a Khewat for a specific Jamabandi.



\---



\# Future Mutation Module



\## Purpose



Record legal changes affecting future Jamabandis.



\## Owns



\- Mutation workflow

\- Change history



\## Does NOT Modify



Historical Jamabandis



\## Status



Planned



\---



\# Future Reports Module



\## Purpose



Generate official reports.



\## Owns



Printing



Exports



Reports



\## Status



Planned



\---



\# Future GIS Module



\## Purpose



Visual representation of parcels.



\## Owns



Maps



Coordinates



Spatial analysis



\## Status



Future



\---



\# Frozen Module Register



| Module | Status |

|---------|--------|

| Dashboard | Frozen |

| Village | Frozen |

| Owner | Frozen |

| Khewat | Frozen |

| Parcel | Frozen |

| Ownership | Frozen |

| Jamabandi | Frozen |

| Partition | Development |

| Mutation | Planned |

| Reports | Planned |

| GIS | Future |



\---



\# Architectural Principles



1\. Every module owns one responsibility.



2\. Master modules never duplicate information.



3\. Relationships are explicit.



4\. Historical information is immutable.



5\. Services contain business logic.



6\. Repositories contain persistence logic only.



7\. Presentation layer contains no business logic.



8\. Stable modules remain frozen unless fixing a verified defect.



\---



\# Pre-Implementation Checklist



Before adding a new class:



□ Does a module already own this responsibility?



□ Is the information already available?



□ Will this duplicate existing logic?



□ Is the relationship permanent or historical?



□ Does it comply with the Revenue Domain Model?



□ Does it comply with the Revenue Relationship Model?



If any answer is uncertain, stop implementation and perform a design review.



\---



Version



1.0



Status



Approved



Release



A4.2



End of Document

