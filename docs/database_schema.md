\# Haryana Revenue Toolkit (HRTK)



\# Database Schema

Version: 1.0



Status: APPROVED



Release: A4.2



\---



\# Purpose



This document defines the logical and physical database schema used by the

Haryana Revenue Toolkit (HRTK).



It provides a single reference for all database tables, their purpose,

relationships, and future expansion.



No database table shall be introduced unless it is documented here.



\---



\# Design Principles



1\. One table represents one business entity.



2\. Relationships shall be represented explicitly.



3\. Historical data shall never be overwritten.



4\. Database design shall follow the Revenue Domain Model.



5\. Stable tables shall not change without architectural review.



\---



\# Naming Convention



Database tables use singular names.



Examples



Village



Owner



Khewat



Parcel



Ownership



Jamabandi



\---



\# Current Database



\---



\## Village



Purpose



Stores Revenue Villages.



Primary Key



id



Important Fields



\- id

\- village\_name

\- hadbast\_number

\- district

\- tehsil



Referenced By



\- Khewat

\- Parcel

\- Jamabandi



Status



Frozen



\---



\## Owner



Purpose



Stores owner master information.



Primary Key



id



Important Fields



\- id

\- owner\_name

\- parent\_name

\- address

\- remarks



Referenced By



Ownership



Status



Frozen



\---



\## Khewat



Purpose



Stores ownership accounts.



Primary Key



id



Important Fields



\- id

\- village\_id

\- khewat\_number

\- remarks



Referenced By



Ownership



Future Land Relationship



Status



Frozen



\---



\## Parcel (Khasra)



Purpose



Stores physical land parcels.



Primary Key



id



Important Fields



\- id

\- village\_id

\- rectangle\_number

\- killa\_number

\- area

\- remarks



Referenced By



Future Relationship Layer



Partition



Reports



Status



Frozen



\---



\## Ownership



Purpose



Connects Owners with Khewats.



Primary Key



id



Foreign Keys



owner\_id



khewat\_id



Important Fields



\- ownership\_share

\- ownership\_type



Status



Frozen



\---



\## Jamabandi



Purpose



Represents one Record of Rights.



Primary Key



id



Important Fields



\- id

\- village\_id

\- revenue\_year

\- remarks



Status



Frozen



\---



\# Current Relationships



Village



↓



Khewat



Village



↓



Parcel



Village



↓



Jamabandi



Owner



↓



Ownership



↓



Khewat



\---



\# Missing Relationship



Current Gap



Khewat



↓



Parcel



The current schema does not define how parcels belonging to a Khewat are

recorded for a specific Jamabandi.



This relationship shall be introduced in a future release after design

approval.



\---



\# Future Tables



The following tables are planned.



\## Partition



Stores partition proceedings.



Status



Planned



\---



\## Allocation



Stores parcel allocations during partition.



Status



Planned



\---



\## Mutation



Stores mutation proceedings.



Status



Planned



\---



\## Reports



Virtual objects only.



No physical tables required.



\---



\# Foreign Key Policy



All relationships shall use foreign keys.



No duplicate information shall be stored.



Master entities remain independent.



\---



\# Historical Policy



Historical records shall never be deleted.



New Jamabandis shall create new records.



Partition shall never modify previous Jamabandis.



Mutation shall never overwrite history.



\---



\# Indexing Policy



Indexes shall exist for



Village ID



Owner ID



Khewat ID



Parcel Number



Revenue Year



Ownership



These indexes shall be reviewed before every major release.



\---



\# Schema Evolution



Database changes require



Architecture Review



↓



Approval



↓



Migration



↓



Regression Testing



↓



Freeze



\---



\# Stable Tables



Village



Owner



Khewat



Parcel



Ownership



Jamabandi



These tables are considered stable.



Future work shall extend the schema rather than redesign these tables.



\---



\# Future Expansion



Future modules may introduce



Partition



Allocation



Mutation



GIS



Analytics



without modifying the stable master tables.



\---



\# HRTK Database Principles



Master tables represent facts.



Relationship tables represent legal associations.



Historical tables represent change.



No table shall perform more than one responsibility.



\---



Version



1.0



Status



Approved



Release



A4.2



End of Document

