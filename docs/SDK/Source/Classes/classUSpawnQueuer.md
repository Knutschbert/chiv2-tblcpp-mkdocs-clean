---
title: USpawnQueuer
type: class
aliases: USpawnQueuer
share: false

---

# USpawnQueuer





Inherits from [UTBLObject](/docs/SDK/Source/Classes/classUTBLObject.md), [UAssemblyObject](/docs/SDK/Source/Classes/classUAssemblyObject.md), UObject

Inherited by [UCumulativeSpawnQueuer](/docs/SDK/Source/Classes/classUCumulativeSpawnQueuer.md), [UGroupSpawnQueuer](/docs/SDK/Source/Classes/classUGroupSpawnQueuer.md), [UNewSpawnSystemQueuer](/docs/SDK/Source/Classes/classUNewSpawnSystemQueuer.md), [URoundBasedSpawnQueuer](/docs/SDK/Source/Classes/classURoundBasedSpawnQueuer.md), [UWaveSpawnQueuer](/docs/SDK/Source/Classes/classUWaveSpawnQueuer.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[Activate]]**() |
| bool | **[[CanActivate]]**() |
| bool | **[[CanDeactivate]]**() |
| void | **[[Deactivate]]**() |
| bool | **[[IsActive]]**() |
| void | **[[ReceiveActivate]]**() |
| void | **[[ReceiveDeactivate]]**() |
| bool | **[[RemoveFromQueue]]**(AController * PC) |
| bool | **[[RequestSpawnFor]]**(AController * PC) |
| | **[[USpawnQueuer]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| EFaction | **[[Faction]]**  |
| FName | **[[Name]]**  |
| FSpawnQueueActivated | **[[OnActivated]]**  |
| FSpawnQueueDeactivated | **[[OnDeactivated]]**  |
| FSpawnQueuePlayerReadyToSpawn | **[[OnSpawnQueuePlayerReadyToSpawn]]**  |
| bool | **[[bApplysToAllTeams]]**  |
| bool | **[[bAutoActivate]]**  |
| bool | **[[bAutoDeactivate]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200