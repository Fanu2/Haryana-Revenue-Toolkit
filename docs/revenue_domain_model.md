\# Haryana Revenue Toolkit (HRTK)



\# Revenue Domain Model

Version: 1.0



Status: APPROVED



Release: A4.1



Author:

Haryana Revenue Toolkit Development Team



\---



\# Purpose



This document defines the official Revenue Domain Model used throughout the

Haryana Revenue Toolkit (HRTK).



All future development shall conform to this document.



Whenever software implementation differs from actual Haryana Revenue

practice, the software shall be corrected.



The Revenue Domain Model is considered the authoritative reference for

application architecture.



\---



\# Guiding Principles



1\. Revenue practice drives software design.



2\. Existing stable modules shall not be modified unless a verified defect is

&#x20;  discovered.



3\. Relationships between entities shall be represented explicitly.



4\. Historical records shall never be destroyed.



5\. Every Jamabandi represents a snapshot of land ownership for one revenue

&#x20;  year.



\---



\# Current Stable Modules



The following modules are frozen.



• Dashboard



• Village



• Owner



• Khewat



• Parcel (Khasra)



• Ownership



• Jamabandi



These modules may only be modified after:



\- bug verification

\- impact analysis

\- regression testing



\---



\# Core Revenue Entities



\## Village



Represents a Revenue Village.



Contains:



\- Village Name

\- Hadbast Number

\- District

\- Tehsil

\- Other administrative information



Village is the highest operational unit.



\---



\## Parcel (Khasra)



Represents one physical parcel of land.



A Parcel represents land only.



A Parcel shall never contain ownership information.



Contains:



\- Rectangle Number

\- Killa Number

\- Area

\- Remarks



Future enhancements may include GIS coordinates.



\---



\## Owner



Represents one person or legal entity.



Contains only owner information.



Ownership shall not be stored inside Owner.



\---



\## Khewat



Represents one ownership account.



Contains:



\- Khewat Number



A Khewat groups Owners together.



A Khewat does not represent land.



Land is linked separately.



\---



\## Ownership



Ownership links:



Owner



↓



Khewat



Ownership stores:



\- Share

\- Ownership Type

\- Related information



Ownership does not contain parcels.



\---



\## Jamabandi



Represents one Record of Rights.



Each Jamabandi belongs to one Revenue Year.



Examples



2008-09



2012-13



2017-18



2023-24



Jamabandi is historical.



Older Jamabandis remain preserved.



\---



\# Revenue Hierarchy



Village



↓



Jamabandi



↓



Khewat



↓



Ownership



↓



Parcel (Khasra)



\---



\# Important Design Principle



Parcel is an independent entity.



Owner is an independent entity.



Khewat is an independent entity.



Relationships shall never be duplicated.



\---



\# Partition



Partition is a workflow.



Partition does not own land.



Partition consumes information from:



Village



Jamabandi



Khewat



Ownership



Parcel



Partition creates allocation records.



\---



\# Mutation (Future)



Mutation modifies:



Ownership



Relationship between Khewat and Parcel



Future Jamabandis



Mutation never alters historical Jamabandis.



\---



\# Historical Records



Historical Jamabandis remain immutable.



Every new Jamabandi represents a new legal snapshot.



\---



\# Development Rules



Before creating any new module developers shall answer:



1\.

Does the entity already exist?



2\.

Is this information already stored elsewhere?



3\.

Would this duplicate another module?



4\.

Is the relationship historical?



5\.

Can this design survive future mutations and partitions?



\---



\# Module Development Order



Completed



✓ Dashboard



✓ Village



✓ Owner



✓ Khewat



✓ Parcel



✓ Ownership



✓ Jamabandi



Current



► Partition



Future



Mutation



Reports



GIS



Analytics



\---



\# Engineering Principles



Business logic belongs in Services.



Domain Objects remain independent.



Repositories provide persistence only.



Presentation Layer contains no business rules.



Historical information shall never be overwritten.



\---



\# Coding Principles



Every feature shall be implemented using the Command Protocol.



Every command shall define:



Objective



Files Allowed



Protected Modules



Validation Tests



Freeze Decision



Git Commit



\---



\# Freeze Policy



Stable modules are protected.



Changes require:



Verified Bug



↓



Approval



↓



Regression Test



↓



Freeze



\---



\# Future Domain Review



The Revenue Domain Model shall be reviewed before every major release.



Current Version



1.0



Status



Approved



Release



A4.1



End of Document

