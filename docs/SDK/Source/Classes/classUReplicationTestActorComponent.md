---
title: UReplicationTestActorComponent
type: class
aliases: UReplicationTestActorComponent
share: false

---

# UReplicationTestActorComponent





Inherits from UActorComponent, [IReplicatedSubobjectInterface](/docs/SDK/Source/Classes/classIReplicatedSubobjectInterface.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| virtual void | **[[GetLifetimeReplicatedProps]]**(TArray< FLifetimeProperty > & OutLifetimeProps) const override |
| void | **[[OnRep_TestVisible]]**() |
| void | **[[OnRep_TestVisibleEngine]]**() |
| void | **[[SetVisible]]**(bool Vis) |
| | **[[UReplicationTestActorComponent]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| FOnReplicationtestVisible | **[[OnReplicationEngineTestVisible]]**  |
| FOnReplicationtestVisible | **[[OnReplicationtestVisible]]**  |
| bool | **[[StartTestVisible]]**  |
| [FReplicated_Bool](/docs/SDK/Source/Classes/structFReplicated__Bool.md) | **[[TestVisible]]**  |
| bool | **[[TestVisibleEngine]]**  |
| bool | **[[bBroadcastSetVariableOnlyOnAuthority]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200