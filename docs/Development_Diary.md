\# Haryana Revenue Toolkit (HRTK)



\# Development Diary



\---



\## Release A3 – Demo Seeder Framework Complete



\*\*Date:\*\* 05 July 2026



\### Objective



Build a reusable developer seeder capable of creating a complete reference database for development, testing, demonstrations and future automated testing.



\---



\### Completed



\#### Seeder Framework



\- BaseSeeder framework

\- DemoDataSeeder launcher

\- Common progress reporting

\- Duplicate detection

\- Error reporting

\- UUID compatible seeding



\#### Seeders



\- Village Seeder

\- Owner Seeder

\- Jamabandi Seeder

\- Khewat Seeder

\- Parcel Seeder

\- Ownership Seeder



\#### Sample Data



Created demonstration datasets for:



\- Villages

\- Owners

\- Jamabandis

\- Khewats

\- Parcels

\- Ownerships



\---



\### Database



Resolved a legacy UUID migration issue discovered during testing.



One Jamabandi record contained an invalid textual village reference instead of a UUID foreign key.



The database was repaired and verified.



\---



\### Architecture Decisions



The Seeder Framework is intended only for baseline reference data.



The following workflow modules will \*\*not\*\* be included in the general-purpose seeder:



\- Partition Cases

\- Partition Allocations

\- Mutation workflow

\- Other operational workflow data



These will instead be implemented as scenario-based datasets when their respective workspaces are developed.



\---



\### Result



A new HRTK development database can now be generated with a single command.



The generated database contains a complete, internally consistent reference dataset suitable for development and testing.



\---



\### Lessons Learned



\- UUID migrations require strict validation of all foreign keys.

\- Seeder execution order is critical.

\- Business workflow data should remain separate from reference data.

\- Stable milestone commits simplify project recovery.



\---



\### Milestone Status



Release A3 completed.



Repository committed and pushed.



Seeder Framework frozen except for verified bug fixes.



\---



\### Next Milestone



Partition Workspace



Focus:



\- Partition Case management

\- Allocation engine

\- Validation workflow

\- Decision support

\- Reporting

