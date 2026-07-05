\# Haryana Revenue Toolkit (HRTK)



\# Revenue Relationship Model

Version: 1.0



Status: APPROVED



Release: A4.1



\---



\# Purpose



This document defines every relationship between the major entities of the

Haryana Revenue Toolkit.



The purpose is to ensure every module uses a single, consistent domain model.



No relationship shall be implemented unless it is first defined in this

document.



\---



\# Relationship Principles



The system models the Haryana Revenue Record.



Software shall follow Revenue practice.



Historical relationships shall never overwrite previous records.



Master entities remain independent.



Relationships connect master entities.



\---



\# Master Entities



Village



Jamabandi



Owner



Khewat



Parcel (Khasra)



Ownership



Partition



Mutation



\---



\# Entity Relationships



\## Village → Jamabandi



Relationship



One Village



↓



Many Jamabandis



Reason



Each revenue year creates one Jamabandi for every village.



Historical



YES



\---



\## Jamabandi → Khewat



Relationship



One Jamabandi



↓



Many Khewats



Reason



Each Jamabandi contains many ownership accounts.



Historical



YES



\---



\## Khewat → Ownership



Relationship



One Khewat



↓



Many Ownership Records



Reason



A Khewat usually has multiple owners.



Historical



YES



\---



\## Ownership → Owner



Relationship



Many Ownership Records



↓



One Owner



Reason



One owner may appear in many Khewats.



Historical



YES



\---



\## Khewat → Parcel



Relationship



One Khewat



↓



Many Parcels



Reason



Every Khewat consists of one or more Khasras.



Historical



YES



Important



The relationship exists only within a Jamabandi.



The Parcel itself remains independent.



\---



\## Parcel



Parcel represents physical land.



Parcel never stores



Owner



Khewat



Jamabandi



Partition



Mutation



Parcel only stores



Parcel Number



Area



Remarks



Future GIS information



\---



\## Ownership



Ownership stores



Owner



↓



Khewat



Ownership never stores



Parcels



\---



\## Partition



Partition consumes



Village



Jamabandi



Khewat



Ownership



Parcel



Partition creates



Allocation Records



Partition never modifies historical Jamabandis.



\---



\## Mutation



Mutation modifies



Ownership



Future Khewats



Future Parcel Relationships



Mutation never modifies historical records.



\---



\# Historical Rule



Historical relationships remain immutable.



Every Jamabandi represents a legal snapshot.



Future changes produce new records.



Historical records remain unchanged.



\---



\# Permanent Entities



Village



Owner



Parcel



\---



\# Historical Entities



Jamabandi



Ownership



Partition



Mutation



Relationship between Khewat and Parcel



\---



\# Database Rules



Master tables shall remain independent.



Relationship tables shall reference master tables.



Historical tables shall never overwrite previous records.



\---



\# Future Modules



The following modules shall use this relationship model.



Partition



Mutation



Reports



GIS



Analytics



Decision Support



\---



\# Engineering Rules



Business logic belongs in Services.



Repositories perform persistence only.



Presentation Layer performs no business logic.



Domain Objects remain independent.



Relationships shall never duplicate information.



\---



\# Validation Checklist



Before implementing a relationship verify



□ Does the relationship already exist?



□ Is it historical?



□ Is it permanent?



□ Will mutation affect it?



□ Will partition affect it?



□ Can historical records still be reconstructed?



\---



\# HRTK Rule



Entities represent facts.



Relationships represent legal associations.



History represents legal change.



These concepts shall never be mixed.



\---



Version



1.0



Status



Approved



Release



A4.1



End of Document

