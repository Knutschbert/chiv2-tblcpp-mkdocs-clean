---
title: ATBLActor
type: class
aliases: ATBLActor
share: false

---

# ATBLActor





Inherits from AActor, [IReplicatedSubobjectInterface](/docs/SDK/Source/Classes/classIReplicatedSubobjectInterface.md)

Inherited by [AAlwaysOnMusicManager](/docs/SDK/Source/Classes/classAAlwaysOnMusicManager.md), [AAmbientAnimalManager](/docs/SDK/Source/Classes/classAAmbientAnimalManager.md), [ABrawlAlwaysOnMusicManager](/docs/SDK/Source/Classes/classABrawlAlwaysOnMusicManager.md), [ABreakableActor](/docs/SDK/Source/Classes/classABreakableActor.md), [ACaptureVolume](/docs/SDK/Source/Classes/classACaptureVolume.md), [AHUDMarkerActor](/docs/SDK/Source/Classes/classAHUDMarkerActor.md), [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md), [ALadder](/docs/SDK/Source/Classes/classALadder.md), [ANPCSpawnManagerBase](/docs/SDK/Source/Classes/classANPCSpawnManagerBase.md), [APushableSiegeActor](/docs/SDK/Source/Classes/classAPushableSiegeActor.md), [APushableSplineActor](/docs/SDK/Source/Classes/classAPushableSplineActor.md), [AReplicatedCollisionActor](/docs/SDK/Source/Classes/classAReplicatedCollisionActor.md), [AReplicationTestActor](/docs/SDK/Source/Classes/classAReplicationTestActor.md), [ASpawnWave](/docs/SDK/Source/Classes/classASpawnWave.md), [AWaterActor](/docs/SDK/Source/Classes/classAWaterActor.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[[ATBLActor]]**() |
| bool | **[[CanBeBaseForCharacterTBL]]**(APawn * Pawn) const |
| TArray< AActor * > | **[[GetAIHintLocations]]**() const |
| void | **[[WakeUpNetDormancyForSeconds]]**(float Seconds) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| [FReplicationPredictionState](/docs/SDK/Source/Classes/structFReplicationPredictionState.md) | **[[PredictionState]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| TArray< TSoftObjectPtr< AActor > > | **[[AIHintLocationList]]**  |
| TArray< AActor * > | **[[CachedAIHintLocationList]]**  |
| float | **[[TimeToWakeUpNetDormancyWhenSubobjectChanges]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:58 +0200