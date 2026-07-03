\# Haryana Revenue Toolkit (HRTK)



\# Project Charter



\*\*Version:\*\* 1.0



\*\*Status:\*\* Active



\*\*Project:\*\* Haryana Revenue Toolkit (HRTK)



\---



\# Vision



The Haryana Revenue Toolkit (HRTK) is a professional desktop application designed to model the complete Haryana Revenue Administration workflow.



The objective is to provide a modern, maintainable and accurate software platform for managing revenue records while preserving official Haryana Revenue terminology, procedures and business rules.



The software is intended to evolve into a complete revenue administration suite supporting the entire lifecycle of land records.



\---



\# Mission



Develop a reliable desktop application that faithfully represents Haryana Revenue procedures while maintaining modern software engineering practices.



The software should assist:



\- Patwari

\- Kanungo

\- Naib Tehsildar

\- Tehsildar

\- Revenue Officers

\- Advocates

\- Land Owners



through day-to-day revenue administration.



\---



\# Core Philosophy



The software shall model the Haryana Revenue System.



The Revenue System shall never be modified to fit software limitations.



Business rules always take precedence over implementation convenience.



\---



\# Guiding Principles



\## 1. Stable Modules Are Frozen



Once a module is declared stable it becomes frozen.



Frozen modules are modified only for:



\- Critical bugs

\- Data corruption

\- Security fixes



Feature development shall occur only in new modules.



Current frozen modules are:



\- Dashboard

\- Village

\- Owner

\- Khewat

\- Khasra

\- Ownership



\---



\## 2. Business Before Technology



Revenue procedures determine software behaviour.



Whenever uncertainty exists:



1\. Verify Haryana Revenue Rules.

2\. Verify Domain Model.

3\. Implement software.



Never reverse this order.



\---



\## 3. Clean Architecture



Every component shall belong to a single architectural layer.



Presentation



↓



Application Services



↓



Repositories



↓



Domain



↓



Infrastructure



No shortcuts are permitted.



\---



\## 4. Single Responsibility



Every class performs one responsibility only.



Widgets display information.



Services contain business rules.



Repositories manage persistence.



Domain contains business concepts.



\---



\## 5. Professional Quality



Every production module should provide:



\- Toolbar

\- Validation

\- Status Messages

\- Summary

\- Reports

\- Logging

\- Undo (where applicable)



\---



\## 6. Incremental Development



Every feature shall follow the sequence:



Design



↓



Skeleton



↓



Integration



↓



Testing



↓



Commit



↓



Tag



↓



Push



Large uncontrolled modifications are prohibited.



\---



\## 7. Recovery First



Every development milestone must end with:



\- Commit

\- Tag

\- Push



The project must always be recoverable.



\---



\## 8. Revenue Terminology



The user interface shall always use official Haryana Revenue terminology.



Examples:



Parcel → Khasra



Parcel Number → Khasra No.



Mutation → Intkal



Partition → Takseem



Ownership Share → Hissa



Area → Kanal–Marla–Sarsai



\---



\## 9. Stable Foundation



Existing stable modules shall remain reusable by future modules.



Future modules consume stable services instead of modifying them.



\---



\## 10. Long-Term Maintainability



Code shall prioritise:



\- Readability

\- Simplicity

\- Maintainability

\- Testability

\- Recoverability



Over clever or complex implementations.



\---



\# Development Workflow



Every new feature shall follow:



Research



↓



Design



↓



Implementation



↓



Testing



↓



Documentation



↓



Commit



↓



Release Tag



\---



\# Release Philosophy



Release A1



Framework



Release A2



Village



Owner



Release A3



Khewat



Khasra



Ownership



Release A4



Partition



Release A5



Mutation



Release A6



Tatima



Release A7



Reports



Release A8



GIS



Release A9



Complete Revenue Administration Suite



\---



\# Project Motto



> Model the Haryana Revenue System faithfully while maintaining clean software architecture.



\---



\# Conclusion



HRTK is intended to become a complete professional Revenue Administration Toolkit for Haryana.



The emphasis of the project shall always remain:



Accuracy



Reliability



Maintainability



Professional quality



Faithful implementation of Haryana Revenue procedures.

