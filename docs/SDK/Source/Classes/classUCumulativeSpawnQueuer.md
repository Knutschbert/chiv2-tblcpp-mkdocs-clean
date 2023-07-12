---
title: UCumulativeSpawnQueuer
type: class
aliases: UCumulativeSpawnQueuer
share: false

---

# UCumulativeSpawnQueuer





Inherits from [USpawnQueuer](/docs/SDK/Source/Classes/classUSpawnQueuer.md), [UTBLObject](/docs/SDK/Source/Classes/classUTBLObject.md), [UAssemblyObject](/docs/SDK/Source/Classes/classUAssemblyObject.md), UObject

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[[UCumulativeSpawnQueuer]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| float | **[[CumulativeTime]]**  |
| float | **[[StartingRespawnTime]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| TMap< TWeakObjectPtr< AController >, float > | **[[PlayerCumulativeTimes]]**  |
| TArray< [FCumulativePlayerSpawnPair](/docs/SDK/Source/Classes/structFCumulativePlayerSpawnPair.md) > | **[[SpawnQueue]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200