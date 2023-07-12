---
title: UGateComponent
type: class
aliases: UGateComponent
share: false

---

# UGateComponent





Inherits from UActorComponent, [IReplicatedSubobjectInterface](/docs/SDK/Source/Classes/classIReplicatedSubobjectInterface.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| bool | **[[GetIsGatedOpened]]**() |
| virtual void | **[[GetLifetimeReplicatedProps]]**(TArray< FLifetimeProperty > & OutLifetimeProps) const override |
| void | **[[OnRep_IsGateOpened]]**() |
| void | **[[SetIsGateOpened]]**(bool InGateOpened) |
| | **[[UGateComponent]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| [FReplicated_Bool](/docs/SDK/Source/Classes/structFReplicated__Bool.md) | **[[IsGateOpened]]**  |
| FGateClosed | **[[OnGateClosed]]**  |
| FGateOpened | **[[OnGateOpened]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200