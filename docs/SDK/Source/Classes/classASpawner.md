---
title: ASpawner
type: class
aliases: ASpawner
share: false

---

# ASpawner





Inherits from AActor

Inherited by [AGroupSpawner](/docs/SDK/Source/Classes/classAGroupSpawner.md), [ASeatSpawner](/docs/SDK/Source/Classes/classASeatSpawner.md), [ASimpleSpawner](/docs/SDK/Source/Classes/classASimpleSpawner.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[[ASpawner]]**() |
| void | **[[Cinematics_BecameNextSpawner]]**([ATBLPlayerController](/docs/SDK/Source/Classes/classATBLPlayerController.md) * Controller) |
| void | **[[Cinematics_ControllerPossessedPawn]]**([ATBLPlayerController](/docs/SDK/Source/Classes/classATBLPlayerController.md) * Controller, [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Pawn) |
| void | **[[Cinematics_StartAllowingControl]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Character) |
| void | **[[ConditionalStopSpawning]]**() |
| void | **[[GenerateSpawnComponents]]**() |
| int32 | **[[GetMaxPlayerCount]]**() const |
| int32 | **[[GetMinPlayerCount]]**() const |
| int32 | **[[GetRemainingReservations]]**() const |
| USceneComponent * | **[[GetSpawnLocationAndComponent]]**(int32 Index, FTransform & OutTransform, float & SpawnRadius, float & SpawnHalfHeight) const |
| [ASpawnWave](/docs/SDK/Source/Classes/classASpawnWave.md) * | **[[GetSpawnWave]]**() |
| TArray< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * > | **[[GetSpawnedCharacters]]**() |
| float | **[[GetSpawnerScoreForAllPlayers]]**() const |
| float | **[[GetSpawnerScoreForFaction]]**(EFaction Faction) const |
| int32 | **[[GetTotalReservations]]**() const |
| void | **[[HandleOnCustomizationJobsEmptied]]**() |
| bool | **[[IsChildSpawner]]**() const |
| bool | **[[IsPendingLock]]**() const |
| int32 | **[[IsThereAPlayerTooClose]]**(EFaction Faction, int32 LocationIndex, bool bIsSpawningIn) const |
| bool | **[[IsWaveLocked]]**() const |
| void | **[[LockingWaveDestroyed]]**(AActor * DestroyedSpawnWave) |
| void | **[[OnPossessedCharacter]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Character, AController * Controller) |
| void | **[[OnSpawnedCharacter]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * NewCharacter, USceneComponent * SpawnComp) |
| void | **[[OnSpawningCharacter]]**(const FTransform & SpawningTransform) |
| void | **[[OverrideNextSpawnWaveSpecialSpawnSpec]]**(TSubclassOf< [USpecialSpawnSpec](/docs/SDK/Source/Classes/classUSpecialSpawnSpec.md) > NewSpecialSpawnSpec) |
| void | **[[RequestSpawnQueueSlot]]**() |
| void | **[[SetupComponentsArray]]**() |
| [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * | **[[SpawnCharacter]]**(const FTransform & SpawnTransform, TSubclassOf< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) > Class, AController * Controller) |
| [AForcedRespawnSpawnWave](/docs/SDK/Source/Classes/classAForcedRespawnSpawnWave.md) * | **[[StartForcedSpawning]]**(AController * SpawnController, const [FSpawnWaveParamOverrides](/docs/SDK/Source/Classes/structFSpawnWaveParamOverrides.md) & InSpawnWaveParams) |
| [AForwardSpawnWave](/docs/SDK/Source/Classes/classAForwardSpawnWave.md) * | **[[StartForwardSpawning]]**(const TArray< APawn * > & PawnsAllowedToSpawn, const [FSpawnWaveParamOverrides](/docs/SDK/Source/Classes/structFSpawnWaveParamOverrides.md) & InSpawnWaveParams) |
| [ASpawnWave](/docs/SDK/Source/Classes/classASpawnWave.md) * | **[[StartSpawning]]**(EFaction Faction, const [FSpawnWaveParamOverrides](/docs/SDK/Source/Classes/structFSpawnWaveParamOverrides.md) & InSpawnWaveParams) |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[HandleAddedReservation]]**(const [FSpawnerSpawnReservation](/docs/SDK/Source/Classes/structFSpawnerSpawnReservation.md) & Reservation) |
| bool | **[[IsValidSpawnLocation]]**(const FTransform & OutTransform, TSubclassOf< APawn > PawnClass) const |
| void | **[[RequestSpawnerScoreUpdate]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| float | **[[CameraInterpTime]]**  |
| float | **[[ColumnSpacing]]**  |
| int32 | **[[Columns]]**  |
| float | **[[LastSpawnTime]]**  |
| float | **[[MinimumPlayerDistance]]**  |
| float | **[[MinimumVulnerabilityTime]]**  |
| int32 | **[[NextReservationToSpawn]]**  |
| FPossessedCharacter | **[[OnSpawnerPossessedCharacter]]**  |
| FSpawnerSpawnedCharacter | **[[OnSpawnerSpawnedCharacter]]**  |
| FSpawningEnded | **[[OnSpawningEnded]]**  |
| FSpawningStarted | **[[OnSpawningStarted]]**  |
| TArray< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * > | **[[PendingPossessCharacters]]**  |
| float | **[[PostSpawnPossesionTime]]**  |
| float | **[[RowOffsetPercent]]**  |
| float | **[[RowSpacing]]**  |
| int32 | **[[Rows]]**  |
| float | **[[SnapToGroundDistance]]**  |
| int32 | **[[SpawnLocationIndex]]**  |
| TArray< [FSpawnerSpawnReservation](/docs/SDK/Source/Classes/structFSpawnerSpawnReservation.md) > | **[[SpawnReservations]]**  |
| [FSpawnWaveParamOverrides](/docs/SDK/Source/Classes/structFSpawnWaveParamOverrides.md) | **[[SpawnWaveParams]]**  |
| TArray< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * > | **[[SpawnedCharacters]]**  |
| float | **[[SpawnerScoreMultiplier]]**  |
| [FSpawnScoringConfig](/docs/SDK/Source/Classes/structFSpawnScoringConfig.md) | **[[SpawningConfig]]**  |
| FVector | **[[StartCameraOffset]]**  |
| FRotator | **[[StartCameraRotation]]**  |
| FTransform | **[[StartingSpawnerTransform]]**  |
| float | **[[TimeBeforeVulnerable]]**  |
| bool | **[[bPrioritizeFrontmost]]**  |
| bool | **[[bSkipLocationValidation]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| float | **[[DelayBeforeSpawningStops]]**  |
| TSubclassOf< [USpecialSpawnSpec](/docs/SDK/Source/Classes/classUSpecialSpawnSpec.md) > | **[[SpecialSpawnSpecOverride]]**  |
| bool | **[[bAllowInvalidSpawnLocation]]**  |
| bool | **[[bSkipPawnOverlapTest]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:58 +0200