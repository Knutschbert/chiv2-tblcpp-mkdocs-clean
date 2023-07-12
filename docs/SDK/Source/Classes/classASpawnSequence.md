---
title: ASpawnSequence
type: class
aliases: ASpawnSequence
share: false

---

# ASpawnSequence





Inherits from AActor

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[[ASpawnSequence]]**() |
| bool | **[[Activate]]**() |
| void | **[[ActivateDeactivate]]**(ESpawnSequenceActivateDeactivateAction Action) |
| void | **[[AddSpawner]]**([ASpawner](/docs/SDK/Source/Classes/classASpawner.md) * Spawner) |
| void | **[[Deactivate]]**() |
| void | **[[EmptySpawnerList]]**() |
| void | **[[ForceSpawnController]]**(AController * Controller) |
| void | **[[Initialize]]**([FSpawnSequenceProperties](/docs/SDK/Source/Classes/structFSpawnSequenceProperties.md) Properties) |
| void | **[[PushSpawner]]**([ASpawner](/docs/SDK/Source/Classes/classASpawner.md) * Spawner) |
| void | **[[RemoveSpawner]]**([ASpawner](/docs/SDK/Source/Classes/classASpawner.md) * Spawner) |
| void | **[[SetSecondsBetweenWaves]]**(float InSecondsBetweenWaves) |
| void | **[[SetSpawnerList]]**(const TArray< [ASpawner](/docs/SDK/Source/Classes/classASpawner.md) * > & SpawnerList) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| int32 | **[[CurrentIndex]]**  |
| EFaction | **[[Faction]]**  |
| UCurveFloat * | **[[MaxPlayersPlayerCountBonus]]**  |
| FSequenceFinished | **[[OnSequenceFinished]]**  |
| TArray< [ASpawner](/docs/SDK/Source/Classes/classASpawner.md) * > | **[[PushedSpawners]]**  |
| float | **[[SecondsBetweenWaves]]**  |
| UCurveFloat * | **[[SecondsBetweenWavesPlayerCountBonus]]**  |
| int32 | **[[SimultaneousWaves]]**  |
| [FSpawnWaveParamOverrides](/docs/SDK/Source/Classes/structFSpawnWaveParamOverrides.md) | **[[SpawnWaveParams]]**  |
| TArray< [ASpawner](/docs/SDK/Source/Classes/classASpawner.md) * > | **[[SpawnerQueue]]**  |
| TArray< [ASpawner](/docs/SDK/Source/Classes/classASpawner.md) * > | **[[Spawners]]**  |
| bool | **[[bAlwaysKeepOneWaveActive]]**  |
| bool | **[[bFastFirstSpawn]]**  |
| bool | **[[bIsActive]]**  |
| bool | **[[bLoop]]**  |
| bool | **[[bOverrideWaveTimingToHalfOfSecondsBetweenWaves]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:58 +0200