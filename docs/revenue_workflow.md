\# Haryana Revenue Toolkit (HRTK)



\# Revenue Workflow

Version: 1.0



Status: APPROVED



Release: A5.0



\---



\# Purpose



This document defines the operational workflow followed in a Haryana Revenue

Office.



The Haryana Revenue Toolkit (HRTK) shall model actual revenue procedures rather

than merely storing data.



Every workflow module shall conform to this document.



\---



\# Vision



HRTK is not intended to be only a land records application.



Its objective is to become a complete Digital Revenue Office.



The software shall model:



• Revenue Records



• Revenue Proceedings



• Revenue Administration



• Decision Support



• Historical Records



\---



\# Guiding Principles



1\. Revenue practice drives software design.



2\. Historical records are immutable.



3\. Every proceeding is traceable.



4\. Master records remain independent.



5\. Workflow modules consume master data.



6\. No workflow modifies historical records.



\---



\# Master Data Workflow



Revenue administration begins with master data.



Village

&#x20;   ↓

Owner

&#x20;   ↓

Khewat

&#x20;   ↓

Parcel (Khasra)

&#x20;   ↓

Ownership

&#x20;   ↓

Jamabandi



These modules create the Record of Rights.



\---



\# Revenue Proceedings



After the Record of Rights exists, legal proceedings may occur.



Jamabandi

&#x20;     │

&#x20;     ├── Partition

&#x20;     │

&#x20;     ├── Mutation (Intkal)

&#x20;     │

&#x20;     ├── Correction

&#x20;     │

&#x20;     ├── Exchange

&#x20;     │

&#x20;     ├── Inheritance

&#x20;     │

&#x20;     └── Court Orders



Proceedings never destroy history.



They create new legal records.



\---



\# Revenue Office Workflow



Step 1



Create Revenue Village



↓



Step 2



Register Owners



↓



Step 3



Create Khewats



↓



Step 4



Register Parcels (Khasras)



↓



Step 5



Record Ownership Shares



↓



Step 6



Prepare Jamabandi



↓



Step 7



Publish Record of Rights



↓



Step 8



Revenue Proceedings



↓



Partition



↓



Mutation



↓



Correction



↓



Inheritance



↓



Court Orders



↓



Step 9



Prepare New Jamabandi



↓



Step 10



Reports and Certificates



\---



\# Partition Workflow



Inputs



Village



Jamabandi



Khewat



Ownership



Parcel



Process



Determine legal entitlement.



Select parcels.



Allocate land.



Validate balances.



Prepare proceedings.



Generate final order.



Outputs



Allocation Register



Partition Report



Future Mutation



Future Jamabandi



\---



\# Mutation Workflow



Inputs



Existing Jamabandi



Mutation Order



Supporting Documents



Process



Verify legality.



Record mutation.



Update ownership.



Prepare next Jamabandi.



Outputs



Mutation Register



Updated ownership



Future Jamabandi



\---



\# Correction Workflow



Purpose



Correct clerical mistakes.



Correction never changes legal history.



Every correction is traceable.



\---



\# Court Workflow



Court orders may affect



Ownership



Mutation



Partition



Future Jamabandi



Court proceedings never alter historical records.



\---



\# Reports



The system shall generate



Jamabandi



Ownership Register



Parcel Register



Partition Register



Mutation Register



Owner Statements



Village Summary



Revenue Statistics



Audit Reports



GIS Reports



\---



\# User Roles



Administrator



Revenue Officer



Naib Tehsildar



Tehsildar



Kanungo



Patwari



Read Only User



Auditor



Each role shall have clearly defined permissions.



\---



\# Decision Support



Future versions shall assist officers by



Detecting inconsistencies.



Checking ownership balances.



Validating partition.



Finding missing records.



Producing alerts.



Generating summaries.



Providing recommendations.



\---



\# Historical Policy



Every proceeding produces history.



Nothing is deleted.



Nothing is overwritten.



Every revenue year remains available for audit.



\---



\# Module Responsibilities



Master Modules



Village



Owner



Khewat



Parcel



Ownership



Jamabandi



Workflow Modules



Partition



Mutation



Correction



Inheritance



Court Proceedings



Reporting Modules



Reports



Certificates



Registers



Analytics



GIS



\---



\# Development Rule



Every future feature shall answer three questions.



1\.



How is the work performed in the Revenue Office?



2\.



Which module owns the responsibility?



3\.



Which existing master data is reused?



If these questions cannot be answered, implementation shall stop until

the workflow is clarified.



\---



\# Long-Term Roadmap



Phase 1



Master Data



✓ Completed



Phase 2



Architecture



✓ Completed



Phase 3



Partition Proceedings



In Progress



Phase 4



Mutation Proceedings



Planned



Phase 5



Reporting System



Planned



Phase 6



GIS Integration



Future



Phase 7



Decision Support



Future



Phase 8



AI Assisted Revenue Administration



Vision



\---



\# Engineering Principles



Workflow modules never own master data.



Master modules never contain workflow logic.



Business rules belong in Services.



Repositories perform persistence only.



Presentation layer performs no business logic.



Historical records remain immutable.



\---



\# HRTK Mission



To create a professional Digital Revenue Office that accurately models the

administrative and legal procedures of Haryana Revenue Administration while

maintaining complete historical integrity and providing a modern,

maintainable software architecture.



\---



Version



1.0



Status



APPROVED



Release



A5.0



End of Document

