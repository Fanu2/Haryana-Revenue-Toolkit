\# Haryana Revenue Toolkit (HRTK)



\# Revenue Terminology



Version: 1.0



Status: Active



\---



\# Purpose



This document defines the official revenue terminology used throughout the Haryana Revenue Toolkit (HRTK).



The objective is to ensure that every screen, report and document uses terminology familiar to Haryana Revenue officials.



Internal software names may differ from user-facing terminology.



\---



\# General Rule



Software shall follow Haryana Revenue terminology wherever possible.



Internal implementation names may use software engineering terminology for clarity.



Example



Internal



Parcel



User Interface



Khasra



\---



\# Village



Definition



The basic revenue unit.



Represents a revenue village.



Software



Village



\---



\# Jamabandi



Definition



The Record of Rights prepared periodically showing ownership and cultivation.



Software



Jamabandi Year



Examples



2023–24



2018–19



2013–14



\---



\# Owner



Definition



Person holding ownership rights in land.



Software



Owner



Future



Support for:



Individual



Joint Owner



Company



Government



Trust



\---



\# Khewat



Definition



Revenue account representing ownership.



A Khewat may contain one or more Khasras.



Software



Khewat No.



Examples



125



452



978



\---



\# Khatauni



Definition



Cultivation account.



Represents possession and cultivation.



Status



Future module.



\---



\# Khasra



Definition



A uniquely identified land parcel.



The physical parcel remains unique unless officially subdivided during partition or mutation.



Software



Khasra No.



\---



\# Murabba



Definition



A square block of land used in canal colonies and many revenue estates.



Example



25



\---



\# Killa



Definition



Field number within a Murabba.



Example



13



\---



\# Khasra Number



Standard Format



```

Murabba//Killa

```



Examples



```

25//13



25//14



36//2

```



Sub-divisions



```

25//13/1



25//13/2

```



The software shall display Khasra numbers in this format.



\---



\# Area



Official Unit



Kanal



Marla



Sarsai



Software display



Example



```

7K-8M-0S

```



Future



Automatic conversion utilities.



\---



\# Ownership Share



Definition



Fractional ownership within a Khewat.



Examples



```

1/2



3/5



7/16

```



Software



Ownership Share



Future



Percentage display optional.



\---



\# Partition



Official Term



Takseem



Definition



Division of jointly owned land according to ownership shares.



Software



Partition Workbench



Future reports may use the title:



Partition (Takseem)



\---



\# Mutation



Official Term



Intkal



Definition



Revenue process recording change in ownership.



Status



Future module.



\---



\# Tatima



Definition



Official field sketch showing partition boundaries.



Status



Future module.



\---



\# Revenue Officer



Possible users



Patwari



Kanungo



Naib Tehsildar



Tehsildar



District Revenue Officer



Advocate



Land Owner



The software interface should remain understandable for all these users.



\---



\# Internal vs User Terminology



| Internal Code | User Interface |

|---------------|----------------|

| Parcel | Khasra |

| Parcel Number | Khasra No. |

| Owner | Owner |

| Village | Village |

| Khewat | Khewat No. |

| Ownership | Ownership Share |

| Partition | Partition (Takseem) |

| Mutation | Intkal |

| Area | Kanal–Marla–Sarsai |



\---



\# Number Formatting



Khasra



```

25//13

```



Area



```

7K-8M-0S

```



Ownership



```

3/5

```



These formats should remain consistent throughout the application.



\---



\# Reports



Reports should use official terminology.



Examples



Jamabandi Register



Khewat Register



Khasra Register



Ownership Register



Partition Register



Mutation Register



Owner Ledger



Area Statement



Validation Report



\---



\# Future Expansion



Future terminology will include



Khatauni



Missal Haqiat



Roznamcha



Shajra Nasab



Tatima



Field Book



Aks Shajra



Court Orders



Revenue Appeals



\---



\# Guiding Principle



Every user-facing screen in HRTK should read as though it was designed specifically for the Haryana Revenue Department.



The software must use familiar terminology while maintaining clean internal software architecture.

