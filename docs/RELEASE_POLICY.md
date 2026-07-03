\# Haryana Revenue Toolkit (HRTK)



\# Release Policy



Version: 1.0



Status: Active



\---



\# Purpose



This document defines the official release policy for the Haryana Revenue Toolkit (HRTK).



Every release must satisfy the quality standards defined in this document before it is declared stable.



\---



\# Release Philosophy



A release is a stable checkpoint.



A release must always leave the project in a working, recoverable and documented state.



The application should always be capable of returning to the latest stable release.



\---



\# Release Lifecycle



Every release follows the same lifecycle.



```



Planning



↓



Design



↓



Implementation



↓



Integration



↓



Testing



↓



Documentation



↓



Commit



↓



Tag



↓



Push



↓



Freeze



```



No release may skip any stage.



\---



\# Stable Release



A release becomes Stable only when:



\- Application starts successfully.

\- No runtime traceback exists.

\- Navigation works.

\- Database operations succeed.

\- Documentation is updated.

\- Git commit completed.

\- Git tag created.

\- Repository pushed successfully.



\---



\# Frozen Modules



Once a module is declared Stable it becomes Frozen.



Frozen modules receive only:



\- Critical bug fixes

\- Data integrity fixes

\- Security fixes



Feature development is prohibited.



Current Frozen Modules



\- Dashboard

\- Village

\- Owner

\- Khewat

\- Khasra

\- Ownership



\---



\# Active Development



Only active modules may receive feature development.



Current Active Module



\- Partition Workbench



Future Active Modules



\- Mutation

\- Tatima

\- Reports

\- GIS

\- Court Management



\---



\# Version Numbering



The project follows milestone-based releases.



Examples



```



A1



A2



A3



A4



A5



```



Within a release, optional milestones may be used.



Examples



```



A4 Phase 1



A4 Phase 2



A4 Beta



A4 RC1



A4 Final



```



\---



\# Git Commit Policy



Every completed milestone shall be committed.



Commit messages should describe the feature.



Examples



```



Release A3 Ownership Module Complete



A4 Phase 1 Partition Workbench



Fix Ownership Validation



Improve Summary Panel



```



Avoid vague commit messages such as:



```



Update



Changes



Fixes



Work



```



\---



\# Git Tag Policy



Every stable milestone shall receive a tag.



Examples



```



release-a3



ownership-v1.0



partition-alpha



partition-beta



release-a4



```



Tags represent recovery points.



\---



\# Branch Strategy



Main Branch



```



main



```



Feature Branches



Examples



```



feature/partition



feature/mutation



feature/reports



```



Bug Fix Branches



Examples



```



bugfix/ownership-validation



bugfix/summary-panel



```



\---



\# Documentation Policy



Every release must update:



\- CHANGELOG.md

\- ROADMAP.md



When architecture changes, also update:



\- PROJECT\_CHARTER.md

\- ARCHITECTURE.md



\---



\# Testing Checklist



Before every release verify:



Application starts.



No traceback.



Navigation works.



All stable modules open.



CRUD operations work.



Partition module opens.



Logging works.



Database persists correctly.



\---



\# Freeze Procedure



Before freezing a release:



1\. Complete implementation.

2\. Test all features.

3\. Update documentation.

4\. Commit.

5\. Tag.

6\. Push.

7\. Declare release frozen.



\---



\# Rollback Policy



If a release becomes unstable:



1\. Stop development.

2\. Checkout the latest stable tag.

3\. Investigate.

4\. Fix in a feature branch.

5\. Re-test.

6\. Create a new tag.



Never continue development on an unstable release.



\---



\# Recovery Principle



The repository should always contain a stable recovery point.



Recovery must never depend on local files.



Git is the official recovery mechanism.



\---



\# Long-Term Goal



Every release should improve:



\- Stability

\- Reliability

\- Maintainability

\- Accuracy

\- User Experience



without compromising previous stable functionality.



\---



\# Guiding Principle



A release is complete only when the software, documentation and repository are all in a stable state.

