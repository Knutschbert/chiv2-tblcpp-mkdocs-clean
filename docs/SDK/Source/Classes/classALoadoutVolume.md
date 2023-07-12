---
title: ALoadoutVolume
type: class
aliases: ALoadoutVolume
share: false

---

# ALoadoutVolume





Inherits from [ACaptureVolume](/docs/SDK/Source/Classes/classACaptureVolume.md), [ATBLActor](/docs/SDK/Source/Classes/classATBLActor.md), AActor, [IReplicatedSubobjectInterface](/docs/SDK/Source/Classes/classIReplicatedSubobjectInterface.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[[ALoadoutVolume]]**() |
| virtual void | **[[GetLifetimeReplicatedProps]]**(TArray< FLifetimeProperty > & OutLifetimeProps) const override |
| void | **[[OnIsActiveChanged]]**() |
| void | **[[SetActive]]**(bool Active) |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[LocalPCPossessedPawn]]**(APawn * NewPawn) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| bool | **[[bIsActive]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:58 +0200